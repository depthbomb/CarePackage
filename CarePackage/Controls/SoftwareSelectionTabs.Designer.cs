using System.ComponentModel;

namespace CarePackage.Controls;

partial class SoftwareSelectionTabs
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
        Dock = DockStyle.Fill;
        c_SoftwareSelectionTabs = new TabControl();
        SuspendLayout();
        // 
        // c_SoftwareSelectionTabs
        // 
        c_SoftwareSelectionTabs.Dock = DockStyle.Fill;
        c_SoftwareSelectionTabs.Location = new Point(0, 0);
        c_SoftwareSelectionTabs.Multiline = true;
        c_SoftwareSelectionTabs.Name = "c_SoftwareSelectionTabs";
        c_SoftwareSelectionTabs.Padding = new Point(0, 0);
        c_SoftwareSelectionTabs.SelectedIndex = 0;
        c_SoftwareSelectionTabs.Size = new Size(1223, 869);
        c_SoftwareSelectionTabs.TabIndex = 0;
        // 
        // SoftwareSelectionControl
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        Controls.Add(c_SoftwareSelectionTabs);
        Name = "SoftwareSelectionTabs";
        Size = new Size(1223, 869);
        ResumeLayout(false);
    }

    #endregion

    private TabControl c_SoftwareSelectionTabs;
}
