namespace CarePackage.Controls;

public partial class SoftwareSelectionTabs : UserControl
{
    private bool _resizing;

    private readonly SoftwareService _software;
    private readonly DownloadService _downloader;

    public SoftwareSelectionTabs(SoftwareService software, DownloadService downloader)
    {
        _software   = software;
        _downloader = downloader;
        
        InitializeComponent();

        _downloader.Queue.CollectionChanged += (_, _) => UpdateSoftwareListSelection();

        AddSoftwareControls();
    }
    
    public void UpdateSoftwareListItemWidth()
    {
        if (_resizing) return;

        _resizing = true;

        foreach (TabPage page in c_SoftwareSelectionTabs.TabPages)
        foreach (Control control in page.Controls)
        {
            if (control is SoftwareListItem listItem)
            {
                listItem.Width = page.Width - page.Padding.Horizontal;
            }
        }

        _resizing = false;
    }
    
    private void AddSoftwareControls()
    {
        foreach (var category in _software.GetCategories())
        {
            var categorySoftware = _software.GetDefinitions().Where(s => s.Category == category).ToList();

            var page = new TabPage(category.ToTitle())
            {
                AutoScroll = true,
                BackColor  = Color.White
            };

            if (categorySoftware.Count == 0)
            {
                var emptyCategory = new EmptyCategory(category);

                emptyCategory.Dock = DockStyle.Fill;
                
                page.Controls.Add(emptyCategory);
            }
            else
            {
                var controls = categorySoftware.Select(Control (software) =>
                {
                    var listItem = _software.CreateListItemControl(software);
                    listItem.Dock               =  DockStyle.Top;
                    listItem.AutoSize           =  true;
                    listItem.SoftwareSelected   += (_, s) => _downloader.Queue.Add(s);
                    listItem.SoftwareDeselected += (_, s) => _downloader.Queue.Remove(s);
                
                    return listItem;
                }).ToArray();

                page.Controls.AddRange(controls);
            }

            c_SoftwareSelectionTabs.TabPages.Add(page);
        }

        UpdateSoftwareListItemWidth();
    }
    
    private void UpdateSoftwareListSelection()
    {
        foreach (TabPage page in c_SoftwareSelectionTabs.TabPages)
        foreach (Control control in page.Controls)
        {
            if (control is SoftwareListItem listItem)
            {
                if (_downloader.Queue.Contains(listItem.Software))
                {
                    listItem.SetSelected();
                }
                else
                {
                    listItem.SetDeselected();
                }
            }
        }
    }
}
