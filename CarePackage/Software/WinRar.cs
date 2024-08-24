namespace CarePackage.Software;

public class WinRar : BaseSoftware
{
    public override string           Key            { get; set; } = "winrar";
    public override string           Name           { get; set; } = "WinRAR";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "winrar-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.winrar;
    public override string           Homepage       { get; set; } = "https://win-rar.com";

    private readonly HttpClient _http;

    public WinRar(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.win-rar.com/postdownload.html?&L=0", ct);
        
        res.EnsureSuccessStatusCode();
        
        var downloadPathPattern = new Regex(@"/fileadmin/winrar-versions/winrar/th/winrar-x64-\d{1,}\.exe");
        var html                = await res.Content.ReadAsStringAsync(ct);
        var match               = downloadPathPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return $"https://www.win-rar.com{match.Groups[0].Value}";
    }
}
