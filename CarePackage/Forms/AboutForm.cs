using Windows.System;
using System.Reflection;

namespace CarePackage.Forms;

public partial class AboutForm : Form
{
    public AboutForm()
    {
        InitializeComponent();
        
        c_VersionLabel.Text               =  Assembly.GetExecutingAssembly().GetName().Version!.ToString();
        c_GithubLinkLabel.LinkColor       =  Personalize.GetAccentColor(ColorType.Accent);
        c_GithubLinkLabel.ActiveLinkColor =  Personalize.GetAccentColor(ColorType.Dark3);
        c_GithubLinkLabel.Click           += C_GithubLinkLabelOnClick;
        
        this.RespectDarkMode();
    }

    private async void C_GithubLinkLabelOnClick(object? sender, EventArgs e)
        => await Launcher.LaunchUriAsync(new Uri(GlobalShared.RepositoryLink));
}
