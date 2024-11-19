﻿namespace CarePackage.Software;

public class DotNet9AspNetCoreRuntime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-9-aspnet-core-runtime";
    public override string           Name           { get; set; } = ".NET 9.0 ASP.NET Core Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "aspnetcore-runtime-9.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/815e6104-b92c-4cd5-8971-cba2f685002a/37befaa217f3269a152016da80a922c1/aspnetcore-runtime-9.0.0-win-x64.exe");
}