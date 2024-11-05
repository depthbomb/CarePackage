namespace CarePackage.Software;

public class Arc : BaseSoftware
{
    public override string           Key            { get; set; } = "arc";
    public override string           Name           { get; set; } = "Arc";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "ArcInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.arc;
    public override string           Homepage       { get; set; } = "https://arc.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://releases.arc.net/windows/ArcInstaller.exe");
}
