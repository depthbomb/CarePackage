namespace CarePackage.Software;

public class Blender : BaseSoftware
{
    public override string           Key            { get; set; } = "blender";
    public override string           Name           { get; set; } = "Blender";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "blender-windows-x64.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.blender;
    public override string           Homepage       { get; set; } = "https://blender.org";

    private readonly HttpClient _http;
    
    public Blender(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var initialRes = await _http.GetAsync("https://www.blender.org/download", ct);
        
        initialRes.EnsureSuccessStatusCode();

        var downloadPageUrlPattern = new Regex(@"https://www\.blender\.org/download/release/Blender\d{1,}\.\d{1,}/blender-\d{1,}\.\d{1,}.\d{1,}-windows-x64\.msi");
        var initialHtml            = await initialRes.Content.ReadAsStringAsync(ct);
        var initialMatch           = downloadPageUrlPattern.Match(initialHtml);
        
        DownloadUrlResolveException.ThrowUnless(initialMatch.Success);

        var downloadUrlPattern = new Regex(@"https://mirror\.clarkson\.edu/blender/release/Blender\d{1,}\.\d{1,}/blender-\d{1,}\.\d{1,}\.\d{1,}-windows-x64\.msi");
        var downloadPageUrl    = initialMatch.Groups[0].Value;
        var downloadPageRes    = await _http.GetAsync(downloadPageUrl, ct);
        var downloadHtml       = await downloadPageRes.Content.ReadAsStringAsync(ct);
        var downloadPageMatch  = downloadUrlPattern.Match(downloadHtml);
        
        DownloadUrlResolveException.ThrowUnless(downloadPageMatch.Success);
        
        return downloadPageMatch.Groups[0].Value;
    }
}
