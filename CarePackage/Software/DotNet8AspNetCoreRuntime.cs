namespace CarePackage.Software;

public class DotNet8AspNetCoreRuntime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-8-aspnet-core-runtime";
    public override string           Name           { get; set; } = ".NET 8.0 ASP.NET Core Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "aspnetcore-runtime-8.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/8d6c1aaa-7d58-455a-acec-aab350860582/ab5f7c23dc72516e77065fcaf99ad444/aspnetcore-runtime-8.0.11-win-x64.exe");
}
