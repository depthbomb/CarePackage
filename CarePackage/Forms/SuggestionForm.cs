namespace CarePackage.Forms;

public partial class SuggestionForm : Form
{
    public SuggestionForm()
    {
        InitializeComponent();
        
        foreach (var category in Enum.GetValues<SoftwareCategory>())
        {
            c_CategorySelectionComboBox.Items.Add(category);
        }
        
        c_CategorySelectionComboBox.SelectedIndexChanged += C_CategorySelectionComboBoxOnSelectedIndexChanged;
        c_LaunchUrlButton.Click                          += C_LaunchUrlButtonOnClick;
        
        Theming.ApplyTheme(this);
    }

    private void C_CategorySelectionComboBoxOnSelectedIndexChanged(object? sender, EventArgs e)
    {
        c_LaunchUrlButton.Enabled = c_CategorySelectionComboBox.SelectedItem is not null;
    }

    private async void C_LaunchUrlButtonOnClick(object? sender, EventArgs e)
    {
        if (c_CategorySelectionComboBox.SelectedItem is SoftwareCategory category)
        {
            c_LaunchUrlButton.Enabled = false;
            
            var url = string.Format(GlobalShared.SoftwareSuggestionLink, category.ToTitle());
            await Launcher.LaunchUriAsync(new Uri(url));
            
            Close();
        }
    }
}
