namespace CarePackage.Software;

public class PlayStationAccessories : BaseSoftware
{
    public override string           Key            { get; set; } = "playstation-accessories";
    public override string           Name           { get; set; } = "PlayStation Accessories";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Peripheral;
    public override string           DownloadName   { get; set; } = "PlayStationAccessoriesInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.playstation_accessories;
    public override string           Homepage       { get; set; } = "https://controller.dl.playstation.net/controller/lang/en/2100004.html";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://fwupdater.dl.playstation.net/fwupdater/PlayStationAccessoriesInstaller.exe");
}
