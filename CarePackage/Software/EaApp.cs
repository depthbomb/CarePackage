namespace CarePackage.Software;

public class EaApp : BaseSoftware
{
    public override string           Key            { get; set; } = "ea-app";
    public override string           Name           { get; set; } = "EA App";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "EAappInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.ea_app;
    public override string           Homepage       { get; set; } = "https://ea.com/ea-app";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe");
}
