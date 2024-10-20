using CarePackage.Forms;

namespace CarePackage;

internal static class Program
{
    private static string[] _args = [];
    
    [STAThread]
    private static async Task Main(string[] args)
    {
        _args = args;
        
        var services = CreateServiceProvider();

        await services.GetRequiredService<MaintenanceService>().EnsureFoldersAsync();
        await services.GetRequiredService<SettingsService>().LoadAsync();

        ApplicationConfiguration.Initialize();
        Application.Run(services.GetRequiredService<MainForm>());
    }

    private static ServiceProvider CreateServiceProvider() => new ServiceCollection()
                                                              .AddServices()
                                                              .AddControls()
                                                              .AddHttpClients()
                                                              .AddForms()
                                                              .AddSingleton(_args)
                                                              .BuildServiceProvider();
}
