namespace CarePackage.Software;

public class VisualStudioCode : BaseSoftware
{
    public override string           Key            { get; set; } = "visual-studio-code";
    public override string           Name           { get; set; } = "Visual Studio Code";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "VSCodeUserSetup-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = true;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.visual_studio_code;
    public override string           Homepage       { get; set; } = "https://code.visualstudio.com";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user");
}
