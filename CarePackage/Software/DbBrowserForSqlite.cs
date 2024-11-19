namespace CarePackage.Software;

public class DbBrowserForSqlite : BaseSoftware
{
    public override string           Key            { get; set; } = "db-browser-for-sqlite";
    public override string           Name           { get; set; } = "DB Browser for SQLite";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "DB.Browser.for.SQLite-win64.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.db_browser_for_sqlite;
    public override string           Homepage       { get; set; } = "https://sqlitebrowser.org/";
    
    private readonly GitHubService _github;

    public DbBrowserForSqlite(IServiceProvider services)
    {
        _github = services.GetRequiredService<GitHubService>();
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var assets = await _github.GetLatestRepositoryReleaseAssetsAsync("sqlitebrowser", "sqlitebrowser", ct);
        var asset  = assets.FirstOrDefault(a => a.EndsWith("-win64.msi"));
        
        DownloadUrlResolveException.ThrowIf(asset is null);

        return asset;
    }
}
