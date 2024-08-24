namespace CarePackage.Software;

public class BorderlessGaming : BaseSoftware
{
    public override string           Key            { get; set; } = "borderless-gaming";
    public override string           Name           { get; set; } = "Borderless Gaming";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "BorderlessGaming.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.borderless_gaming;
    public override string           Homepage       { get; set; } = "https://github.com/codeusa/borderless-gaming";
    
    private readonly GitHubService _github;

    public BorderlessGaming(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("Codeusa", "Borderless-Gaming", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith(".exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
