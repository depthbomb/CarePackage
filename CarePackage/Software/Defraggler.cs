namespace CarePackage.Software;

public class Defraggler : BaseSoftware
{
    public override string           Key            { get; set; } = "defraggler";
    public override string           Name           { get; set; } = "Defraggler";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "dfsetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.defraggler;
    public override string           Homepage       { get; set; } = "https://ccleaner.com/defraggler";

    private readonly HttpClient _http;
    
    public Defraggler(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.ccleaner.com/defraggler/download/standard", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://download\.ccleaner\.com/dfsetup(\d){3,}\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        var downloadUrl = match.Groups[0].Value;

        return downloadUrl;
    }
}
