namespace CarePackage.Software;

public class Postman : BaseSoftware
{
    public override string           Key            { get; set; } = "postman";
    public override string           Name           { get; set; } = "Postman";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "Postman-win64-Setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.postman;
    public override string           Homepage       { get; set; } = "https://postman.com";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://dl.pstmn.io/download/latest/win64");
}
