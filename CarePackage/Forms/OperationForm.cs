using Windows.UI.Popups;
using System.Diagnostics;
using System.ComponentModel;

namespace CarePackage.Forms;

public partial class OperationForm : Form
{
    private bool _shouldClose;

    private readonly DownloadService         _downloader;
    private readonly InstallerService        _installer;
    private readonly CancellationTokenSource _cts;

    public OperationForm(DownloadService downloader, InstallerService installer)
    {
        _downloader = downloader;
        _installer  = installer;
        _cts        = new CancellationTokenSource();

        InitializeComponent();

        FormClosing += OnFormClosing;

        c_SkipInstallCheckBox.CheckedChanged       += C_SkipInstallCheckBoxOnCheckedChanged;
        c_StartOperationButton.Click               += C_StartOperationButtonOnClick;
        c_CancelOperationButton.Click              += C_CancelOperationButtonOnClick;
        c_SkipInstallCheckBox.HelpRequested        += C_SkipInstallCheckBoxOnHelpRequested;
        c_OpenDownloadFolderCheckBox.HelpRequested += C_OpenDownloadFolderCheckBoxOnHelpRequested;
        c_InstallSilentlyCheckBox.HelpRequested    += C_InstallSilentlyCheckBoxOnHelpRequested;
        c_CleanUpExecutablesCheckBox.HelpRequested += C_CleanUpExecutablesCheckBoxOnHelpRequested;

        _downloader.SoftwareDownloadUrlResolving += DownloaderOnSoftwareDownloadUrlResolving;
        _downloader.SoftwareDownloadStarted      += DownloaderOnSoftwareDownloadStarted;
        _installer.SoftwareInstallingStarted     += InstallerOnSoftwareInstallingStarted;
        _installer.SoftwareExecutableStarted     += InstallerOnSoftwareExecutableStarted;
        
        Theming.ApplyTheme(this);
    }

    #region Overrides of Form
    protected override CreateParams CreateParams
    {
        get
        {
            var cParams = base.CreateParams;
            cParams.ClassStyle |= 0x200;

            return cParams;
        }
    }
    #endregion

    #region Form Event Handlers
    private void OnFormClosing(object? sender, CancelEventArgs e) => e.Cancel = !_shouldClose;
    #endregion

    #region Control Event Handlers
    private void C_SkipInstallCheckBoxOnCheckedChanged(object? sender, EventArgs e)
    {
        if (c_SkipInstallCheckBox.Checked)
        {
            c_InstallSilentlyCheckBox.Enabled    = false;
            c_InstallSilentlyCheckBox.Checked    = false;
            c_CleanUpExecutablesCheckBox.Enabled = false;
            c_CleanUpExecutablesCheckBox.Checked = false;
        }
        else
        {
            c_InstallSilentlyCheckBox.Enabled    = true;
            c_OpenDownloadFolderCheckBox.Checked = false;
            c_CleanUpExecutablesCheckBox.Enabled = true;
        }
    }

    private async void C_StartOperationButtonOnClick(object? sender, EventArgs e)
    {
        if (_downloader.Queue.Any(s => s.IsArchive) && !c_OpenDownloadFolderCheckBox.Checked)
        {
            var res = await this.ShowMessageDialogAsync(
                "Downloading archive files",
                "One or more of the selected programs will be downloaded as compressed archives. Would you like to open the folder containing the downloaded files when everything is done downloading?",
                [
                    new UICommand("&Yes"),
                    new UICommand("&No"),
                    new UICommand("&Cancel")
                ], cancelCommandIndex: 2);

            switch (res.Label)
            {
                case "&Yes":
                    c_OpenDownloadFolderCheckBox.Checked = true;
                    break;
                case "&Cancel":
                    return;
            }
        }

        if (!Identity.IsAdministrator && _downloader.Queue.Any(s => s.RequiresAdmin) && !c_SkipInstallCheckBox.Checked)
        {
            var res = await this.ShowMessageDialogAsync(
                "Elevated permissions required",
                "One or more of the selected programs require administrator privileges to install. Would you like to restart CarePackage as administrator? If you choose not to, then the folder containing the downloaded programs will be opened after the other programs have finished installing.",
                [
                    new UICommand("&Yes"),
                    new UICommand("&No"),
                    new UICommand("&Cancel"),
                ], cancelCommandIndex: 2);

            switch (res.Label)
            {
                case "&Yes":
                    Process.Start(new ProcessStartInfo
                    {
                        FileName        = Application.ExecutablePath,
                        UseShellExecute = true,
                        Arguments       = string.Join(',', _downloader.Queue.Select(s => s.Key)),
                        Verb            = "runas"
                    });
                
                    Application.Exit();
                    return;
                case "&Cancel":
                    return;
                default:
                    c_OpenDownloadFolderCheckBox.Checked = true;
                    break;
            }
        }
        
        c_SkipInstallCheckBox.Enabled        = false;
        c_OpenDownloadFolderCheckBox.Enabled = false;
        c_InstallSilentlyCheckBox.Enabled    = false;
        c_CleanUpExecutablesCheckBox.Enabled = false;
        c_StartOperationButton.Enabled       = false;
        // c_Spinner.IsSpinning                 = true;

        var files = await _downloader.DownloadQueueAsync(_cts.Token);

        if (!c_SkipInstallCheckBox.Checked && !_cts.IsCancellationRequested)
        {
            await _installer.InstallDownloadedFilesAsync(
                files,
                c_InstallSilentlyCheckBox.Checked,
                c_CleanUpExecutablesCheckBox.Checked,
                _cts.Token
            );
        }

        if (c_OpenDownloadFolderCheckBox.Checked && !_cts.IsCancellationRequested)
        {
            await Launcher.LaunchFolderPathAsync(GlobalShared.DownloadFolder);
            
            _downloader.Queue.Clear(); // TODO always clear queue?
        }

        _shouldClose = true;
        Close();
    }

    private async void C_CancelOperationButtonOnClick(object? sender, EventArgs e)
    {
        c_StatusLabel.Text = "Aborting...";

        await _cts.CancelAsync();

        _shouldClose = true;
        Close();
    }
    
    #region Help Requests
    private async void C_SkipInstallCheckBoxOnHelpRequested(object? sender, HelpEventArgs e)
        => await this.ShowMessageDialogAsync("Skip installation", "This option will skip the installation step after all of the software has finished downloading.", []);

    private async void C_OpenDownloadFolderCheckBoxOnHelpRequested(object? sender, HelpEventArgs e)
        => await this.ShowMessageDialogAsync("Open download folder", "This option will open the folder containing the downloaded software once they have finished downloading.", []);
    
    private async void C_InstallSilentlyCheckBoxOnHelpRequested(object? sender, HelpEventArgs e)
        => await this.ShowMessageDialogAsync("Try to install silently", "This option attempts to install the selected software in the background without any interaction needed.\nThis doesn't work for every installer and may cause issues on installation.", []);
    
    private async void C_CleanUpExecutablesCheckBoxOnHelpRequested(object? sender, HelpEventArgs e)
        => await this.ShowMessageDialogAsync("Clean up installers after installation", "This option will delete a software's installer executable after the software has finished installing.\nThis option is only applicable to software that is not downloaded as a compressed archive.", []);
    #endregion
    #endregion

    #region Service Event Handlers
    private void DownloaderOnSoftwareDownloadUrlResolving(object? sender, BaseSoftware s)
        => c_StatusLabel.Text = $"Resolving URL: {s.Name}";
    
    private void DownloaderOnSoftwareDownloadStarted(object? _, BaseSoftware s)
        => c_StatusLabel.Text = $"Downloading: {s.Name}";

    private void InstallerOnSoftwareInstallingStarted(object? sender, EventArgs e)
        => c_StatusLabel.Text = "Preparing to install software...";

    private void InstallerOnSoftwareExecutableStarted(object? sender, BaseSoftware s)
        => c_StatusLabel.Text = $"Waiting: {s.Name}";
    #endregion
}
