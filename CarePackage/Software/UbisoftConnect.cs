namespace CarePackage.Software;

public class UbisoftConnect : BaseSoftware
{
    public override string           Key            { get; set; } = "ubisoft-connect";
    public override string           Name           { get; set; } = "Ubisoft Connect";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "UbisoftConnectInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.ubisoft_connect;
    public override string           Homepage       { get; set; } = "https://ubisoft.com/en-us/ubisoft-connect";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://static3.cdn.ubi.com/orbit/launcher_installer/UbisoftConnectInstaller.exe");
}
