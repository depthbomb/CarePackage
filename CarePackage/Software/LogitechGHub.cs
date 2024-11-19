namespace CarePackage.Software;

public class LogitechGHub : BaseSoftware
{
    public override string           Key            { get; set; } = "logitech-g-hub";
    public override string           Name           { get; set; } = "Logitech G HUB";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Peripheral;
    public override string           DownloadName   { get; set; } = "lghub_installer.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.logitech_g_hub;
    public override string           Homepage       { get; set; } = "https://www.logitechg.com/en-us/innovation/g-hub.html";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe");
}
