namespace CarePackage.Services;

public class DownloadService
{
    public event EventHandler<BaseSoftware>? SoftwareDownloadUrlResolving;
    public event EventHandler<BaseSoftware>? SoftwareDownloadUrlResolvingError;
    public event EventHandler<BaseSoftware>? SoftwareDownloadStarted;
    public event EventHandler<BaseSoftware>? SoftwareDownloadCompleted;

    public readonly ObservableCollection<BaseSoftware> Queue = [];

    private readonly HttpClient                 _http;
    private readonly Dictionary<string, string> _urlCache = [];

    public DownloadService([FromKeyedServices("MimicBrowser")] HttpClient http)
    {
        _http = http;
    }

    public async Task<List<SoftwareInstallationInfo>> DownloadQueueAsync(CancellationToken ct = default)
    {
        var payloads = new List<SoftwareInstallationInfo>();

        foreach (var software in Queue)
        {
            try
            {
                SoftwareDownloadUrlResolving?.Invoke(this, software);

                var key = software.Key;
                if (!software.ShouldCacheUrl || !_urlCache.TryGetValue(key, out var url))
                {
                    url = await software.GetDownloadUrlAsync(ct);

                    if (software.ShouldCacheUrl)
                    {
                        _urlCache.TryAdd(key, url);
                    }
                }

                var downloadFile = Path.Combine(GlobalShared.DownloadFolder, software.DownloadName);
                if (File.Exists(downloadFile))
                {
                    File.Delete(downloadFile);
                }

                SoftwareDownloadStarted?.Invoke(this, software);

                var res = await _http.GetAsync(url, HttpCompletionOption.ResponseHeadersRead, ct);
                if (!res.IsSuccessStatusCode)
                {
                    MessageBox.Show(
                        $"Failed to download asset for {software.Name}.\n\n{res.ReasonPhrase}",
                        "Download Failed",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Error
                    );
                    continue;
                }
                
                await using (var cs = await res.Content.ReadAsStreamAsync(ct))
                await using (var fs = new FileStream(downloadFile, FileMode.Create, FileAccess.Write, FileShare.None, 8192, true))
                {
                    await cs.CopyToAsync(fs, ct);
                }

                SoftwareDownloadCompleted?.Invoke(this, software);

                payloads.Add(new SoftwareInstallationInfo
                {
                    Software           = software,
                    ExecutableLocation = downloadFile
                });
            }
            catch (Exception ex) when (ex is DownloadUrlResolveException or HttpRequestException)
            {
                SoftwareDownloadUrlResolvingError?.Invoke(this, software);
            }
            catch (OperationCanceledException)
            {
                //
            }
        }

        return payloads;
    }
}
