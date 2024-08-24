namespace CarePackage.Software;

public class Opera : BaseSoftware
{
    public override string           Key            { get; set; } = "opera";
    public override string           Name           { get; set; } = "Opera";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "OperaSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.opera;
    public override string           Homepage       { get; set; } = "https://opera.com";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://net.geo.opera.com/opera/stable/windows");
}
