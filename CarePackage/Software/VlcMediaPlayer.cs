namespace CarePackage.Software;

public class VlcMediaPlayer : BaseSoftware
{
    public override string           Key            { get; set; } = "vlc-media-player";
    public override string           Name           { get; set; } = "VLC Media Player";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "vlc-win64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.vlc_media_player;
    public override string           Homepage       { get; set; } = "https://videolan.org";
    
    private readonly HttpClient _http;

    public VlcMediaPlayer(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var downloadPageUrl = await GetDownloadPageUrlAsync(ct);
        var res             = await _http.GetAsync(downloadPageUrl, ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"<meta http-equiv=""refresh"" content=""5;URL='(.*)'"" />");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[1].Value;
    }

    private async Task<string> GetDownloadPageUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://videolan.org", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"//get\.videolan\.org/vlc/\d{1,}\.\d{1,}\.\d{1,}/win64/vlc-\d{1,}\.\d{1,}\.\d{1,}-win64\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return $"https:{match.Groups[0].Value}";
    }
}
