namespace CarePackage.Software;

public class MinecraftLauncher : BaseSoftware
{
    public override string           Key            { get; set; } = "minecraft-launcher";
    public override string           Name           { get; set; } = "Minecraft Launcher";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Gaming;
    public override string           DownloadName   { get; set; } = "MinecraftInstaller.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.minecraft_launcher;
    public override string           Homepage       { get; set; } = "https://minecraft.net";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://launcher.mojang.com/download/MinecraftInstaller.exe?ref=mcnet");
}
