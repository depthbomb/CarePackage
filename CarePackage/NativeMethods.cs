using System.Runtime.InteropServices;

namespace CarePackage;

public static class NativeMethods
{
    [DllImport("dwmapi.dll")]
    private static extern int DwmSetWindowAttribute(IntPtr hWnd, int attr, ref int attrValue, int attrSize);

    [DllImport("uxtheme.dll", EntryPoint = "#135", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern int SetPreferredAppMode(int preferredAppMode);

    [DllImport("uxtheme.dll", EntryPoint = "#136", SetLastError = true, CharSet = CharSet.Unicode)]
    public static extern void FlushMenuThemes();

    public static void UseImmersiveDarkMode(IntPtr handle, bool enabled)
    {
        var useImmersiveDarkMode = enabled ? 1 : 0;
        DwmSetWindowAttribute(handle, 20, ref useImmersiveDarkMode, sizeof(int));
    }
}
