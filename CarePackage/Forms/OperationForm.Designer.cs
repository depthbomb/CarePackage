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
        groupBox1 = new GroupBox();
        c_OptionsTableLayout = new TableLayoutPanel();
        c_CleanUpExecutablesCheckBox = new CheckBox();
        c_SkipInstallCheckBox = new CheckBox();
        c_InstallSilentlyCheckBox = new CheckBox();
        c_OpenDownloadFolderCheckBox = new CheckBox();
        c_StartOperationButton = new Button();
        c_CancelOperationButton = new Button();
        c_StatusLabel = new Label();
        c_ProgressBar = new ProgressBar();
        c_ProgressLabel = new Label();
        c_ProgressLabelsTableLayout = new TableLayoutPanel();
        c_PercentStatusLabel = new Label();
        groupBox1.SuspendLayout();
        c_OptionsTableLayout.SuspendLayout();
        c_ProgressLabelsTableLayout.SuspendLayout();
        SuspendLayout();
        // 
        // groupBox1
        // 
        groupBox1.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right;
        groupBox1.Controls.Add(c_OptionsTableLayout);
        groupBox1.Location = new Point(12, 12);
        groupBox1.Name = "groupBox1";
        groupBox1.Size = new Size(512, 82);
        groupBox1.TabIndex = 0;
        groupBox1.TabStop = false;
        groupBox1.Text = "Options";
        // 
        // c_OptionsTableLayout
        // 
        c_OptionsTableLayout.ColumnCount = 2;
        c_OptionsTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 49.9999924F));
        c_OptionsTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50.0000038F));
        c_OptionsTableLayout.Controls.Add(c_CleanUpExecutablesCheckBox, 1, 1);
        c_OptionsTableLayout.Controls.Add(c_SkipInstallCheckBox, 0, 0);
        c_OptionsTableLayout.Controls.Add(c_InstallSilentlyCheckBox, 0, 1);
        c_OptionsTableLayout.Controls.Add(c_OpenDownloadFolderCheckBox, 1, 0);
        c_OptionsTableLayout.Dock = DockStyle.Fill;
        c_OptionsTableLayout.Location = new Point(3, 19);
        c_OptionsTableLayout.Name = "c_OptionsTableLayout";
        c_OptionsTableLayout.RowCount = 2;
        c_OptionsTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        c_OptionsTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        c_OptionsTableLayout.Size = new Size(506, 60);
        c_OptionsTableLayout.TabIndex = 0;
        // 
        // c_CleanUpExecutablesCheckBox
        // 
        c_CleanUpExecutablesCheckBox.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        c_CleanUpExecutablesCheckBox.AutoSize = true;
        c_CleanUpExecutablesCheckBox.Location = new Point(255, 33);
        c_CleanUpExecutablesCheckBox.Name = "c_CleanUpExecutablesCheckBox";
        c_CleanUpExecutablesCheckBox.Size = new Size(248, 24);
        c_CleanUpExecutablesCheckBox.TabIndex = 3;
        c_CleanUpExecutablesCheckBox.Text = "Clean up installers after installation";
        c_CleanUpExecutablesCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_SkipInstallCheckBox
        // 
        c_SkipInstallCheckBox.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        c_SkipInstallCheckBox.AutoSize = true;
        c_SkipInstallCheckBox.Location = new Point(3, 3);
        c_SkipInstallCheckBox.Name = "c_SkipInstallCheckBox";
        c_SkipInstallCheckBox.Size = new Size(246, 24);
        c_SkipInstallCheckBox.TabIndex = 0;
        c_SkipInstallCheckBox.Text = "Skip installation";
        c_SkipInstallCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_InstallSilentlyCheckBox
        // 
        c_InstallSilentlyCheckBox.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        c_InstallSilentlyCheckBox.AutoSize = true;
        c_InstallSilentlyCheckBox.Location = new Point(3, 33);
        c_InstallSilentlyCheckBox.Name = "c_InstallSilentlyCheckBox";
        c_InstallSilentlyCheckBox.Size = new Size(246, 24);
        c_InstallSilentlyCheckBox.TabIndex = 2;
        c_InstallSilentlyCheckBox.Text = "Try to install silently";
        c_InstallSilentlyCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_OpenDownloadFolderCheckBox
        // 
        c_OpenDownloadFolderCheckBox.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        c_OpenDownloadFolderCheckBox.AutoSize = true;
        c_OpenDownloadFolderCheckBox.Location = new Point(255, 3);
        c_OpenDownloadFolderCheckBox.Name = "c_OpenDownloadFolderCheckBox";
        c_OpenDownloadFolderCheckBox.Size = new Size(248, 24);
        c_OpenDownloadFolderCheckBox.TabIndex = 1;
        c_OpenDownloadFolderCheckBox.Text = "Open download folder";
        c_OpenDownloadFolderCheckBox.UseVisualStyleBackColor = true;
        // 
        // c_StartOperationButton
        // 
        c_StartOperationButton.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
        c_StartOperationButton.AutoSize = true;
        c_StartOperationButton.Location = new Point(12, 207);
        c_StartOperationButton.Name = "c_StartOperationButton";
        c_StartOperationButton.Size = new Size(128, 25);
        c_StartOperationButton.TabIndex = 2;
        c_StartOperationButton.Text = "&Download and install";
        c_StartOperationButton.UseVisualStyleBackColor = true;
        // 
        // c_CancelOperationButton
        // 
        c_CancelOperationButton.Anchor = AnchorStyles.Bottom | AnchorStyles.Left;
        c_CancelOperationButton.AutoSize = true;
        c_CancelOperationButton.Location = new Point(146, 207);
        c_CancelOperationButton.Name = "c_CancelOperationButton";
        c_CancelOperationButton.Size = new Size(75, 25);
        c_CancelOperationButton.TabIndex = 3;
        c_CancelOperationButton.Text = "&Cancel";
        c_CancelOperationButton.UseVisualStyleBackColor = true;
        // 
        // c_StatusLabel
        // 
        c_StatusLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        c_StatusLabel.Location = new Point(12, 103);
        c_StatusLabel.Margin = new Padding(3, 6, 3, 6);
        c_StatusLabel.Name = "c_StatusLabel";
        c_StatusLabel.Size = new Size(512, 25);
        c_StatusLabel.TabIndex = 4;
        c_StatusLabel.Text = "Waiting";
        c_StatusLabel.TextAlign = ContentAlignment.MiddleLeft;
        // 
        // c_ProgressBar
        // 
        c_ProgressBar.Location = new Point(12, 137);
        c_ProgressBar.MarqueeAnimationSpeed = 20;
        c_ProgressBar.Name = "c_ProgressBar";
        c_ProgressBar.Size = new Size(512, 23);
        c_ProgressBar.TabIndex = 5;
        // 
        // c_ProgressLabel
        // 
        c_ProgressLabel.BackColor = Color.Transparent;
        c_ProgressLabel.Dock = DockStyle.Fill;
        c_ProgressLabel.Location = new Point(0, 0);
        c_ProgressLabel.Margin = new Padding(0);
        c_ProgressLabel.Name = "c_ProgressLabel";
        c_ProgressLabel.Size = new Size(256, 25);
        c_ProgressLabel.TabIndex = 6;
        c_ProgressLabel.Text = "...";
        c_ProgressLabel.TextAlign = ContentAlignment.MiddleLeft;
        // 
        // c_ProgressLabelsTableLayout
        // 
        c_ProgressLabelsTableLayout.ColumnCount = 2;
        c_ProgressLabelsTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        c_ProgressLabelsTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        c_ProgressLabelsTableLayout.Controls.Add(c_ProgressLabel, 0, 0);
        c_ProgressLabelsTableLayout.Controls.Add(c_PercentStatusLabel, 1, 0);
        c_ProgressLabelsTableLayout.Location = new Point(12, 169);
        c_ProgressLabelsTableLayout.Margin = new Padding(3, 6, 3, 6);
        c_ProgressLabelsTableLayout.Name = "c_ProgressLabelsTableLayout";
        c_ProgressLabelsTableLayout.RowCount = 1;
        c_ProgressLabelsTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        c_ProgressLabelsTableLayout.Size = new Size(512, 25);
        c_ProgressLabelsTableLayout.TabIndex = 7;
        // 
        // c_PercentStatusLabel
        // 
        c_PercentStatusLabel.Dock = DockStyle.Fill;
        c_PercentStatusLabel.Location = new Point(256, 0);
        c_PercentStatusLabel.Margin = new Padding(0);
        c_PercentStatusLabel.Name = "c_PercentStatusLabel";
        c_PercentStatusLabel.Size = new Size(256, 25);
        c_PercentStatusLabel.TabIndex = 7;
        c_PercentStatusLabel.TextAlign = ContentAlignment.MiddleRight;
        // 
        // OperationForm
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        AutoSizeMode = AutoSizeMode.GrowAndShrink;
        ClientSize = new Size(536, 244);
        Controls.Add(c_ProgressLabelsTableLayout);
        Controls.Add(c_ProgressBar);
        Controls.Add(c_StatusLabel);
        Controls.Add(c_CancelOperationButton);
        Controls.Add(c_StartOperationButton);
        Controls.Add(groupBox1);
        FormBorderStyle = FormBorderStyle.FixedDialog;
        HelpButton = true;
        MaximizeBox = false;
        MinimizeBox = false;
        Name = "OperationForm";
        ShowIcon = false;
        ShowInTaskbar = false;
        StartPosition = FormStartPosition.CenterParent;
        Text = "CarePackage Installer";
        groupBox1.ResumeLayout(false);
        c_OptionsTableLayout.ResumeLayout(false);
        c_OptionsTableLayout.PerformLayout();
        c_ProgressLabelsTableLayout.ResumeLayout(false);
        ResumeLayout(false);
        PerformLayout();
    }

    #endregion

    private GroupBox groupBox1;
    private TableLayoutPanel c_OptionsTableLayout;
    private CheckBox c_SkipInstallCheckBox;
    private CheckBox c_OpenDownloadFolderCheckBox;
    private CheckBox c_InstallSilentlyCheckBox;
    private Button c_StartOperationButton;
    private Button c_CancelOperationButton;
    private CheckBox c_CleanUpExecutablesCheckBox;
    private Label c_StatusLabel;
    private ProgressBar c_ProgressBar;
    private Label c_ProgressLabel;
    private TableLayoutPanel c_ProgressLabelsTableLayout;
    private Label c_PercentStatusLabel;
}
