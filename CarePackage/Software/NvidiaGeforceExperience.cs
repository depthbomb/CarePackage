namespace CarePackage.Software;

public class NvidiaGeforceExperience : BaseSoftware
{
    public override string           Key            { get; set; } = "nvidia-geforce-experience";
    public override string           Name           { get; set; } = "NVIDIA GeForce Experience";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Peripheral;
    public override string           DownloadName   { get; set; } = "GeForce_Experience.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.nvidia_geforce_experience;
    public override string           Homepage       { get; set; } = "https://nvidia.com/en-us/geforce/geforce-experience";

    private readonly HttpClient _http;

    public NvidiaGeforceExperience(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.nvidia.com/en-us/geforce/geforce-experience/", ct);
        
        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://us\.download\.nvidia\.com/GFE/GFEClient/\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}/GeForce_Experience_v\d{1,}\.\d{1,}\.\d{1,}\.\d{1,}\.exe");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);
        
        return match.Groups[0].Value;
    }
}
