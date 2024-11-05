namespace CarePackage.Software;

public class JetBrainsToolbox : BaseSoftware
{
    public override string           Key            { get; set; } = "jetbrains-toolbox";
    public override string           Name           { get; set; } = "JetBrains Toolbox";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "jetbrains-toolbox.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.jetbrains_toolbox;
    public override string           Homepage       { get; set; } = "https://jetbrains.com/toolbox-app";

    private readonly HttpClient _http;
    
    public JetBrainsToolbox(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://download\.jetbrains\.com/toolbox/jetbrains-toolbox-\d+\.\d+\.\d+\.\d+\.exe\b");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[0].Value;
    }
}
