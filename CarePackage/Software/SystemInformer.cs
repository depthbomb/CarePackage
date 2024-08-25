namespace CarePackage.Software;

public class SystemInformer : BaseSoftware
{
    public override string           Key            { get; set; } = "system-informer";
    public override string           Name           { get; set; } = "System Informer";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "systeminformer-setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.system_informer;
    public override string           Homepage       { get; set; } = "https://systeminformer.sourceforge.io";

    private readonly HttpClient _http;
    
    public SystemInformer(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var fileName        = await GetDownloadFileNameAsync(ct);
        var mirrorDialogUrl = $"https://sourceforge.net/settings/mirror_choices?projectname=systeminformer&filename={fileName}&selected=auto&dialog=true";
        var res             = await _http.GetAsync(mirrorDialogUrl, ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"<a href=""(.*)"" rel=""nofollow"">");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[1].Value;
    }

    private async Task<string> GetDownloadFileNameAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://systeminformer.sourceforge.io/downloads", ct);

        res.EnsureSuccessStatusCode();

        var fileNamePattern = new Regex(@"https://sourceforge\.net/projects/systeminformer/files/(systeminformer-\d{1,}\.\d{1,}\.\d{1,}-release-setup\.exe)/download");
        var html            = await res.Content.ReadAsStringAsync(ct);
        var match           = fileNamePattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[1].Value;
    }
}
