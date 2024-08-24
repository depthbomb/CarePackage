namespace CarePackage.Software;

public class DolphinEmulator : BaseSoftware
{
    public override string           Key            { get; set; } = "dolphin-emulator";
    public override string           Name           { get; set; } = "Dolphin Emulator";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "DolphinEmu.7z";
    public override bool             IsArchive      { get; set; } = true;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dolphin_emu;
    public override string           Homepage       { get; set; } = "https://dolphin-emu.org";

    private readonly HttpClient _http;

    public DolphinEmulator(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }
    
    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://dolphin-emu.org/download/list/releases/1/", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://dl\.dolphin-emu\.org/(?:releases/\d+|builds/[\da-f]{2}/[\da-f]{2})/dolphin-(?:\d+|master-\d+\.\d+-\d+)-x64\.7z");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var matches            = downloadUrlPattern.Matches(html);
        var downloadUrl        = matches.FirstOrDefault()?.Value;
        
        DownloadUrlResolveException.ThrowIf(downloadUrl is null);

        return downloadUrl;
    }
}
