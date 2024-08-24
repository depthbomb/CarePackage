namespace CarePackage.Software;

public class MinecraftLauncherLegacy : BaseSoftware
{
    public override string           Key            { get; set; } = "minecraft-launcher-legacy";
    public override string           Name           { get; set; } = "Minecraft Launcher (Legacy)";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "MinecraftInstaller.msi";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.minecraft_launcher_legacy;
    public override string           Homepage       { get; set; } = "https://minecraft.net";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://launcher.mojang.com/download/MinecraftInstaller.msi?ref=mcnet");
}
