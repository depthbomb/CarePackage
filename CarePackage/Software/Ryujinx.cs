namespace CarePackage.Software;

public class Ryujinx : BaseSoftware
{
    public override string           Key            { get; set; } = "ryujinx";
    public override string           Name           { get; set; } = "Ryujinx";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "ryujinx-win_x64.zip";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.ryujinx;
    public override string           Homepage       { get; set; } = "https://ryujinx.org";

    private readonly GitHubService _github;

    public Ryujinx(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets      = await _github.GetLatestRepositoryReleaseAssetsAsync("Ryujinx", "release-channel-master", ct);
        var filePattern = new Regex(@"ryujinx-\d{1,}\.\d{1,}\.\d{1,}-win_x64\.zip");
        var asset       = assets.FirstOrDefault(a => filePattern.IsMatch(a));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
