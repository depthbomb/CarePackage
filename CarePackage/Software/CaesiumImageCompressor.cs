namespace CarePackage.Software;

public class CaesiumImageCompressor : BaseSoftware
{
    public override string           Key            { get; set; } = "caesium-image-compressor";
    public override string           Name           { get; set; } = "Caesium Image Compressor";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "caesium-image-compressor-win-setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.caesium_image_compressor;
    public override string           Homepage       { get; set; } = "https://saerasoft.com/caesium";
    
    private readonly GitHubService _github;

    public CaesiumImageCompressor(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("Lymphatus", "caesium-image-compressor", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith(".exe"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
