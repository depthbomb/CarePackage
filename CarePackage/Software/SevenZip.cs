namespace CarePackage.Software;

public class SevenZip : BaseSoftware
{
    public override string           Key            { get; set; } = "seven-zip";
    public override string           Name           { get; set; } = "7-Zip";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "7zSetup.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons._7zip;
    public override string           Homepage       { get; set; } = "https://7-zip.org";

    private readonly GitHubService _github;

    public SevenZip(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("ip7z", "7zip", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-x64.msi"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
