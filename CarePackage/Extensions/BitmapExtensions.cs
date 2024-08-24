using System.Drawing.Imaging;

namespace CarePackage.Extensions;

public static class BitmapExtensions
{
    private static readonly ColorMatrix GrayMatrix = new(
    [
        [.2126f, .2126f, .2126f, 0, 0],
        [.7152f, .7152f, .7152f, 0, 0],
        [.0722f, .0722f, .0722f, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1]
    ]);
    
    public static Bitmap ToGrayScale(this Bitmap source)
    {
        var grayscaleVersion = new Bitmap(source.Width, source.Height, source.PixelFormat);
            grayscaleVersion.SetResolution(source.HorizontalResolution, source.VerticalResolution);

        using (var g = Graphics.FromImage(grayscaleVersion))
        using (var attrs = new ImageAttributes())
        {
            attrs.SetColorMatrix(GrayMatrix);
            g.DrawImage(source, new Rectangle(0, 0, source.Width, source.Height), 0, 0, source.Width, source.Height, GraphicsUnit.Pixel, attrs);

            return grayscaleVersion;
        }
    }
}
