namespace CarePackage.Software;

public class DotNet6DesktopRuntime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-6-desktop-runtime";
    public override string           Name           { get; set; } = ".NET 6.0 Desktop Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "windowsdesktop-runtime-6.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/3ebc1f91-a5ba-477e-9353-198fa4e13371/35f447d6820b078fd18523764a4f0213/windowsdesktop-runtime-6.0.33-win-x64.exe");
}
