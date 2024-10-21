using CarePackage.Forms;

namespace CarePackage;

internal static class Program
{
    [STAThread]
    private static async Task Main(string[] args)
    {
        ArgParser.AddArg("debug", "d", false);
        ArgParser.AddArg("software", "s", new List<string>());
        ArgParser.ParseArgs(args);
        
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
                                                              .BuildServiceProvider();
}
