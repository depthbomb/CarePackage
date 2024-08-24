using System.Reflection;
using Windows.UI.Popups;
using System.Net.Http.Json;

namespace CarePackage.Services;

internal record GithubRelease
{
    [JsonPropertyName("tag_name")]
    public required string Tag { get; set; }
}

public class MaintenanceService
{
    public async Task EnsureFoldersAsync()
    {
        await Task.Run(() =>
        {
            Directory.CreateDirectory(GlobalShared.DownloadFolder);
            Directory.CreateDirectory(GlobalShared.DataFolder);
        });
    }

    public bool HasSeenDisclaimer(out MessageDialog disclaimerDialog)
    {
        var disclaimerFile = Path.Combine(GlobalShared.DataFolder, "SeenDisclaimer");

        disclaimerDialog = new MessageDialog("This application is an independent, open-source project and is not affiliated with, endorsed by, or associated with the software it manages. All trademarks and software names are the property of their respective owners.", "Disclaimer")
        {
            Commands            = { new UICommand("OK") },
            DefaultCommandIndex = 0
        };

        if (!File.Exists(disclaimerFile))
        {
            File.Create(disclaimerFile).Dispose();
            return false;
        }

        return true;
    }

    public async Task<bool> IsUpdateAvailableAsync(CancellationToken ct = default)
    {
        try
        {
            using (var http = new HttpClient())
            {
                http.DefaultRequestHeaders.Add("User-Agent", GlobalShared.UserAgent);

                var res        = await http.GetAsync("https://api.github.com/repos/depthbomb/carepackage/releases/latest", ct);
                var data       = await res.Content.ReadFromJsonAsync<GithubRelease>(ct);
                var tagVersion = new Version(data!.Tag);
                
                return tagVersion >= Assembly.GetExecutingAssembly().GetName().Version;
            }
        }
        catch (Exception e)
        {
            #if DEBUG
            Console.WriteLine(e);
            #endif

            return false;
        }
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
