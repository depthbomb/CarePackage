namespace CarePackage.Software;

public class Putty : BaseSoftware
{
    public override string           Key            { get; set; } = "putty";
    public override string           Name           { get; set; } = "PuTTY";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "putty-64bit-installer.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.putty;
    public override string           Homepage       { get; set; } = "https://putty.org";

    private readonly HttpClient _http;
    
    public Putty(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://the\.earth\.li/~sgtatham/putty/latest/w64/putty-64bit-\d{1,}\.\d{1,}-installer\.msi");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[0].Value;
    }
}
