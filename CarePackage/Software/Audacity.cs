namespace CarePackage.Software;

public class Audacity : BaseSoftware
{
    public override string           Key            { get; set; } = "audacity";
    public override string           Name           { get; set; } = "Audacity";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "audacity-win-64bit.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.audacity;
    public override string           Homepage       { get; set; } = "https://audacityteam.org";

    private readonly GitHubService _github;

    public Audacity(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets       = await _github.GetLatestRepositoryReleaseAssetsAsync("audacity", "audacity", ct);
        var asset = assets.FirstOrDefault(a => a.EndsWith("-64bit.exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
