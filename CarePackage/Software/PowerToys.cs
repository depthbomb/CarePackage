namespace CarePackage.Software;

public class PowerToys : BaseSoftware
{
    public override string           Key            { get; set; } = "microsoft-powertoys";
    public override string           Name           { get; set; } = "PowerToys";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "PowerToysUserSetup-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.powertoys;
    public override string           Homepage       { get; set; } = "https://learn.microsoft.com/en-us/windows/powertoys";

    private readonly GitHubService _github;
    
    public PowerToys(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("microsoft", "PowerToys", ct);
        var asset  = assets.FirstOrDefault(a => a.Contains("PowerToysSetup-") && a.EndsWith("-x64.exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);
        
        return asset;
    }
}
