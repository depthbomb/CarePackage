namespace CarePackage.Software;

public class DotNet8Sdk : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-8-sdk";
    public override string           Name           { get; set; } = ".NET 8.0 SDK";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Development;
    public override string           DownloadName   { get; set; } = "dotnet-sdk-8.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/ba3a1364-27d8-472e-a33b-5ce0937728aa/6f9495e5a587406c85af6f93b1c89295/dotnet-sdk-8.0.404-win-x64.exe");
}
