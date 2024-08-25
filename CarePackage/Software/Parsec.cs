namespace CarePackage.Software;

public class Parsec : BaseSoftware
{
    public override string           Key            { get; set; } = "parsec";
    public override string           Name           { get; set; } = "Parsec";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "parsec-windows.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.parsec;
    public override string           Homepage       { get; set; } = "https://parsec.app";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://builds.parsec.app/package/parsec-windows.exe");
}
