using CarePackage.Forms;

namespace CarePackage;

internal static class Program
{
    private static string[] _args = [];
    
    [STAThread]
    private static async Task Main(string[] args)
    {
        _args = args;
        
        var services    = CreateServiceProvider();
        var maintenance = services.GetRequiredService<MaintenanceService>();

        await maintenance.EnsureFoldersAsync();
        
        ApplicationConfiguration.Initialize();
        #pragma warning disable WFO5001
        Application.SetColorMode(SystemColorMode.Classic);
        #pragma warning restore WFO5001
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
