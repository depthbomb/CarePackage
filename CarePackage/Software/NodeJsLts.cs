namespace CarePackage.Software;

public class NodeJsLts : BaseSoftware
{
    public override string           Key            { get; set; } = "nodejs-lts";
    public override string           Name           { get; set; } = "Node.js (LTS)";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "node-lts-x64.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.nodejs;
    public override string           Homepage       { get; set; } = "https://nodejs.org";
    
    private readonly HttpClient _http;

    public NodeJsLts(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://nodejs.org/en", ct);
        
        res.EnsureSuccessStatusCode();
        
        var versionPattern = new Regex(@"dist\/(v\d{2}\.\d{1,2}\.\d{1,})\/node");
        var html           = await res.Content.ReadAsStringAsync(ct);
        var matches        = versionPattern.Matches(html);
        var version = matches
                      .OrderBy(m => new Version(m.Groups[1].Value[1..]))
                      .FirstOrDefault()
                      ?.Groups[1].Value;
        
        DownloadUrlResolveException.ThrowIf(version is null);

        return $"https://nodejs.org/dist/{version}/node-{version}-x64.msi";
    }
}
