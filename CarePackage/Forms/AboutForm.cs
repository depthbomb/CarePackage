using System.Reflection;

namespace CarePackage.Forms;

public partial class AboutForm : Form
{
    public AboutForm()
    {
        InitializeComponent();

        c_VersionLabel.Text     =  Assembly.GetExecutingAssembly().GetName().Version!.ToString();
        c_GithubLinkLabel.Click += C_GithubLinkLabelOnClick;
        
        Theming.ApplyTheme(this);
    }

    private async void C_GithubLinkLabelOnClick(object? sender, EventArgs e)
        => await Launcher.LaunchUriAsync(new Uri(GlobalShared.RepositoryLink));
}
