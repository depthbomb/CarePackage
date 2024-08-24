namespace CarePackage.Software;

public class Insomnia : BaseSoftware
{
    public override string           Key            { get; set; } = "insomnia";
    public override string           Name           { get; set; } = "Insomnia";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "Insomnia.Core.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.insomnia;
    public override string           Homepage       { get; set; } = "https://insomnia.rest";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website");
}
