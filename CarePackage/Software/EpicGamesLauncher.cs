namespace CarePackage.Software;

public class EpicGamesLauncher : BaseSoftware
{
    public override string           Key            { get; set; } = "epic-games-launcher";
    public override string           Name           { get; set; } = "Epic Games Launcher";
    public override SoftwareCategory Category       { get; set; } =  SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "EpicGamesLauncherInstaller.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.epic_games_launcher;
    public override string           Homepage       { get; set; } = "https://store.epicgames.com";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi");
}
