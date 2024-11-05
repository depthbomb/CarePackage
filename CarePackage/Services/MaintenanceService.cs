using WinRT.Interop;
using System.Reflection;
using Windows.UI.Popups;
using System.Net.Http.Json;

namespace CarePackage.Services;

internal record GithubRelease
{
    [JsonPropertyName("tag_name")]
    public required string Tag { get; init; }
}

public class MaintenanceService
{
    private readonly SettingsService _settings;

    public MaintenanceService(SettingsService settings)
    {
        _settings = settings;
    }
    
    public async Task EnsureFoldersAsync()
    {
        await Task.Run(() =>
        {
            Directory.CreateDirectory(GlobalShared.DownloadFolder);
            Directory.CreateDirectory(GlobalShared.DataFolder);
        });
    }

    public async Task ShowDisclaimerIfRequiredAsync(nint handle)
    {
        var seenDisclaimer = _settings.Get(s => s.SeenDisclaimer);
        var dialog = new MessageDialog("This application is an independent, open-source project and is not affiliated with, endorsed by, or associated with the software it manages. All trademarks and software names are the property of their respective owners.", "Disclaimer")
        {
            Commands            = { new UICommand("OK") },
            DefaultCommandIndex = 0
        };

        if (!seenDisclaimer)
        {
            _settings.Set(s => s with { SeenDisclaimer = true });
            
            InitializeWithWindow.Initialize(dialog, handle);
            
            await dialog.ShowAsync();
            await _settings.CommitAsync();
        }
    }

    public async Task<bool> IsUpdateAvailableAsync(CancellationToken ct = default)
    {
        var currentVersion = Assembly.GetExecutingAssembly().GetName().Version!;

        try
        {
            using (var http = new HttpClient())
            {
                http.DefaultRequestHeaders.Add("User-Agent", GlobalShared.UserAgent);

                var res        = await http.GetAsync("https://api.github.com/repos/depthbomb/carepackage/releases/latest", ct);
                var data       = await res.Content.ReadFromJsonAsync<GithubRelease>(ct);
                var tagVersion = new Version(data!.Tag);

                // Force update if we are currently using calver and the latest release is semver
                if (currentVersion.Major.ToString().Length == 4 && tagVersion.Major.ToString().Length < 4)
                {
                    return true;
                }

                return tagVersion > currentVersion;
            }
        }
        #if DEBUG
        catch (Exception e)
        {
            Console.WriteLine(e);

            return false;
        }
        #else
        catch
        {
            return false;
        }
        #endif
    }

    public async Task CleanUpDownloadFolderAsync(CancellationToken ct = default)
    {
        await Task.Run(() =>
        {
            foreach (var file in Directory.EnumerateFiles(GlobalShared.DownloadFolder))
            {
                ct.ThrowIfCancellationRequested();
                File.Delete(file);
            }
        }, ct);
    }
}
