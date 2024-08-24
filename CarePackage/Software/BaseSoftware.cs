namespace CarePackage.Software;

public enum SoftwareCategory
{
    Browser,
    Gaming,
    Social,
    Media,
    Utility,
    Runtime,
    Peripheral,
    Development,
    Creative,
    Security,
}

public abstract class BaseSoftware
{
    /// <summary>
    ///     The key of this software. Should be all lowercase and not contain any spaces.
    /// </summary>
    public abstract string Key { get; set; }

    /// <summary>
    ///     The proper name of this software.
    /// </summary>
    public abstract string Name { get; set; }

    /// <summary>
    ///     The category that this software belongs to.
    /// </summary>
    public abstract SoftwareCategory Category { get; set; }

    /// <summary>
    ///     The name of the downloaded file.
    /// </summary>
    public abstract string DownloadName { get; set; }

    /// <summary>
    ///     Whether the download for this software is an archive rather than a binary.
    /// </summary>
    public abstract bool IsArchive { get; set; }

    /// <summary>
    ///     Whether to cache the download URL after it is fetched for the first time.
    /// </summary>
    public abstract bool ShouldCacheUrl { get; set; }

    /// <summary>
    ///     Whether the downloaded executable must be run with elevated privileges.
    /// </summary>
    public abstract bool RequiresAdmin { get; set; }

    /// <summary>
    ///     The icon of the software that is displayed in the UI.
    /// </summary>
    public abstract Bitmap Icon { get; set; }

    /// <summary>
    ///     The home page of this software.
    /// </summary>
    public abstract string Homepage { get; set; }

    /// <summary>
    ///     Resolves to the direct download URL of this software.
    /// </summary>
    public abstract Task<string> GetDownloadUrlAsync(CancellationToken ct);
}
