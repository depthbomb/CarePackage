using System.Text;
using System.Text.Json;
using System.Net.Http.Json;

namespace CarePackage.Software;

internal record ProjectSettings
{
    [JsonPropertyName("pageName")]
    public required string PageName { get; set; }
    
    [JsonPropertyName("projectId")]
    public required string ProjectId { get; set; }
    
    [JsonPropertyName("pool")]
    public required ProjectPool Pool { get; set; }
}

internal record ProjectPool
{
    [JsonPropertyName("f")]
    public required ProjectPoolFile[] Files { get; set; }
}

internal record ProjectPoolFile
{
    [JsonPropertyName("n")]
    public required string FileName { get; set; }
    
    [JsonPropertyName("r")]
    public required string ReleaseId { get; set; }
}

internal record DownloadRequestResponse
{
    [JsonPropertyName("data")]
    public required DownloadRequestData Data {get; set; }
}

internal record DownloadRequestData
{
    [JsonPropertyName("url")]
    public required string Url { get; set; }
}

public class QBittorrent : BaseSoftware
{
    public override string           Key            { get; set; } = "qbittorrent";
    public override string           Name           { get; set; } = "qBittorrent";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "qbittorrent_x64_setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.qbittorrent;
    public override string           Homepage       { get; set; } = "https://qbittorrent.org";
    
    private readonly HttpClient _http;
    
    public QBittorrent(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var html            = await GetDownloadPageHtmlAsync(ct);
        var settingsPattern = new Regex(@"<script>\s+var settings =(.*)\s+</script>", RegexOptions.Multiline);
        var settingsMatch   = settingsPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(settingsMatch.Success);
        
        var json = settingsMatch.Groups[1].Value;
        var data = JsonSerializer.Deserialize<ProjectSettings>(json);
        
        DownloadUrlResolveException.ThrowIf(data is null);
        
        var latestFile = data.Pool.Files.First(f => f.FileName.EndsWith("_setup.exe"));
        var downloadUrlRequestPayload = $$"""
        {
            "projectId": "{{data.ProjectId}}",
            "releaseId": "{{latestFile.ReleaseId}}",
            "projectUri": "{{data.PageName}}.html",
            "fileName": "{{latestFile.FileName}}",
            "source": "CF"
        }
""";
        var downloadUrl = await RequestDownloadUrlAsync(downloadUrlRequestPayload, ct);
        
        return downloadUrl;
    }

    private async Task<string> GetDownloadPageHtmlAsync(CancellationToken ct = default)
    {
        var res = await _http.GetAsync("https://www.fosshub.com/qBittorrent.html", ct);

        res.EnsureSuccessStatusCode();

        return await res.Content.ReadAsStringAsync(ct);
    }

    private async Task<string> RequestDownloadUrlAsync(string payload, CancellationToken ct = default)
    {
        var json = new StringContent(payload, Encoding.UTF8, "application/json");
        var res  = await _http.PostAsync("https://api.fosshub.com/download/", json, ct);
        
        res.EnsureSuccessStatusCode();

        var data = await res.Content.ReadFromJsonAsync<DownloadRequestResponse>(ct);
        if (data is null)
        {
            throw new Exception("Could not deserialize data.");
        }

        return data.Data.Url;
    }
}
