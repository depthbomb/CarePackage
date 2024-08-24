using System.Web;

namespace CarePackage.Software;

public class GoogleChrome : BaseSoftware
{
    public override string           Key            { get; set; } = "google-chrome";
    public override string           Name           { get; set; } = "Google Chrome";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "ChromeSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.google_chrome;
    public override string           Homepage       { get; set; } = "https://google.com/chrome";

    private readonly HttpClient _http;

    public GoogleChrome(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var iid         = Guid.NewGuid();
        var appGuid     = await RetrieveStableAppGuidAsync(ct);
        var path        = HttpUtility.UrlEncode($"appguid={appGuid}&iid={iid:B}&lang=en&browser=4&usagestats=0&appname=Google%20Chrome&needsadmin=prefers&ap=x64-statsdef_1&");
        var downloadUrl = $"https://dl.google.com/tag/s/{path}installdataindex=empty/update2/installers/ChromeSetup.exe";

        return downloadUrl;
    }

    private async Task<string> RetrieveStableAppGuidAsync(CancellationToken ct = default)
    {
        var url = new Uri("https://www.google.com/chrome/static/js/installer.min.js");
        var res = await _http.GetAsync(url, ct);

        res.EnsureSuccessStatusCode();

        var appGuidPattern = new Regex(@"stablechannel:""(?<guid>[{(]?[0-9A-F]{8}[-]?(?:[0-9A-F]{4}[-]?){3}[0-9A-F]{12}[)}]?)""");
        var content        = await res.Content.ReadAsStringAsync(ct);
        var match          = appGuidPattern.Match(content);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups["guid"].Value;
    }
}
