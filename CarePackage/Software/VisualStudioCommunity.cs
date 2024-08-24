namespace CarePackage.Software;

public class VisualStudioCommunity : BaseSoftware
{
    public override string           Key            { get; set; } = "visual-studio-community";
    public override string           Name           { get; set; } = "Visual Studio 2022 Community";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "VisualStudioSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.visual_studio_community;
    public override string           Homepage       { get; set; } = "https://visualstudio.microsoft.com";

    private readonly HttpClient _http;
    
    public VisualStudioCommunity(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https:\/\/c2rsetup\.officeapps\.live\.com\/c2r\/downloadVS\.aspx\?sku=community&channel=Release&version=VS\d{4}&passive=true");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        var downloadUrl = match.Groups[0].Value;

        return downloadUrl;
    }
}
