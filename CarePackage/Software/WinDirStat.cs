namespace CarePackage.Software;

public class WinDirStat : BaseSoftware
{
    public override string           Key            { get; set; } = "windirstat";
    public override string           Name           { get; set; } = "WinDirStat";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "wds_current_setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.windirstat;
    public override string           Homepage       { get; set; } = "https://windirstat.net";

    private readonly HttpClient _http;
    
    public WinDirStat(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("Wget")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://windirstat.net/wds_current_setup.exe", ct);

        res.EnsureSuccessStatusCode();
        
        return res.RequestMessage!.RequestUri!.ToString();
    }
}
