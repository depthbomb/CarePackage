namespace CarePackage.Software;

public class OperaGx : BaseSoftware
{
    public override string           Key            { get; set; } = "opera-gx";
    public override string           Name           { get; set; } = "Opera GX";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "OperaGXSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.operagx;
    public override string           Homepage       { get; set; } = "https://opera.com/gx";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://net.geo.opera.com/opera_gx/stable/windows");
}
