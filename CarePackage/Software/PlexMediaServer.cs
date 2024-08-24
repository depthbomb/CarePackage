namespace CarePackage.Software;

public class PlexMediaServer : BaseSoftware
{
    public override string           Key            { get; set; } = "plex-media-server";
    public override string           Name           { get; set; } = "Plex Media Server";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "PlexMediaServer-x86_64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.plex_media_server;
    public override string           Homepage       { get; set; } = "https://plex.tv";

    private readonly HttpClient _http;
    
    public PlexMediaServer(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://plex.tv/api/downloads/5.json", ct);
        
        res.EnsureSuccessStatusCode();
        
        var downloadUrlPattern = new Regex(@"https://downloads\.plex\.tv/plex-media-server-new/\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}-[a-f0-9]{9}/windows/PlexMediaServer-\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}-[a-f0-9]{9}-x86_64\.exe");
        var json  = await res.Content.ReadAsStringAsync(ct);
        var match = downloadUrlPattern.Match(json);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
