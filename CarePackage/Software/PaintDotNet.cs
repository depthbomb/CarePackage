namespace CarePackage.Software;

public class PaintDotNet : BaseSoftware
{
    public override string           Key            { get; set; } = "paint-dot-net";
    public override string           Name           { get; set; } = "Paint.NET";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "Paint.NET.zip";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.paintdotnet;
    public override string           Homepage       { get; set; } = "https://getpaint.net";
    
    private readonly GitHubService _github;

    public PaintDotNet(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("paintdotnet", "release", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith(".install.x64.zip"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
