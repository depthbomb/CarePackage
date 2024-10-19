namespace CarePackage.Software;

public class WinDirStat : BaseSoftware
{
    public override string           Key            { get; set; } = "windirstat";
    public override string           Name           { get; set; } = "WinDirStat";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "WinDirStat-x64.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.windirstat;
    public override string           Homepage       { get; set; } = "https://windirstat.net";

    private readonly GitHubService _github;
    
    public WinDirStat(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("windirstat", "windirstat", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-x64.msi"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
