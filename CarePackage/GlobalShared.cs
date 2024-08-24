namespace CarePackage;

public static class GlobalShared
{
    public const string UserAgent        = "CarePackage (depthbomb/carepackage)";
    public const string BrowserUserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36";

    #if DEBUG
    public const string LatestReleasePermalink = "https://github.com/depthbomb/CarePackage/releases/latest";
    #else
    public const string LatestReleasePermalink = "https://bit.ly/get-carepackage";
    #endif

    public static readonly string DownloadFolder = Path.Combine(Path.GetTempPath(), ".carepackage");
    public static readonly string DataFolder 
        = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Caprine Logic", "CarePackage");
}
