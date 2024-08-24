namespace CarePackage.Software;

public class Discord : BaseSoftware
{
    public override string           Key            { get; set; } = "discord-stable";
    public override string           Name           { get; set; } = "Discord";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Social;
    public override string           DownloadName   { get; set; } = "DiscordSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.discord;
    public override string           Homepage       { get; set; } = "https://discord.com";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64");
}
