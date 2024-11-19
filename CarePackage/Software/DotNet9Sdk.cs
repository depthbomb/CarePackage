namespace CarePackage.Software;

public class DotNet9Sdk : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-9-sdk";
    public override string           Name           { get; set; } = ".NET 9.0 SDK";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "dotnet-sdk-9.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/10bb041d-e705-473e-9654-27c0e038f5bd/447c0c10654c2949872fa6154b8c27b5/dotnet-sdk-9.0.100-win-x64.exe");
}
