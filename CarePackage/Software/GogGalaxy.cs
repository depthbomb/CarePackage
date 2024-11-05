namespace CarePackage.Software;

public class GogGalaxy : BaseSoftware
{
    public override string           Key            { get; set; } = "gog-galaxy";
    public override string           Name           { get; set; } = "GOG GALAXY";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "GOG_Galaxy_2.0.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.gog_galaxy;
    public override string           Homepage       { get; set; } = "https://www.gog.com/galaxy";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe");
}
