using System.Drawing.Drawing2D;

namespace CarePackage.Controls;

public class InterpolatedPictureBox : PictureBox
{
    public InterpolationMode InterpolationMode { get; set; } = InterpolationMode.Default;

    #region Overrides of PictureBox
    protected override void OnPaint(PaintEventArgs pe)
    {
        pe.Graphics.InterpolationMode = InterpolationMode;
        base.OnPaint(pe);
    }
    #endregion
}
