namespace CarePackage.Software;

public class DotNet8Runtime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-8-runtime";
    public override string           Name           { get; set; } = ".NET 8.0 Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "dotnet-runtime-8.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/53e9e41c-b362-4598-9985-45f989518016/53c5e1919ba2fe23273f2abaff65595b/dotnet-runtime-8.0.11-win-x64.exe");
}
