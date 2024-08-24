namespace CarePackage.Software;

public class NotepadPlusPlus : BaseSoftware
{
    public override string           Key            { get; set; } = "notepad-plus-plus";
    public override string           Name           { get; set; } = "Notepad++";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "npp.Installer.x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.notepad_plus_plus;
    public override string           Homepage       { get; set; } = "https://notepad-plus-plus.org";

    private readonly GitHubService _github;
    
    public NotepadPlusPlus(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("notepad-plus-plus", "notepad-plus-plus", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith(".Installer.x64.exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);
        
        return asset;
    }
}
