using Microsoft.Win32;
using Windows.UI.ViewManagement;

namespace CarePackage.Utils;

public enum ColorType
{
    Accent,
    AccentBackground,
    AccentForeground,
    Dark1,
    Dark2,
    Dark3,
    Light1,
    Light2,
    Light3
}

public static class Theming
{
    private static bool _accentColorsLoaded;

    private static Color _accentColorBackground;
    private static Color _accentColorForeground;
    private static Color _accentColor;
    private static Color _accentColorDark1;
    private static Color _accentColorDark2;
    private static Color _accentColorDark3;
    private static Color _accentColorLight1;
    private static Color _accentColorLight2;
    private static Color _accentColorLight3;

    public static Color GetAccentColor(ColorType type)
    {
        if (!_accentColorsLoaded)
        {
            LoadUiColors();
        }

        return type switch
        {
            ColorType.Accent           => _accentColor,
            ColorType.AccentBackground => _accentColorBackground,
            ColorType.AccentForeground => _accentColorForeground,
            ColorType.Dark1            => _accentColorDark1,
            ColorType.Dark2            => _accentColorDark2,
            ColorType.Dark3            => _accentColorDark3,
            ColorType.Light1           => _accentColorLight1,
            ColorType.Light2           => _accentColorLight2,
            ColorType.Light3           => _accentColorLight3,
            _                          => throw new ArgumentOutOfRangeException(nameof(type), type, null)
        };
    }

    public static void ApplyTheme(Form form)
    {
        ApplyThemeToControl(form);

        if (IsSystemUsingDarkMode())
        {
            if (form.IsHandleCreated)
            {
                NativeMethods.SetPreferredAppMode(2);
                NativeMethods.UseImmersiveDarkMode(form.Handle, true);
                NativeMethods.FlushMenuThemes();
            }
            else
            {
                form.HandleCreated += (_, _) =>
                {
                    NativeMethods.SetPreferredAppMode(2);
                    NativeMethods.UseImmersiveDarkMode(form.Handle, true);
                    NativeMethods.FlushMenuThemes();
                };
            }
        }

        var cornerPreference = (int)NativeMethods.DWM_WINDOW_CORNER_PREFERENCE.DWMWCP_ROUND;

        NativeMethods.DwmSetWindowAttribute(
            form.Handle,
            NativeMethods.DWMWINDOWATTRIBUTE.DWMWA_WINDOW_CORNER_PREFERENCE,
            ref cornerPreference,
            sizeof(uint)
        );
    }

    public static bool IsSystemUsingDarkMode()
    {
        try
        {
            var res = (int)(Registry.GetValue(@"HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize", "AppsUseLightTheme", -1) ?? 0);

            return res == 0;
        }
        catch
        {
            return false;
        }
    }

    private static void LoadUiColors()
    {
        var uiSettings = new UISettings();

        _accentColorBackground = uiSettings.GetColorValue(UIColorType.Background).ToDrawingColor();
        _accentColorForeground = uiSettings.GetColorValue(UIColorType.Foreground).ToDrawingColor();
        _accentColor           = uiSettings.GetColorValue(UIColorType.Accent).ToDrawingColor();
        _accentColorDark1      = uiSettings.GetColorValue(UIColorType.AccentDark1).ToDrawingColor();
        _accentColorDark2      = uiSettings.GetColorValue(UIColorType.AccentDark2).ToDrawingColor();
        _accentColorDark3      = uiSettings.GetColorValue(UIColorType.AccentDark3).ToDrawingColor();
        _accentColorLight1     = uiSettings.GetColorValue(UIColorType.AccentLight1).ToDrawingColor();
        _accentColorLight2     = uiSettings.GetColorValue(UIColorType.AccentLight2).ToDrawingColor();
        _accentColorLight3     = uiSettings.GetColorValue(UIColorType.AccentLight3).ToDrawingColor();

        _accentColorsLoaded = true;
    }

    private static void ApplyThemeToControl(Control control)
    {
        switch (control)
        {
            case LinkLabel linkLabel:
                linkLabel.LinkColor       = GetAccentColor(ColorType.Accent);
                linkLabel.ActiveLinkColor = GetAccentColor(ColorType.Dark3);
                break;
        }

        foreach (Control childControl in control.Controls)
        {
            ApplyThemeToControl(childControl);
        }
    }
}
