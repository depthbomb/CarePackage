using WinRT.Interop;
using Windows.UI.Popups;
using Windows.Foundation;

namespace CarePackage.Extensions;

public static class FormExtensions
{
    public static void RespectDarkMode(this Form form)
    {
        if (Personalize.IsSystemUsingDarkMode())
        {
            NativeMethods.SetPreferredAppMode(2);
            NativeMethods.UseImmersiveDarkMode(form.Handle, true);
            NativeMethods.FlushMenuThemes();
        }
    }

    public static IAsyncOperation<IUICommand> ShowMessageDialogAsync(this Form               form,
                                                                     string                  title,
                                                                     string                  content,
                                                                     IEnumerable<IUICommand> commands,
                                                                     uint                    defaultCommandIndex = 0,
                                                                     uint                    cancelCommandIndex  = 0)
    {
        var dialog = new MessageDialog(content, title);

        foreach (var command in commands)
        {
            dialog.Commands.Add(command);
        }
        
        dialog.DefaultCommandIndex = defaultCommandIndex;
        dialog.CancelCommandIndex  = cancelCommandIndex;

        InitializeWithWindow.Initialize(dialog, form.Handle);

        return dialog.ShowAsync();
    }
}
