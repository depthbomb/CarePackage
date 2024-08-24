namespace CarePackage.Software;

public class WebView2Runtime : BaseSoftware
{
    public override string           Key            { get; set; } = "webview2-runtime";
    public override string           Name           { get; set; } = "Microsoft Edge WebView2 Runtime";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Runtime;
    public override string           DownloadName   { get; set; } = "MicrosoftEdgeWebview2Setup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.microsoft_edge_webview2_runtime;
    public override string           Homepage       { get; set; } = "https://developer.microsoft.com/en-us/microsoft-edge/webview2";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://go.microsoft.com/fwlink/p/?LinkId=2124703");
}
