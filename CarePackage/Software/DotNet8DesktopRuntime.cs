namespace CarePackage.Software;

public class DotNet8DesktopRuntime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-8-desktop-runtime";
    public override string           Name           { get; set; } = ".NET 8.0 Desktop Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "windowsdesktop-runtime-8.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    private readonly HttpClient _http;
    
    public DotNet8DesktopRuntime(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var downloadPageUrl = await GetDownloadPageUrlAsync(ct);
        var res             = await _http.GetAsync(downloadPageUrl, ct);

        res.EnsureSuccessStatusCode();
        
        var downloadUrlPattern = new Regex(@"https://download\.visualstudio\.microsoft\.com/download/pr/(?i)[0-9A-F]{8}[-]?(?:[0-9A-F]{4}[-]?){3}[0-9A-F]{12}?/[\da-f]{32}/windowsdesktop-runtime-8\.\d{1,}\.\d{1,}-win-x64\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }

    private async Task<string> GetDownloadPageUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://dotnet.microsoft.com/en-us/download/dotnet/8.0", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadPageUrlPattern = new Regex(@"/en-us/download/dotnet/thank-you/runtime-desktop-8\.\d{1,}\.\d{1,}-windows-x64-installer");
        var html                   = await res.Content.ReadAsStringAsync(ct);
        var match                  = downloadPageUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return $"https://dotnet.microsoft.com{match.Groups[0].Value}";
    }
}
