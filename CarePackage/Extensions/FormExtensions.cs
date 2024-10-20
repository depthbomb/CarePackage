using WinRT.Interop;
using Windows.UI.Popups;

namespace CarePackage.Extensions;

public static class FormExtensions
{
    public static async Task<int> ShowMessageDialogAsync(this Form               form,
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

        var res = await dialog.ShowAsync();

        return dialog.Commands.IndexOf(res);
    }
}
