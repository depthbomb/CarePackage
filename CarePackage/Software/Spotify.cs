namespace CarePackage.Software;

public class Spotify : BaseSoftware
{
    public override string           Key            { get; set; } = "spotify";
    public override string           Name           { get; set; } = "Spotify";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Media;
    public override string           DownloadName   { get; set; } = "SpotifySetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = false;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.spotify;
    public override string           Homepage       { get; set; } = "https://spotify.com/";

    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://download.scdn.co/SpotifySetup.exe");
}
