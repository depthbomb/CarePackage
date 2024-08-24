using System.Diagnostics;

namespace CarePackage.Services;

public record SoftwareInstallationInfo
{
    public required BaseSoftware Software           { get; init; }
    public required string       ExecutableLocation { get; init; }
}

public class InstallerService
{
    public event EventHandler?               SoftwareInstallingStarted;
    public event EventHandler<BaseSoftware>? SoftwareExecutableStarted;
    public event EventHandler<BaseSoftware>? SoftwareExecutableExited;
    public event EventHandler?               SoftwareInstallingCompleted;

    public async Task InstallDownloadedFilesAsync(List<SoftwareInstallationInfo> installations,
                                                  bool                           appendSilentFlags,
                                                  bool                           cleanUpExecutables,
                                                  CancellationToken              ct = default)
    {
        SoftwareInstallingStarted?.Invoke(this, EventArgs.Empty);

        var validInstallations = installations.Where(p => p.ExecutableLocation.EndsWith(".exe") || p.ExecutableLocation.EndsWith(".msi"));
        foreach (var installation in validInstallations)
        {
            var software   = installation.Software;
            var executable = installation.ExecutableLocation;

            if (!Identity.IsAdministrator && software.RequiresAdmin)
            {
                continue;
            }

            if (!File.Exists(executable))
            {
                continue;
            }

            var argumentsList = new List<string>();

            if (appendSilentFlags)
            {
                argumentsList.AddRange([
                    "--silent",
                    "--no-interaction",
                    "--no-input",
                    "--no-user-input",
                    "--quiet",
                    "/quiet",
                    "/q",
                    "/S"
                ]);
            }

            var arguments = string.Join(' ', argumentsList);
            var psi = new ProcessStartInfo
            {
                FileName        = executable,
                Arguments       = arguments,
                UseShellExecute = true,
            };

            if (software.RequiresAdmin)
            {
                psi.Verb = "runas";
            }

            try
            {
                using (var proc = Process.Start(psi))
                {
                    SoftwareExecutableStarted?.Invoke(this, software);

                    await proc!.WaitForExitAsync(ct);

                    if (cleanUpExecutables)
                    {
                        File.Delete(executable);
                    }

                    SoftwareExecutableExited?.Invoke(this, software);
                }
            }
            catch (OperationCanceledException) { }
            catch (Exception e)
            {
                MessageBox.Show(e.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        SoftwareInstallingCompleted?.Invoke(this, EventArgs.Empty);
    }
}
