namespace CarePackage.Software;

public class TelegramDesktop : BaseSoftware
{
    public override string           Key            { get; set; } = "telegram-desktop";
    public override string           Name           { get; set; } = "Telegram";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Social;
    public override string           DownloadName   { get; set; } = "tsetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.telegram;
    public override string           Homepage       { get; set; } = "https://telegram.org";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://telegram.org/dl/desktop/win64");
}
