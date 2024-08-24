namespace CarePackage.Software;

public class ShareX : BaseSoftware
{
    public override string           Key            { get; set; } = "sharex";
    public override string           Name           { get; set; } = "ShareX";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "ShareX-setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.sharex;
    public override string           Homepage       { get; set; } = "https://getsharex.com";

    private readonly GitHubService _github;

    public ShareX(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("ShareX", "ShareX", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-setup.exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
