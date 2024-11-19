namespace CarePackage.Software;

public class DotNet9Runtime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-9-runtime";
    public override string           Name           { get; set; } = ".NET 9.0 Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "dotnet-runtime-9.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/99bd07c2-c95c-44dc-9d47-36d3b18df240/bdf26c62f69c1b783687c1dce83ccf7a/dotnet-runtime-9.0.0-win-x64.exe");
}
