namespace CarePackage.Forms;

public partial class SoftwareInfoForm : Form
{
    private readonly BaseSoftware _software;

    public SoftwareInfoForm(BaseSoftware software)
    {
        _software = software;

        InitializeComponent();

        C_KeyValue.Text                    =  _software.Key;
        C_NameValue.Text                   =  _software.Name;
        C_CategoryValue.Text               =  $"{_software.Category.ToTitle()} ({_software.Category})";
        C_DownloadNameValue.Text           =  _software.DownloadName;
        C_IsArchiveValue.Text              =  _software.IsArchive ? "Yes" : "No";
        C_ShouldCacheDownloadUrlValue.Text =  _software.ShouldCacheUrl ? "Yes" : "No";
        C_RequiresAdminValue.Text          =  _software.RequiresAdmin ? "Yes" : "No";
        C_IconPictureBox.Image             =  _software.Icon;
        C_IconPictureBoxGrayscale.Image    =  _software.Icon.ToGrayScale();
        C_HomepageLinkLabel.Text           =  _software.Homepage;
        C_HomepageLinkLabel.LinkClicked    += C_HomepageLinkLabelOnLinkClicked;

        Theming.ApplyTheme(this);
    }

    private async void C_HomepageLinkLabelOnLinkClicked(object? sender, LinkLabelLinkClickedEventArgs e)
        => await Launcher.LaunchUriAsync(new Uri(_software.Homepage));
}
