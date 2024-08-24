namespace CarePackage.Software;

public class HandBrake : BaseSoftware
{
    public override string           Key            { get; set; } = "handbrake";
    public override string           Name           { get; set; } = "HandBrake";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "HandBrake-x86_64-Win_GUI.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.handbrake;
    public override string           Homepage       { get; set; } = "https://handbrake.fr";

    private readonly GitHubService _github;

    public HandBrake(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("HandBrake", "HandBrake", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-x86_64-Win_GUI.exe"));

        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
