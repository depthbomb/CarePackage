namespace CarePackage.Services;

public class GitHubService
{
    private readonly HttpClient _http;
    private readonly Regex      _releaseHrefPattern;

    public GitHubService([FromKeyedServices("MimicBrowser")] HttpClient http)
    {
        _http               = http;
        _releaseHrefPattern = new Regex(@"href=""(.*)"" rel=""nofollow""", RegexOptions.Compiled);
    }

    public async Task<List<string>> GetLatestRepositoryReleaseAssetsAsync(string            owner,
                                                                          string            repo,
                                                                          CancellationToken ct = default)
    {
        var initialRes = await _http.GetAsync(
            $"https://github.com/{owner}/{repo}/releases/latest",
            HttpCompletionOption.ResponseHeadersRead,
            ct
        );

        initialRes.EnsureSuccessStatusCode();

        var latestVersion = initialRes.RequestMessage!.RequestUri!.Segments.Last();
        var assetsUrl     = $"https://github.com/{owner}/{repo}/releases/expanded_assets/{latestVersion}";
        var assetsRes     = await _http.GetAsync(assetsUrl, ct);

        assetsRes.EnsureSuccessStatusCode();

        var html    = await assetsRes.Content.ReadAsStringAsync(ct);
        var matches = _releaseHrefPattern.Matches(html);

        return matches.Select(m => $"https://github.com{m.Groups[1].Value}").ToList();
    }
}
