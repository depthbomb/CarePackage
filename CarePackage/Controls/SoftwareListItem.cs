using CarePackage.Renderers;

namespace CarePackage.Controls;

public partial class SoftwareListItem : UserControl
{
    public readonly BaseSoftware Software;

    public event EventHandler<BaseSoftware>? SoftwareSelected;
    public event EventHandler<BaseSoftware>? SoftwareDeselected;

    private bool _hovered;
    private bool _selected;

    private readonly Bitmap           _activeIcon;
    private readonly Bitmap           _inactiveIcon;
    private readonly Color            _foreColor;
    private readonly Color            _backColor;
    private readonly ContextMenuStrip _menu;

    public SoftwareListItem(BaseSoftware software)
    {
        Software = software;

        _activeIcon   = software.Icon;
        _inactiveIcon = software.Icon.ToGrayScale();
        _backColor    = Theming.GetAccentColor(ColorType.Light3);
        _foreColor    = Theming.GetAccentColor(ColorType.Dark3);
        _menu = new ContextMenuStrip
        {
            ShowImageMargin   = false,
            DropShadowEnabled = true,
            Items             = { "Homepage" }
        };
        _menu.ItemClicked += ContextMenuOnItemClicked;
        _menu.ForeColor   =  _foreColor;
        _menu.Renderer    =  new AccentedContextMenuStripRenderer();

        InitializeComponent();

        SubscribeToClickEvent(this);
        SubscribeToMouseEnterOrLeaveEvents(this);

        Height               = 64;
        c_SoftwareIcon.Image = _inactiveIcon;
        c_SoftwareIcon.Top   = (Height - c_SoftwareIcon.Height) / 2;
        c_SoftwareName.Text  = Software.Name;
        c_SoftwareName.Top   = (Height - c_SoftwareName.Height) / 2;
    }

    public void SetSelected()
    {
        _selected                = true;
        BackColor                = _backColor;
        c_SoftwareIcon.Image     = _activeIcon;
        c_SoftwareName.ForeColor = _foreColor;
    }

    public void SetDeselected()
    {
        _selected                = false;
        BackColor                = Color.Transparent;
        c_SoftwareIcon.Image     = _hovered ? _activeIcon : _inactiveIcon;
        c_SoftwareName.ForeColor = _hovered ? Color.Black : Color.DimGray;
    }

    #region Event Handlers
    private void OnClick(object? sender, EventArgs e)
    {
        var mouseEvent = (MouseEventArgs)e;
        if (mouseEvent.Button == MouseButtons.Left)
        {
            if (_selected)
            {
                SoftwareDeselected?.Invoke(this, Software);
            }
            else
            {
                SoftwareSelected?.Invoke(this, Software);
            }
        }
        else
        {
            _menu.Show(this, mouseEvent.Location);
        }
    }

    private void OnMouseEnter(object? sender, EventArgs e)
    {
        _hovered = true;

        if (!_selected)
        {
            c_SoftwareIcon.Image     = _activeIcon;
            c_SoftwareName.ForeColor = Color.Black;
        }
    }

    private void OnMouseLeave(object? sender, EventArgs e)
    {
        _hovered = false;

        if (!_selected)
        {
            c_SoftwareIcon.Image     = _inactiveIcon;
            c_SoftwareName.ForeColor = Color.DimGray;
        }
    }
    
    private async void ContextMenuOnItemClicked(object? sender, ToolStripItemClickedEventArgs e)
    {
        switch (e.ClickedItem?.Text)
        {
            case "Homepage":
                await Launcher.LaunchUriAsync(new Uri(Software.Homepage));
                break;
        }
    }
    #endregion

    private void SubscribeToClickEvent(Control control)
    {
        control.Click += OnClick;

        foreach (Control childControl in control.Controls)
        {
            SubscribeToClickEvent(childControl);
        }
    }

    private void SubscribeToMouseEnterOrLeaveEvents(Control control)
    {
        control.MouseEnter += OnMouseEnter;
        control.MouseLeave += OnMouseLeave;

        foreach (Control childControl in control.Controls)
        {
            SubscribeToMouseEnterOrLeaveEvents(childControl);
        }
    }
}
