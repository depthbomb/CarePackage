namespace CarePackage.Software;

public class PowerShellCore : BaseSoftware
{
    public override string           Key            { get; set; } = "powershell-core";
    public override string           Name           { get; set; } = "PowerShell 7";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "PowerShell-win-x64.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.powershell_core;
    public override string           Homepage       { get; set; } = "https://github.com/PowerShell/PowerShell";

    private readonly GitHubService _github;

    public PowerShellCore(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("PowerShell", "PowerShell", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-win-x64.msi"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
