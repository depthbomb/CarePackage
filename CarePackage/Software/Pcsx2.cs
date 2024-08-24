namespace CarePackage.Software;

public class Pcsx2 : BaseSoftware
{
    public override string           Key            { get; set; } = "pcsx2-stable";
    public override string           Name           { get; set; } = "PCSX2";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "PCSX2.7z";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.pcsx2;
    public override string           Homepage       { get; set; } = "https://pcsx2.net";
    
    private readonly GitHubService _github;

    public Pcsx2(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("pcsx2", "pcsx2", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("windows-x64-Qt.7z"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
