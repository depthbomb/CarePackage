using System.Runtime.InteropServices;

namespace CarePackage;

// ReSharper disable InconsistentNaming
public static class NativeMethods
{
    public enum DWMWINDOWATTRIBUTE
    {
        DWMWA_USE_IMMERSIVE_DARK_MODE  = 20,
        DWMWA_WINDOW_CORNER_PREFERENCE = 33
    }

    public enum DWM_WINDOW_CORNER_PREFERENCE
    {
        DWMWCP_DEFAULT    = 0,
        DWMWCP_DONOTROUND = 1,
        DWMWCP_ROUND      = 2,
        DWMWCP_ROUNDSMALL = 3
    }

    [DllImport("dwmapi.dll")]
    public static extern int DwmSetWindowAttribute(IntPtr             hwnd,
                                                   DWMWINDOWATTRIBUTE attribute,
                                                   ref int            pvAttribute,
                                                   int                cbAttribute);

    [DllImport("uxtheme.dll", EntryPoint = "#135", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern int SetPreferredAppMode(int preferredAppMode);

    [DllImport("uxtheme.dll", EntryPoint = "#136", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern void FlushMenuThemes();

    public static void UseImmersiveDarkMode(IntPtr handle, bool enabled)
    {
        var useImmersiveDarkMode = enabled ? 1 : 0;
        DwmSetWindowAttribute(handle, DWMWINDOWATTRIBUTE.DWMWA_USE_IMMERSIVE_DARK_MODE, ref useImmersiveDarkMode, sizeof(uint));
    }
}
