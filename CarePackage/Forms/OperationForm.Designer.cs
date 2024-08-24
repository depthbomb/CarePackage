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
        c_Spinner = new SpinnerControl();
        tableLayoutPanel1 = new TableLayoutPanel();
        groupBox1.SuspendLayout();
        c_OptionsTableLayout.SuspendLayout();
        tableLayoutPanel1.SuspendLayout();
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
        c_StartOperationButton.Location = new Point(12, 100);
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
        c_CancelOperationButton.Location = new Point(146, 100);
        c_CancelOperationButton.Name = "c_CancelOperationButton";
        c_CancelOperationButton.Size = new Size(75, 25);
        c_CancelOperationButton.TabIndex = 3;
        c_CancelOperationButton.Text = "&Cancel";
        c_CancelOperationButton.UseVisualStyleBackColor = true;
        // 
        // c_StatusLabel
        // 
        c_StatusLabel.AutoSize = true;
        c_StatusLabel.Dock = DockStyle.Fill;
        c_StatusLabel.Location = new Point(28, 0);
        c_StatusLabel.Name = "c_StatusLabel";
        c_StatusLabel.Size = new Size(1, 25);
        c_StatusLabel.TabIndex = 1;
        c_StatusLabel.TextAlign = ContentAlignment.MiddleRight;
        // 
        // c_Spinner
        // 
        c_Spinner.Dock = DockStyle.Fill;
        c_Spinner.Font = new Font("Segoe Boot Semilight", 10F);
        c_Spinner.IsSpinning = false;
        c_Spinner.Location = new Point(3, 0);
        c_Spinner.Name = "c_Spinner";
        c_Spinner.Size = new Size(19, 25);
        c_Spinner.SpinnerStyle = SpinnerStyle.Line;
        c_Spinner.TabIndex = 0;
        c_Spinner.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // tableLayoutPanel1
        // 
        tableLayoutPanel1.Anchor = AnchorStyles.Bottom | AnchorStyles.Right;
        tableLayoutPanel1.AutoSize = true;
        tableLayoutPanel1.AutoSizeMode = AutoSizeMode.GrowAndShrink;
        tableLayoutPanel1.ColumnCount = 2;
        tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Absolute, 25F));
        tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle());
        tableLayoutPanel1.Controls.Add(c_Spinner, 0, 0);
        tableLayoutPanel1.Controls.Add(c_StatusLabel, 1, 0);
        tableLayoutPanel1.Location = new Point(493, 100);
        tableLayoutPanel1.Name = "tableLayoutPanel1";
        tableLayoutPanel1.RowCount = 1;
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
        tableLayoutPanel1.Size = new Size(31, 25);
        tableLayoutPanel1.TabIndex = 4;
        // 
        // OperationForm
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        AutoSizeMode = AutoSizeMode.GrowAndShrink;
        BackColor = Color.White;
        ClientSize = new Size(536, 136);
        Controls.Add(tableLayoutPanel1);
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
        tableLayoutPanel1.ResumeLayout(false);
        tableLayoutPanel1.PerformLayout();
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
    private Label c_StatusLabel;
    private CheckBox c_CleanUpExecutablesCheckBox;
    private SpinnerControl c_Spinner;
    private TableLayoutPanel tableLayoutPanel1;
}
