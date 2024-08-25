namespace CarePackage.Software;

public class FileZilla : BaseSoftware
{
    public override string           Key            { get; set; } = "filezilla";
    public override string           Name           { get; set; } = "FileZilla";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "FileZilla_win64-setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.filezilla;
    public override string           Homepage       { get; set; } = "https://filezilla-project.org";

    private readonly HttpClient _http;
    
    public FileZilla(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var req = new HttpRequestMessage(HttpMethod.Get, "https://filezilla-project.org/download.php?show_all=1");
        req.Headers.Add("Accept", "*/*"); // Their site doesn't like it when this header isn't sent
        var res = await _http.SendAsync(req, ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://dl\d{1,}\.cdn\.filezilla-project\.org/client/FileZilla_\d{1,}\.\d{1,}\.\d{1,}_win64-setup\.exe\?h=[a-zA-Z0-9-_]{22,}&x=\d{10,}");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[0].Value;
    }
}
