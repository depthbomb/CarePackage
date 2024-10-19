using System.Drawing.Text;
using System.ComponentModel;

namespace CarePackage.Controls;

public enum SpinnerStyle
{
    Dots,
    Line
}

public sealed class Spinner : Label
{
    public event EventHandler? IsSpinningChanged;

    /// <summary>
    ///     Whether the spinning animation is playing.
    /// </summary>
    [DesignerSerializationVisibility(DesignerSerializationVisibility.Visible)]
    [Bindable(true)]
    [Browsable(true)]
    public bool IsSpinning
    {
        get => _isSpinning;
        set
        {
            if (_isSpinning == value)
            {
                return;
            }

            _isSpinning = value;

            OnIsSpinningChanged(EventArgs.Empty);
        }
    }

    [DesignerSerializationVisibility(DesignerSerializationVisibility.Visible)]
    [Bindable(true)]
    [Browsable(true)]
    public SpinnerStyle SpinnerStyle { get; set; } = SpinnerStyle.Line;

    private bool                     _isSpinning;
    private CancellationTokenSource? _cts;

    private const string BootFontPath = "Boot\\Fonts_EX";
    private const string FontFileName = "segoe_slboot_EX.ttf";

    private readonly PrivateFontCollection _pfc;
    private readonly char[]                _dotStyleParts  = CharSequence(0xE052..0xE0CB);
    private readonly char[]                _lineStyleParts = CharSequence(0xE100..0xE176);

    public Spinner()
    {
        DoubleBuffered = true;
        Text           = "";
        AutoSize       = false;
        TextAlign      = ContentAlignment.MiddleCenter;

        _isSpinning = false;

        _pfc = new PrivateFontCollection();

        LoadBootFont();

        var form = FindForm();
        if (form != null)
        {
            form.FormClosing += OnFormClosing;
        }
    }

    private void OnFormClosing(object? sender, FormClosingEventArgs e)
    {
        if (_cts is not null)
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = null;

            Text = "";
        }
        
        Dispose();
    }

    private void LoadBootFont()
    {
        var windowsFolderPath = Environment.GetFolderPath(Environment.SpecialFolder.Windows);
        var bootFolder        = Path.Combine(windowsFolderPath, BootFontPath);
        var fontFilePath      = Path.Combine(bootFolder, FontFileName);

        _pfc.AddFontFile(fontFilePath);
    }

    private async void OnIsSpinningChanged(EventArgs e)
    {
        IsSpinningChanged?.Invoke(this, e);
        
        if (_cts is not null)
        {
            _cts.Cancel();
            _cts.Dispose();
            _cts = null;

            Text = "";

            return;
        }

        _cts = new CancellationTokenSource();

        await SpinAsync(_cts.Token);
    }

    private async Task SpinAsync(CancellationToken ct = default)
    {
        var timer = new PeriodicTimer(TimeSpan.FromMilliseconds(15));
        
        try
        {
            var index = 0;

            while (await timer.WaitForNextTickAsync(ct))
            {
                if (ct.IsCancellationRequested) break;

                if (IsHandleCreated)
                {
                    var parts = SpinnerStyle switch
                    {
                        SpinnerStyle.Dots => _dotStyleParts,
                        SpinnerStyle.Line => _lineStyleParts,
                        _                 => throw new ArgumentOutOfRangeException()
                    };

                    await InvokeAsync(() =>
                    {
                        Text = parts[index].ToString();

                        index = (index + 1) % parts.Length;
                    }, ct);
                }
            }
        }
        catch
        {
            //
        }
        finally
        {
            timer.Dispose();
        }
    }

    private static char[] CharSequence(Range range)
    {
        var start = range.Start.Value;
        var end   = range.End.Value;
        if (start >= end)
        {
            throw new ArgumentException("Start of the range must be less than the end.");
        }

        var chars = new char[end - start];
        for (int i = 0; i < chars.Length; i++)
        {
            chars[i] = (char)(start + i);
        }

        return chars;
    }
}
