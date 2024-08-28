namespace CarePackage.Services;

public class DownloadService
{
    public event EventHandler?               QueueDownloadingStarted;
    public event EventHandler?               QueueDownloadingComplete;
    public event EventHandler<BaseSoftware>? SoftwareDownloadUrlResolving;
    public event EventHandler<BaseSoftware>? SoftwareDownloadStarted;
    public event ProgressChangedHandler?     SoftwareDownloadProgressChanged;
    public event EventHandler<BaseSoftware>? SoftwareDownloadCompleted;

    public readonly ObservableCollection<BaseSoftware> Queue = [];

    public delegate void ProgressChangedHandler(long?        totalFileSize,
                                                long         totalBytesDownloaded,
                                                double?      progressPercentage,
                                                BaseSoftware software);

    private readonly HttpClient                 _http;
    private readonly Dictionary<string, string> _urlCache = [];

    public DownloadService([FromKeyedServices("MimicBrowser")] HttpClient http)
    {
        _http = http;
    }

    public async Task<List<SoftwareInstallationInfo>> DownloadQueueAsync(CancellationToken ct = default)
    {
        QueueDownloadingStarted?.Invoke(this, EventArgs.Empty);

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

                var totalBytes = res.Content.Headers.ContentLength;

                await using (var cs = await res.Content.ReadAsStreamAsync(ct))
                {
                    var totalBytesRead = 0L;
                    var readCount      = 0L;
                    var buffer         = new byte[8192];
                    var isMoreToRead   = true;

                    await using (var fileStream = new FileStream(downloadFile, FileMode.Create, FileAccess.Write, FileShare.None, 8192, true))
                    {
                        do
                        {
                            var bytesRead = await cs.ReadAsync(buffer, ct);
                            if (bytesRead == 0)
                            {
                                isMoreToRead = false;
                                TriggerProgressChanged(totalBytes, totalBytesRead, software);
                                continue;
                            }

                            await fileStream.WriteAsync(buffer.AsMemory(0, bytesRead), ct);

                            totalBytesRead += bytesRead;
                            readCount      += 1;

                            if (readCount % 100 == 0)
                            {
                                TriggerProgressChanged(totalBytes, totalBytesRead, software);
                            }
                        } while (isMoreToRead);
                    }
                }

                SoftwareDownloadCompleted?.Invoke(this, software);

                payloads.Add(new SoftwareInstallationInfo
                {
                    Software           = software,
                    ExecutableLocation = downloadFile
                });
            }
            catch (OperationCanceledException) { }
        }

        QueueDownloadingComplete?.Invoke(this, EventArgs.Empty);

        return payloads;
    }

    private void TriggerProgressChanged(long? totalDownloadSize, long totalBytesRead, BaseSoftware software)
    {
        if (SoftwareDownloadProgressChanged == null)
        {
            return;
        }

        double? progressPercentage = null;
        if (totalDownloadSize.HasValue)
        {
            progressPercentage = Math.Round((double)totalBytesRead / totalDownloadSize.Value * 100, 2);
        }

        SoftwareDownloadProgressChanged(totalDownloadSize, totalBytesRead, progressPercentage, software);
    }
}
