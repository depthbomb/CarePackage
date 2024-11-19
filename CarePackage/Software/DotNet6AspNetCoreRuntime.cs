namespace CarePackage.Software;

public class DotNet6AspNetCoreRuntime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-6-aspnet-core-runtime";
    public override string           Name           { get; set; } = ".NET 6.0 ASP.NET Core Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "aspnetcore-runtime-6.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/0f0ea01c-ef7c-4493-8960-d1e9269b718b/3f95c5bd383be65c2c3384e9fa984078/aspnetcore-runtime-6.0.36-win-x64.exe");
}
