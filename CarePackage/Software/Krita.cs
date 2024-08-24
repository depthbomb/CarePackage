namespace CarePackage.Software;

public class Krita : BaseSoftware
{
    public override string           Key            { get; set; } = "krita";
    public override string           Name           { get; set; } = "Krita";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "krita-x64-setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.krita;
    public override string           Homepage       { get; set; } = "https://krita.org";

    private readonly HttpClient _http;

    public Krita(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://krita.org/en/download", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://download\.kde\.org/stable/krita/\d{1,}\.\d{1,}\.\d{1,}/krita-x64-\d{1,}\.\d{1,}\.\d{1,}-setup\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[0].Value;
    }
}
