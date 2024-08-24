namespace CarePackage.Extensions;

public static class SoftwareCategoryExtensions
{
    public static string ToTitle(this SoftwareCategory cat)
    {
        return cat switch
        {
            SoftwareCategory.Browser     => "Web Browsers",
            SoftwareCategory.Gaming      => "Gaming",
            SoftwareCategory.Social      => "Social",
            SoftwareCategory.Media       => "Media",
            SoftwareCategory.Utility     => "Utilities",
            SoftwareCategory.Runtime     => "Runtimes",
            SoftwareCategory.Peripheral  => "Peripheral",
            SoftwareCategory.Development => "Developer Tools",
            SoftwareCategory.Creative    => "Creative Tools",
            SoftwareCategory.Security    => "Security",
            _                            => throw new ArgumentOutOfRangeException(nameof(cat), cat, null)
        };
    }
}
