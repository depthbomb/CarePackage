namespace CarePackage.Software;

public class BattleNet : BaseSoftware
{
    public override string           Key            { get; set; } = "blizzard-battle-net";
    public override string           Name           { get; set; } = "Battle.net";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "Battle.net-Setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.battlenet;
    public override string           Homepage       { get; set; } = "https://battle.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://downloader.battle.net/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live");
}
