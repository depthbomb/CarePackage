using System.Reflection;

namespace CarePackage.Forms;

public partial class AboutForm : Form
{
    public AboutForm()
    {
        InitializeComponent();
        
        c_VersionLabel.Text = Assembly.GetExecutingAssembly().GetName().Version!.ToString();
        
        this.RespectDarkMode();
    }
}
