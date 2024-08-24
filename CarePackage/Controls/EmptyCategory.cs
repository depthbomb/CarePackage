namespace CarePackage.Controls;

public partial class EmptyCategory : UserControl
{
    private readonly SoftwareCategory _category;

    public EmptyCategory(SoftwareCategory category)
    {
        _category = category;

        InitializeComponent();

        c_Subheading.LinkClicked += C_SubheadingOnLinkClicked;
    }

    private async void C_SubheadingOnLinkClicked(object? sender, LinkLabelLinkClickedEventArgs e)
    {
        var url = string.Format(GlobalShared.SoftwareSuggestionLink, _category.ToTitle());
        
        await Launcher.LaunchUriAsync(new Uri(url));
    }
}
