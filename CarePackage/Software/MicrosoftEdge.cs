namespace CarePackage.Software;

public class MicrosoftEdge : BaseSoftware
{
    public override string           Key            { get; set; } = "microsoft-edge";
    public override string           Name           { get; set; } = "Microsoft Edge";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "MicrosoftEdgeSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.microsoft_edge;
    public override string           Homepage       { get; set; } = "https://microsoft.com/en-us/edge";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=en&brand=M100");
}
