using CarePackage.Controls;

namespace CarePackage.Forms;

public partial class MainForm : Form
{
    private bool _doCleanup = true;

    private readonly DownloadService    _downloader;
    private readonly InstallerService   _installer;
    private readonly MaintenanceService _maintenance;
    private readonly bool               _debug;

    public MainForm(SoftwareService       software,
                    DownloadService       downloader,
                    InstallerService      installer,
                    MaintenanceService    maintenance,
                    SoftwareSelectionTabs softwareSelectionControl)
    {
        _downloader  = downloader;
        _installer   = installer;
        _maintenance = maintenance;
        _debug       = ArgParser.GetArg<bool>("debug");

        InitializeComponent();

        if (Identity.IsAdministrator)
        {
            // ReSharper disable VirtualMemberCallInConstructor
            Text = $"[Administrator] {Text}";
            // ReSharper restore VirtualMemberCallInConstructor
        }

        c_HeadingLabel.ForeColor = Theming.GetAccentColor(ColorType.Dark3);

        c_SoftwareSelectionSlotPanel.Controls.Add(softwareSelectionControl);

        if (!_debug)
        {
            c_Debug_SelectAllButton.Dispose();
        }

        Load        += OnLoad;
        FormClosing += OnFormClosing;

        c_PrepareOperationButton.Click += C_StartOperationButtonOnClick;
        c_ClearSelectionButton.Click   += C_ClearSelectionButtonOnClick;
        c_LatestReleaseLinkLabel.Click += C_LatestReleaseLinkLabelOnClick;
        c_SuggestionLinkLabel.Click    += C_SuggestionLinkLabelOnClick;
        c_AboutLinkLabel.Click         += C_AboutLinkLabelOnClick;
        if (_debug)
        {
            c_Debug_SelectAllButton.Click += (_, _) =>
            {
                foreach (var sw in software.GetDefinitions())
                {
                    _downloader.Queue.Add(sw);
                }
            };
        }

        _downloader.Queue.CollectionChanged += (_, _) =>
        {
            var hasSelection = _downloader.Queue.Any();
            c_PrepareOperationButton.Enabled = hasSelection;
            c_ClearSelectionButton.Enabled   = hasSelection;
        };
        _installer.SoftwareInstallingCompleted += (_, _) => _downloader.Queue.Clear();

        // Iterate through the launch arguments and try to pre-select software
        var softwareFromArgs = ArgParser.GetArg<List<string>>("software");
        if (softwareFromArgs.Count > 0)
        {
            var definitions = software.GetDefinitions();
            foreach (var softwareKey in softwareFromArgs)
            {
                var sw = definitions.FirstOrDefault(d => d.Key == softwareKey);
                if (sw != null)
                {
                    _downloader.Queue.Add(sw);
                }
            }
        }

        Theming.ApplyTheme(this);
    }

    private async void OnLoad(object? sender, EventArgs e)
    {
        await _maintenance.ShowDisclaimerIfRequiredAsync(Handle);

        c_LatestReleaseLinkLabel.Visible = await _maintenance.IsUpdateAvailableAsync();
    }

    private async void OnFormClosing(object? sender, FormClosingEventArgs e)
    {
        if (_doCleanup)
        {
            e.Cancel = true;

            Hide(); // Hide the form while we clean up or else it waits until all files are deleted before closing

            await _maintenance.CleanUpDownloadFolderAsync();

            _doCleanup = false;

            Close();
        }
    }

    private void C_StartOperationButtonOnClick(object? sender, EventArgs e)
    {
        c_PrepareOperationButton.Enabled = false;

        new OperationForm(_downloader, _installer).ShowDialog(this);

        c_PrepareOperationButton.Enabled = true;
    }

    private void C_ClearSelectionButtonOnClick(object? sender, EventArgs e) => _downloader.Queue.Clear();

    private void C_SuggestionLinkLabelOnClick(object? sender, EventArgs e) => new SuggestionForm().ShowDialog(this);

    private async void C_LatestReleaseLinkLabelOnClick(object? sender, EventArgs e)
        => await Launcher.LaunchUriAsync(new Uri(GlobalShared.LatestReleasePermalink));

    private void C_AboutLinkLabelOnClick(object? sender, EventArgs e) => new AboutForm().ShowDialog(this);
}
