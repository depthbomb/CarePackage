using CarePackage.Forms;
using CarePackage.Controls;

namespace CarePackage.Extensions;

public static class ServiceCollectionExtensions
{
    public static IServiceCollection AddServices(this IServiceCollection services)
        => services.AddSingleton<GitHubService>()
                   .AddSingleton<SoftwareService>()
                   .AddSingleton<DownloadService>()
                   .AddSingleton<InstallerService>()
                   .AddSingleton<MaintenanceService>();

    public static IServiceCollection AddControls(this IServiceCollection services)
        => services.AddSingleton<SoftwareSelectionTabs>();

    public static IServiceCollection AddHttpClients(this IServiceCollection services)
    {
        var defaultHttp = new HttpClient();
            defaultHttp.DefaultRequestHeaders.Add("User-Agent", GlobalShared.UserAgent);
        services.AddKeyedSingleton("Default", defaultHttp);
        
        var mimicBrowserHttp = new HttpClient();
            mimicBrowserHttp.DefaultRequestHeaders.Add("User-Agent", GlobalShared.BrowserUserAgent);
        services.AddKeyedSingleton("MimicBrowser", mimicBrowserHttp);
        
        var wgetHttp = new HttpClient();
            wgetHttp.DefaultRequestHeaders.Add("User-Agent", "Wget/1.21.4");
        services.AddKeyedSingleton("Wget", wgetHttp);
        
        return services;
    }

    public static IServiceCollection AddForms(this IServiceCollection services) => services.AddTransient<MainForm>();
}
