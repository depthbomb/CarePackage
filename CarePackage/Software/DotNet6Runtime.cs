namespace CarePackage.Software;

public class DotNet6Runtime : BaseSoftware
{
    public override string           Key            { get; set; } = "dotnet-6-runtime";
    public override string           Name           { get; set; } = ".NET 6.0 Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "dotnet-runtime-6.0-win-x64.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.dotnet;
    public override string           Homepage       { get; set; } = "https://dot.net";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.visualstudio.microsoft.com/download/pr/1a5fc50a-9222-4f33-8f73-3c78485a55c7/1cb55899b68fcb9d98d206ba56f28b66/dotnet-runtime-6.0.36-win-x64.exe");
}
