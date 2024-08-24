namespace CarePackage.Software;

public class Thunderbird : BaseSoftware
{
    public override string           Key            { get; set; } = "thunderbird";
    public override string           Name           { get; set; } = "Thunderbird";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Social;
    public override string           DownloadName   { get; set; } = "Thunderbird_Setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.thunderbird;
    public override string           Homepage       { get; set; } = "https://thunderbird.net";

    private readonly HttpClient _http;
    
    public Thunderbird(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://thunderbird.net", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://download\.mozilla\.org/\?product=thunderbird-(.*)-SSL&os=win64&lang=en-US");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
