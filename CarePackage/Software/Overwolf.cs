namespace CarePackage.Software;

public class Overwolf : BaseSoftware
{
    public override string           Key            { get; set; } = "overwolf";
    public override string           Name           { get; set; } = "Overwolf";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "OverwolfSetup.zip";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.overwolf;
    public override string           Homepage       { get; set; } = "https://overwolf.com";

    private readonly HttpClient _http;

    public Overwolf(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://content.overwolf.com/downloads/setup/latest/regular.html", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://setup-overwolf-com\.akamaized\.net/\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}/OverwolfSetup\.zip");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
