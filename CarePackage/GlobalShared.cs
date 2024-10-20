﻿namespace CarePackage;

public static class GlobalShared
{
    public const string UserAgent        = "CarePackage (depthbomb/carepackage)";
    public const string BrowserUserAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36";

    #if DEBUG
    public const string LatestReleasePermalink = "https://github.com/depthbomb/CarePackage/releases/latest";
    public const string RepositoryLink         = "https://github.com/depthbomb/CarePackage";
    #else
    public const string LatestReleasePermalink = "https://bit.ly/get-carepackage";
    public const string RepositoryLink         = "https://bit.ly/carepackage-repo";
    #endif
    public const string SoftwareSuggestionLink = "https://github.com/depthbomb/CarePackage/issues/new?title=[{0}] PROGRAM NAME";

    public static readonly string DownloadFolder = Path.Combine(Path.GetTempPath(), ".carepackage");
    public static readonly string DataFolder 
        = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.LocalApplicationData), "Caprine Logic", "CarePackage");
}
