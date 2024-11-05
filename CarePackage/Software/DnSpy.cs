namespace CarePackage.Software;

public class DnSpy : BaseSoftware
{
    public override string           Key            { get; set; } = "dnspy-ex";
    public override string           Name           { get; set; } = "dnSpy (Fork)";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "dnSpy-net-win64.zip";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dnspy;
    public override string           Homepage       { get; set; } = "https://github.com/dnSpyEx/dnSpy";
    
    private readonly GitHubService _github;

    public DnSpy(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("dnSpyEx", "dnSpy", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("win64.zip"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
