namespace CarePackage.Software;

public class ElgatoStreamDeck : BaseSoftware
{
    public override string           Key            { get; set; } = "elgato-stream-deck";
    public override string           Name           { get; set; } = "Elgato Stream Deck";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Peripheral;
    public override string           DownloadName   { get; set; } = "Stream_Deck.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.elgato_stream_deck;
    public override string           Homepage       { get; set; } = "https://help.elgato.com/hc/en-us/sections/5162671529357-Elgato-Stream-Deck-Software-Release-Notes";

    private readonly HttpClient _http;
    
    public ElgatoStreamDeck(IServiceProvider services)
    {
        _http = services.GetKeyedService<HttpClient>("MimicBrowser")!;
    }

    public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
    {
        var res = await _http.GetAsync("https://www.elgato.com/us/en/s/downloads", ct);

        res.EnsureSuccessStatusCode();

        var downloadUrlPattern = new Regex(@"https://edge\.elgato\.com/egc/windows/sd/Stream_Deck_\d+\.\d+\.\d+\.\d+\.msi");
        var html               = await res.Content.ReadAsStringAsync(ct);
        var match              = downloadUrlPattern.Match(html);
        
        DownloadUrlResolveException.ThrowUnless(match.Success);

        return match.Groups[0].Value;
    }
}
