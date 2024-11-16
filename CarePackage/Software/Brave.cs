namespace CarePackage.Software;

public class Brave : BaseSoftware
{
    public override string           Key            { get; set; } = "brave-browser";
    public override string           Name           { get; set; } = "Brave";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "BraveBrowserSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.brave_browser;
    public override string           Homepage       { get; set; } = "https://brave.com";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://laptop-updates.brave.com/download/desktop/release/BRV010?bitness=64");
}
