namespace CarePackage.Software;

public class MozillaFirefox : BaseSoftware
{
    public override string           Key            { get; set; } = "mozilla-firefox";
    public override string           Name           { get; set; } = "Mozilla Firefox";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Browser;
    public override string           DownloadName   { get; set; } = "Firefox Installer.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.mozilla_firefox;
    public override string           Homepage       { get; set; } = "https://mozilla.org/firefox";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US");
}
