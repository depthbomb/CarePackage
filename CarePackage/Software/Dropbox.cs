namespace CarePackage.Software;

public class Dropbox : BaseSoftware
{
    public override string           Key            { get; set; } = "dropbox";
    public override string           Name           { get; set; } = "Dropbox";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
    public override string           DownloadName   { get; set; } = "DropboxInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dropbox;
    public override string           Homepage       { get; set; } = "https://dropbox.com";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://www.dropbox.com/download?os=win&plat=win");
}
