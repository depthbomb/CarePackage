namespace CarePackage.Extensions;

public static class ColorExtensions
{
    public static bool IsLight(this Color color)
    {
        var brightness = (color.R * 0.299 + color.G * 0.587 + color.B * 0.114) / 255;
        
        return brightness > 0.5;
    }

    public static Color ToDrawingColor(this Windows.UI.Color color) => Color.FromArgb(color.A, color.R, color.G, color.B);
}
