using Windows.Storage;
using System.Text.Json;
using CarePackage.Models;

namespace CarePackage.Services;

public class SettingsService
{
    private Settings _settings;

    public SettingsService()
    {
        _settings = new Settings();
    }

    public T Get<T>(Func<Settings, T> selector) => selector(_settings);

    public void Set(Func<Settings, Settings> update)
    {
        _settings = update(_settings);
    }

    public async Task CommitAsync()
    {
        var folder = await GetStorageFolderAsync();
        var file   = await folder.CreateFileAsync("Settings", CreationCollisionOption.ReplaceExisting);

        await using var fs = await file.OpenStreamForWriteAsync();
        await JsonSerializer.SerializeAsync(fs, _settings);
    }

    public async Task LoadAsync()
    {
        try
        {
            var folder = await GetStorageFolderAsync();
            var file   = await folder.GetFileAsync("Settings");
            if (file.IsAvailable)
            {
                await using var sr       = await file.OpenStreamForReadAsync();
                var             settings = await JsonSerializer.DeserializeAsync<Settings>(sr);

                if (settings != null)
                {
                    _settings = settings;
                }
            }
        }
        catch (FileNotFoundException)
        {
            //
        }
    }

    private async Task<StorageFolder> GetStorageFolderAsync()
        => await StorageFolder.GetFolderFromPathAsync(GlobalShared.DataFolder);
}
