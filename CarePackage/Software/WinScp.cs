namespace CarePackage.Software;

public class WinScp : BaseSoftware
{
    public override string           Key            { get; set; } = "winscp";
    public override string           Name           { get; set; } = "WinSCP";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "WinSCP-Setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.winscp;
    public override string           Homepage       { get; set; } = "https://winscp.net";

    private readonly HttpClient _http;
    
    public WinScp(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var installerName = await GetInstallerNameAsync(ct);
        var res           = await _http.GetAsync($"https://winscp.net/download/{installerName}/download", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"<a rel=""nofollow"" href=""(.*)"" class=""btn btn-primary btn-lg"">Direct download</a>");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[1].Value;
    }

    private async Task<string> GetInstallerNameAsync(CancellationToken ct = default)
    {
        var res = await _http.GetAsync("https://winscp.net/eng/download.php", ct);
        
        res.EnsureSuccessStatusCode();

        var installerNamePattern = new Regex(@"WinSCP-\d{1,}\.\d{1,}\.\d{1,}-Setup\.exe");
        var html                 = await res.Content.ReadAsStringAsync(ct);
        var match                = installerNamePattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
