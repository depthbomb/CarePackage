namespace CarePackage.Software;

public class DotNet6Sdk : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-6-sdk";
    public override string           Name           { get; set; } = ".NET 6.0 SDK";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "dotnet-sdk-6.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/396abf58-60df-4892-b086-9ed9c7a914ba/eb344c08fa7fc303f46d6905a0cb4ea3/dotnet-sdk-6.0.428-win-x64.exe");
}
