namespace CarePackage.Software;

public class Gimp : BaseSoftware
{
    public override string           Key            { get; set; } = "gimp";
    public override string           Name           { get; set; } = "GIMP";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "GimpSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.gimp;
    public override string           Homepage       { get; set; } = "https://gimp.org";

    private readonly HttpClient _http;

    public Gimp(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.gimp.org/downloads/", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"//download\.gimp\.org/gimp/v\d{1,}\.\d{1,}/windows/gimp-\d{1,}\.\d{1,}\.\d{1,}-setup(-\d{1,})\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return $"https:{match.Groups[0].Value}";
    }
}
