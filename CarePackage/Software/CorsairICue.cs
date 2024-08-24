namespace CarePackage.Software;

public class CorsairICue : BaseSoftware
{
    public override string           Key            { get; set; } = "corsair-icue";
    public override string           Name           { get; set; } = "Corsair iCUE";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Peripheral;
    public override string           DownloadName   { get; set; } = "Install_iCue.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.corsair_icue;
    public override string           Homepage       { get; set; } = "https://corsair.com/us/en/s/icue";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://www3.corsair.com/software/CUE_V5/public/modules/windows/installer/Install%20iCUE.exe");
}
