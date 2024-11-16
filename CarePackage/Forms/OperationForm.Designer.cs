using CarePackage.Controls;
using System.ComponentModel;

namespace CarePackage.Forms;

partial class OperationForm
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

    #region Windows Form Designer generated code
    /// <summary>
    /// Required method for Designer support - do not modify
    /// the contents of this method with the code editor.
    /// </summary>
    private void InitializeComponent()
    {
        groupBox1                    = new System.Windows.Forms.GroupBox();
        c_OptionsTableLayout         = new System.Windows.Forms.TableLayoutPanel();
        c_SkipInstallCheckBox        = new System.Windows.Forms.CheckBox();
        c_InstallSilentlyCheckBox    = new System.Windows.Forms.CheckBox();
        c_OpenDownloadFolderCheckBox = new System.Windows.Forms.CheckBox();
        c_CleanUpExecutablesCheckBox = new System.Windows.Forms.CheckBox();
        c_StartOperationButton       = new System.Windows.Forms.Button();
        c_CancelOperationButton      = new System.Windows.Forms.Button();
        tableLayoutPanel1            = new System.Windows.Forms.TableLayoutPanel();
        c_Spinner                    = new CarePackage.Controls.Spinner();
        c_StatusLabel                = new System.Windows.Forms.Label();
        groupBox1.SuspendLayout();
        c_OptionsTableLayout.SuspendLayout();
        tableLayoutPanel1.SuspendLayout();
        SuspendLayout();
        // 
        // groupBox1
        // 
        groupBox1.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        groupBox1.Controls.Add(c_OptionsTableLayout);
        groupBox1.Location = new System.Drawing.Point(12, 12);
        groupBox1.Name     = "groupBox1";
        groupBox1.Size     = new System.Drawing.Size(344, 142);
        groupBox1.TabIndex = 0;
        groupBox1.TabStop  = false;
        groupBox1.Text     = "Options";
        // 
        // c_OptionsTableLayout
        // 
        c_OptionsTableLayout.ColumnCount = 1;
        c_OptionsTableLayout.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
        c_OptionsTableLayout.Controls.Add(c_SkipInstallCheckBox, 0, 0);
        c_OptionsTableLayout.Controls.Add(c_InstallSilentlyCheckBox, 0, 1);
        c_OptionsTableLayout.Controls.Add(c_OpenDownloadFolderCheckBox, 0, 2);
        c_OptionsTableLayout.Controls.Add(c_CleanUpExecutablesCheckBox, 0, 3);
        c_OptionsTableLayout.Dock     = System.Windows.Forms.DockStyle.Fill;
        c_OptionsTableLayout.Location = new System.Drawing.Point(3, 19);
        c_OptionsTableLayout.Name     = "c_OptionsTableLayout";
        c_OptionsTableLayout.RowCount = 4;
        c_OptionsTableLayout.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
        c_OptionsTableLayout.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
        c_OptionsTableLayout.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
        c_OptionsTableLayout.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 25F));
        c_OptionsTableLayout.Size     = new System.Drawing.Size(338, 120);
        c_OptionsTableLayout.TabIndex = 0;
        // 
        // c_SkipInstallCheckBox
        // 
        c_SkipInstallCheckBox.Anchor                  = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        c_SkipInstallCheckBox.AutoSize                = true;
        c_SkipInstallCheckBox.Location                = new System.Drawing.Point(3, 3);
        c_SkipInstallCheckBox.Name                    = "c_SkipInstallCheckBox";
        c_SkipInstallCheckBox.Size                    = new System.Drawing.Size(332, 24);
        c_SkipInstallCheckBox.TabIndex                = 0;
        c_SkipInstallCheckBox.Text                    = "Skip installation";
        c_SkipInstallCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_InstallSilentlyCheckBox
        // 
        c_InstallSilentlyCheckBox.Anchor                  = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        c_InstallSilentlyCheckBox.AutoSize                = true;
        c_InstallSilentlyCheckBox.Location                = new System.Drawing.Point(3, 33);
        c_InstallSilentlyCheckBox.Name                    = "c_InstallSilentlyCheckBox";
        c_InstallSilentlyCheckBox.Size                    = new System.Drawing.Size(332, 24);
        c_InstallSilentlyCheckBox.TabIndex                = 2;
        c_InstallSilentlyCheckBox.Text                    = "Try to install silently";
        c_InstallSilentlyCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_OpenDownloadFolderCheckBox
        // 
        c_OpenDownloadFolderCheckBox.Anchor                  = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        c_OpenDownloadFolderCheckBox.AutoSize                = true;
        c_OpenDownloadFolderCheckBox.Location                = new System.Drawing.Point(3, 63);
        c_OpenDownloadFolderCheckBox.Name                    = "c_OpenDownloadFolderCheckBox";
        c_OpenDownloadFolderCheckBox.Size                    = new System.Drawing.Size(332, 24);
        c_OpenDownloadFolderCheckBox.TabIndex                = 1;
        c_OpenDownloadFolderCheckBox.Text                    = "Open download folder";
        c_OpenDownloadFolderCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_CleanUpExecutablesCheckBox
        // 
        c_CleanUpExecutablesCheckBox.Anchor                  = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        c_CleanUpExecutablesCheckBox.AutoSize                = true;
        c_CleanUpExecutablesCheckBox.Location                = new System.Drawing.Point(3, 93);
        c_CleanUpExecutablesCheckBox.Name                    = "c_CleanUpExecutablesCheckBox";
        c_CleanUpExecutablesCheckBox.Size                    = new System.Drawing.Size(332, 24);
        c_CleanUpExecutablesCheckBox.TabIndex                = 3;
        c_CleanUpExecutablesCheckBox.Text                    = "Delete installers after installation";
        c_CleanUpExecutablesCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_StartOperationButton
        // 
        c_StartOperationButton.Anchor                  = ((System.Windows.Forms.AnchorStyles)(System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left));
        c_StartOperationButton.AutoSize                = true;
        c_StartOperationButton.Location                = new System.Drawing.Point(12, 201);
        c_StartOperationButton.Name                    = "c_StartOperationButton";
        c_StartOperationButton.Size                    = new System.Drawing.Size(128, 25);
        c_StartOperationButton.TabIndex                = 2;
        c_StartOperationButton.Text                    = "&Download and install";
        c_StartOperationButton.UseVisualStyleBackColor = true;
        // 
        // c_CancelOperationButton
        // 
        c_CancelOperationButton.Anchor                  = ((System.Windows.Forms.AnchorStyles)(System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left));
        c_CancelOperationButton.AutoSize                = true;
        c_CancelOperationButton.Location                = new System.Drawing.Point(146, 201);
        c_CancelOperationButton.Name                    = "c_CancelOperationButton";
        c_CancelOperationButton.Size                    = new System.Drawing.Size(75, 25);
        c_CancelOperationButton.TabIndex                = 3;
        c_CancelOperationButton.Text                    = "&Cancel";
        c_CancelOperationButton.UseVisualStyleBackColor = true;
        // 
        // tableLayoutPanel1
        // 
        tableLayoutPanel1.Anchor       = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        tableLayoutPanel1.AutoSizeMode = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
        tableLayoutPanel1.ColumnCount  = 2;
        tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Absolute, 24F));
        tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle(System.Windows.Forms.SizeType.Percent, 100F));
        tableLayoutPanel1.Controls.Add(c_Spinner, 0, 0);
        tableLayoutPanel1.Controls.Add(c_StatusLabel, 1, 0);
        tableLayoutPanel1.Location = new System.Drawing.Point(15, 163);
        tableLayoutPanel1.Margin   = new System.Windows.Forms.Padding(6);
        tableLayoutPanel1.Name     = "tableLayoutPanel1";
        tableLayoutPanel1.RowCount = 1;
        tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 32F));
        tableLayoutPanel1.Size     = new System.Drawing.Size(344, 30);
        tableLayoutPanel1.TabIndex = 4;
        // 
        // c_Spinner
        // 
        c_Spinner.Anchor       = System.Windows.Forms.AnchorStyles.None;
        c_Spinner.IsSpinning   = false;
        c_Spinner.Location     = new System.Drawing.Point(0, 4);
        c_Spinner.Margin       = new System.Windows.Forms.Padding(0);
        c_Spinner.Name         = "c_Spinner";
        c_Spinner.Size         = new System.Drawing.Size(24, 24);
        c_Spinner.SpinnerStyle = CarePackage.Controls.SpinnerStyle.Line;
        c_Spinner.TabIndex     = 0;
        c_Spinner.TextAlign    = System.Drawing.ContentAlignment.MiddleCenter;
        // 
        // c_StatusLabel
        // 
        c_StatusLabel.Anchor    = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom) | System.Windows.Forms.AnchorStyles.Left) | System.Windows.Forms.AnchorStyles.Right));
        c_StatusLabel.Location  = new System.Drawing.Point(27, 0);
        c_StatusLabel.Name      = "c_StatusLabel";
        c_StatusLabel.Size      = new System.Drawing.Size(314, 32);
        c_StatusLabel.TabIndex  = 1;
        c_StatusLabel.Text      = "...";
        c_StatusLabel.TextAlign = System.Drawing.ContentAlignment.MiddleLeft;
        // 
        // OperationForm
        // 
        AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
        AutoScaleMode       = System.Windows.Forms.AutoScaleMode.Font;
        AutoSizeMode        = System.Windows.Forms.AutoSizeMode.GrowAndShrink;
        ClientSize          = new System.Drawing.Size(371, 237);
        Controls.Add(c_CancelOperationButton);
        Controls.Add(c_StartOperationButton);
        Controls.Add(tableLayoutPanel1);
        Controls.Add(groupBox1);
        FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
        HelpButton      = true;
        MaximizeBox     = false;
        MinimizeBox     = false;
        ShowIcon        = false;
        ShowInTaskbar   = false;
        StartPosition   = System.Windows.Forms.FormStartPosition.CenterParent;
        Text            = "CarePackage Installer";
        groupBox1.ResumeLayout(false);
        c_OptionsTableLayout.ResumeLayout(false);
        c_OptionsTableLayout.PerformLayout();
        tableLayoutPanel1.ResumeLayout(false);
        ResumeLayout(false);
        PerformLayout();
    }

    private System.Windows.Forms.Label c_StatusLabel;

    private CarePackage.Controls.Spinner c_Spinner;

    private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
    #endregion

    private System.Windows.Forms.GroupBox         groupBox1;
    private System.Windows.Forms.TableLayoutPanel c_OptionsTableLayout;
    private System.Windows.Forms.CheckBox         c_SkipInstallCheckBox;
    private System.Windows.Forms.CheckBox         c_OpenDownloadFolderCheckBox;
    private System.Windows.Forms.CheckBox         c_InstallSilentlyCheckBox;
    private System.Windows.Forms.Button           c_StartOperationButton;
    private System.Windows.Forms.Button           c_CancelOperationButton;
    private System.Windows.Forms.CheckBox         c_CleanUpExecutablesCheckBox;
}
