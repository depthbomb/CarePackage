namespace CarePackage.Renderers;

public class AccentedContextMenuStripRenderer : ToolStripProfessionalRenderer
{
    public AccentedContextMenuStripRenderer() : base(new AccentedColors()) { }

    private class AccentedColors : ProfessionalColorTable
    {
        public override Color MenuBorder                    => Personalize.GetAccentColor(ColorType.Accent);
        public override Color MenuItemBorder                => Color.Transparent;
        public override Color MenuItemSelectedGradientBegin => Personalize.GetAccentColor(ColorType.Light3);
        public override Color MenuItemSelectedGradientEnd   => Personalize.GetAccentColor(ColorType.Light3);
    }
}
