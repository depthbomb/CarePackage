namespace CarePackage.Software;

public class UnityHub : BaseSoftware
{
    public override string           Key            { get; set; } = "unity-hub";
    public override string           Name           { get; set; } = "Unity Hub";
    public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Creative;
    public override string           DownloadName   { get; set; } = "UnityHubSetup.exe";
    public override bool             IsArchive      { get; set; } = false;
    public override bool             ShouldCacheUrl { get; set; } = false;
    public override bool             RequiresAdmin  { get; set; } = true;
    public override Bitmap           Icon           { get; set; } = Resources.Icons.unity_hub;
    public override string           Homepage       { get; set; } = "https://unity.com";
    
    public override Task<string> GetDownloadUrlAsync(CancellationToken ct)
        => Task.FromResult("https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.exe");
}
