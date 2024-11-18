using System.Drawing.Imaging.Effects;

namespace CarePackage.Extensions;

public static class BitmapExtensions
{
    public static Bitmap ToGrayScale(this Bitmap source)
    {
        var copy = (Bitmap)source.Clone();
        copy.ApplyEffect(new GrayScaleEffect(), Rectangle.Empty);

        return copy;
    }
}
