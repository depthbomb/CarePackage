// namespace CarePackage.Software;
//
// public class EqualizerApo : BaseSoftware
// {
//     public override string           Key            { get; set; } = "equalizer-apo";
//     public override string           Name           { get; set; } = "Equalizer APO";
//     public override SoftwareCategory Category       { get; set; } = SoftwareCategory.Utility;
//     public override string           DownloadName   { get; set; } = "EqualizerAPO64.exe";
//     public override bool             IsArchive      { get; set; } = false;
//     public override bool             ShouldCacheUrl { get; set; } = false;
//     public override bool             RequiresAdmin  { get; set; } = true;
//     public override Bitmap           Icon           { get; set; } = Resources.Icons.generic;
//     public override string           Homepage       { get; set; } = "https://sourceforge.net/projects/equalizerapo";
//     
//     private readonly HttpClient _http;
//     private readonly HtmlParser _htmlParser;
//
//     public EqualizerApo(IServiceProvider services)
//     {
//         _http       = services.GetKeyedService<HttpClient>("MimicBrowser")!;
//         _htmlParser = new HtmlParser();
//     }
//
//     public override async Task<string> GetDownloadUrlAsync(CancellationToken ct)
//     {
//         var version = await GetLatestVersionStringAsync();
//         var url     = $"https://sourceforge.net/settings/mirror_choices?projectname=equalizerapo&filename={version}/EqualizerAPO64-{version}.exe&selected=master&dialog=true";
//         var res     = await _http.GetAsync(url, ct);
//
//         res.EnsureSuccessStatusCode();
//
//         var html = await res.Content.ReadAsStringAsync(ct);
//         using (var document = await _htmlParser.ParseDocumentAsync(html))
//         {
//             var downloadAnchorTag = document.QuerySelector("div.section-problems p a");
//             var downloadLink      = downloadAnchorTag?.GetAttribute("href");
//             if (downloadLink == null)
//             {
//                 throw new Exception("Failed to retrieve download URL");
//             }
//             
//             return downloadLink;
//         }
//     }
//
//     private async Task<string?> GetLatestVersionStringAsync()
//     {
//         var res = await _http.GetAsync("https://sourceforge.net/projects/equalizerapo/files/");
//
//         res.EnsureSuccessStatusCode();
//
//         var html = await res.Content.ReadAsStringAsync();
//         using (var document = await _htmlParser.ParseDocumentAsync(html))
//         {
//             var filesTbody = document.QuerySelector("table#files_list > tbody");
//             var firstRow   = filesTbody?.QuerySelectorAll("tr.folder").FirstOrDefault();
//
//             return firstRow?.GetAttribute("title");
//         }
//     }
// }
