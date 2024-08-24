using System.ComponentModel;
using System.Drawing.Drawing2D;

namespace CarePackage.Controls;

partial class SoftwareListItem
{
    /// <summary> 
    /// Required designer variable.
    /// </summary>
    private IContainer components = null;

    /// <summary> 
    /// Clean up any resources being used.
    /// </summary>
    /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
    protected override void Dispose(bool disposing)
    {
        if (disposing && (components != null))
        {
            components.Dispose();
        }

        base.Dispose(disposing);
    }

    #region Component Designer generated code

    /// <summary> 
    /// Required method for Designer support - do not modify 
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        c_SoftwareName = new Label();
        c_SoftwareIcon = new InterpolatedPictureBox();
        ((ISupportInitialize)c_SoftwareIcon).BeginInit();
        SuspendLayout();
        // 
        // c_SoftwareName
        // 
        c_SoftwareName.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left;
        c_SoftwareName.AutoSize = true;
        c_SoftwareName.Font = new Font("Segoe UI", 11.25F, FontStyle.Regular, GraphicsUnit.Point, 0);
        c_SoftwareName.ForeColor = Color.DimGray;
        c_SoftwareName.Location = new Point(44, 22);
        c_SoftwareName.Name = "c_SoftwareName";
        c_SoftwareName.Size = new Size(70, 20);
        c_SoftwareName.TabIndex = 0;
        c_SoftwareName.Text = "Unknown";
        // 
        // c_SoftwareIcon
        // 
        c_SoftwareIcon.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left;
        c_SoftwareIcon.BackColor = Color.Transparent;
        c_SoftwareIcon.InterpolationMode = InterpolationMode.High;
        c_SoftwareIcon.Location = new Point(3, 16);
        c_SoftwareIcon.Margin = new Padding(3, 3, 6, 3);
        c_SoftwareIcon.Name = "c_SoftwareIcon";
        c_SoftwareIcon.Size = new Size(32, 32);
        c_SoftwareIcon.SizeMode = PictureBoxSizeMode.Zoom;
        c_SoftwareIcon.TabIndex = 1;
        c_SoftwareIcon.TabStop = false;
        // 
        // SoftwareListItem
        // 
        AutoScaleMode = AutoScaleMode.None;
        AutoSize = true;
        BackColor = Color.Transparent;
        Controls.Add(c_SoftwareIcon);
        Controls.Add(c_SoftwareName);
        Cursor = Cursors.Hand;
        Margin = new Padding(0);
        Name = "SoftwareListItem";
        Size = new Size(500, 64);
        ((ISupportInitialize)c_SoftwareIcon).EndInit();
        ResumeLayout(false);
        PerformLayout();
    }

    #endregion

    private Label c_SoftwareName;
    private InterpolatedPictureBox c_SoftwareIcon;
}
