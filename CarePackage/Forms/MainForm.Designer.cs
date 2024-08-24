using System.Drawing.Drawing2D;
using CarePackage.Controls;

namespace CarePackage.Forms;

partial class MainForm
{
    /// <summary>
    ///  Required designer variable.
    /// </summary>
    private System.ComponentModel.IContainer components = null;

    /// <summary>
    ///  Clean up any resources being used.
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

    #region Windows Form Designer generated code

    /// <summary>
    ///  Required method for Designer support - do not modify
    ///  the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
        c_PrepareOperationButton = new Button();
        c_SoftwareSelectionSlotPanel = new Panel();
        c_ClearSelectionButton = new Button();
        c_AboutLinkLabel = new LinkLabel();
        c_HeadingLabel = new Label();
        c_Debug_SelectAllButton = new Button();
        c_LatestReleaseLinkLabel = new LinkLabel();
        c_SuggestionLinkLabel = new LinkLabel();
        SuspendLayout();
        // 
        // c_PrepareOperationButton
        // 
        resources.ApplyResources(c_PrepareOperationButton, "c_PrepareOperationButton");
        c_PrepareOperationButton.Name = "c_PrepareOperationButton";
        c_PrepareOperationButton.UseVisualStyleBackColor = true;
        // 
        // c_SoftwareSelectionSlotPanel
        // 
        resources.ApplyResources(c_SoftwareSelectionSlotPanel, "c_SoftwareSelectionSlotPanel");
        c_SoftwareSelectionSlotPanel.BackColor = Color.Transparent;
        c_SoftwareSelectionSlotPanel.Name = "c_SoftwareSelectionSlotPanel";
        // 
        // c_ClearSelectionButton
        // 
        resources.ApplyResources(c_ClearSelectionButton, "c_ClearSelectionButton");
        c_ClearSelectionButton.Name = "c_ClearSelectionButton";
        c_ClearSelectionButton.UseVisualStyleBackColor = true;
        // 
        // c_AboutLinkLabel
        // 
        c_AboutLinkLabel.ActiveLinkColor = SystemColors.HotTrack;
        resources.ApplyResources(c_AboutLinkLabel, "c_AboutLinkLabel");
        c_AboutLinkLabel.BackColor = Color.Transparent;
        c_AboutLinkLabel.LinkBehavior = LinkBehavior.HoverUnderline;
        c_AboutLinkLabel.LinkColor = SystemColors.Highlight;
        c_AboutLinkLabel.Name = "c_AboutLinkLabel";
        c_AboutLinkLabel.TabStop = true;
        // 
        // c_HeadingLabel
        // 
        c_HeadingLabel.BackColor = Color.Transparent;
        resources.ApplyResources(c_HeadingLabel, "c_HeadingLabel");
        c_HeadingLabel.ForeColor = SystemColors.Highlight;
        c_HeadingLabel.Name = "c_HeadingLabel";
        // 
        // c_Debug_SelectAllButton
        // 
        resources.ApplyResources(c_Debug_SelectAllButton, "c_Debug_SelectAllButton");
        c_Debug_SelectAllButton.Name = "c_Debug_SelectAllButton";
        c_Debug_SelectAllButton.UseVisualStyleBackColor = true;
        // 
        // c_LatestReleaseLinkLabel
        // 
        c_LatestReleaseLinkLabel.ActiveLinkColor = SystemColors.HotTrack;
        resources.ApplyResources(c_LatestReleaseLinkLabel, "c_LatestReleaseLinkLabel");
        c_LatestReleaseLinkLabel.LinkBehavior = LinkBehavior.HoverUnderline;
        c_LatestReleaseLinkLabel.LinkColor = SystemColors.Highlight;
        c_LatestReleaseLinkLabel.Name = "c_LatestReleaseLinkLabel";
        c_LatestReleaseLinkLabel.TabStop = true;
        // 
        // c_SuggestionLinkLabel
        // 
        c_SuggestionLinkLabel.ActiveLinkColor = SystemColors.HotTrack;
        resources.ApplyResources(c_SuggestionLinkLabel, "c_SuggestionLinkLabel");
        c_SuggestionLinkLabel.LinkBehavior = LinkBehavior.HoverUnderline;
        c_SuggestionLinkLabel.LinkColor = SystemColors.Highlight;
        c_SuggestionLinkLabel.Name = "c_SuggestionLinkLabel";
        c_SuggestionLinkLabel.TabStop = true;
        // 
        // MainForm
        // 
        resources.ApplyResources(this, "$this");
        AutoScaleMode = AutoScaleMode.Font;
        Controls.Add(c_LatestReleaseLinkLabel);
        Controls.Add(c_SuggestionLinkLabel);
        Controls.Add(c_Debug_SelectAllButton);
        Controls.Add(c_AboutLinkLabel);
        Controls.Add(c_HeadingLabel);
        Controls.Add(c_ClearSelectionButton);
        Controls.Add(c_SoftwareSelectionSlotPanel);
        Controls.Add(c_PrepareOperationButton);
        HelpButton = true;
        Name = "MainForm";
        ResumeLayout(false);
        PerformLayout();
    }

    #endregion
    private Button c_PrepareOperationButton;
    private Panel c_SoftwareSelectionSlotPanel;
    private Button c_ClearSelectionButton;
    private LinkLabel c_AboutLinkLabel;
    private Label c_HeadingLabel;
    private Button c_Debug_SelectAllButton;
    private LinkLabel c_LatestReleaseLinkLabel;
    private LinkLabel c_SuggestionLinkLabel;
}
