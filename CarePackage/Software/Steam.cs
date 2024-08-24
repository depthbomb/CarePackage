namespace CarePackage.Software;

public class Steam : BaseSoftware
{
    public override string           Key            { get; set; } = "steam";
    public override string           Name           { get; set; } = "Steam";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "SteamSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.steam;
    public override string           Homepage       { get; set; } = "https://store.steampowered.com";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe");
}
