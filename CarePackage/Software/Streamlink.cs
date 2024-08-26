namespace CarePackage.Software;

public class Streamlink : BaseSoftware
{
    public override string           Key            { get; set; } = "streamlink";
    public override string           Name           { get; set; } = "Streamlink";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "streamlink-x86_64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.streamlink;
    public override string           Homepage       { get; set; } = "https://streamlink.github.io";

    private readonly GitHubService _github;

    public Streamlink(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets      = await _github.GetLatestRepositoryReleaseAssetsAsync("streamlink", "windows-builds", ct);
        var filePattern = new Regex(@"streamlink-\d{1,}\.\d{1,}\.\d{1,}(?:-\d{1,})?-py3\d{2}-x86_64\.exe");
        var asset       = assets.FirstOrDefault(a => filePattern.IsMatch(a));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
