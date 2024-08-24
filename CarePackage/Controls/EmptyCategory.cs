using Windows.System;

namespace CarePackage.Controls;

public partial class EmptyCategory : UserControl
{
    private readonly SoftwareCategory _category;
    private readonly Uri              _suggestionUrl = new("https://github.com/depthbomb/carepackage");

    public EmptyCategory(SoftwareCategory category)
    {
        _category = category;

        InitializeComponent();

        c_Subheading.LinkClicked += async (_, _) => await Launcher.LaunchUriAsync(_suggestionUrl);
    }
}
