namespace CarePackage.Software;

public class ObsStudio : BaseSoftware
{
    public override string           Key            { get; set; } = "obs-studio";
    public override string           Name           { get; set; } = "OBS Studio";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "OBS-Studio-Windows-Installer.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.obs_studio;
    public override string           Homepage       { get; set; } = "https://obsproject.com";

    private readonly HttpClient _http;

    public ObsStudio(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://obsproject.com/download", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://cdn-fastly\.obsproject\.com/downloads/OBS-Studio-\d{1,}.\d{1,}.\d{1,}-Windows-Installer\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
