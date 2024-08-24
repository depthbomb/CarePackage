namespace CarePackage.Software;

public class Foobar2000 : BaseSoftware
{
    public override string           Key            { get; set; } = "foobar2000";
    public override string           Name           { get; set; } = "foobar2000";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "foobar2000-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.foobar2000;
    public override string           Homepage       { get; set; } = "https://foobar2000.org";

    private readonly HttpClient _http;

    public Foobar2000(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.foobar2000.org/download", ct);

        res.EnsureSuccessStatusCode();

        var downloadNamePattern = new Regex(@"foobar2000-x64_v\d{1,}\.\d{1,}\.\d{1,}\.exe");
        var html                = await res.Content.ReadAsStringAsync(ct);
        var match               = downloadNamePattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        var downloadFileName = match.Groups[0].Value;

        return $"https://foobar2000.org/files/{downloadFileName}";
    }
}
