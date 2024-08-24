using System.ComponentModel;

namespace CarePackage.Forms;

partial class AboutForm
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
        c_Logo = new Controls.InterpolatedPictureBox();
        c_TitleLabel = new Label();
        c_VersionLabel = new Label();
        tableLayoutPanel1 = new TableLayoutPanel();
        c_GithubLinkLabel = new LinkLabel();
        ((ISupportInitialize)c_Logo).BeginInit();
        tableLayoutPanel1.SuspendLayout();
        SuspendLayout();
        // 
        // c_Logo
        // 
        c_Logo.Anchor = AnchorStyles.None;
        c_Logo.BackColor = Color.Transparent;
        c_Logo.Image = Resources.Images.icon;
        c_Logo.ImeMode = ImeMode.NoControl;
        c_Logo.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.HighQualityBilinear;
        c_Logo.Location = new Point(55, 3);
        c_Logo.Margin = new Padding(0);
        c_Logo.MaximumSize = new Size(64, 64);
        c_Logo.Name = "c_Logo";
        c_Logo.Size = new Size(64, 64);
        c_Logo.SizeMode = PictureBoxSizeMode.Zoom;
        c_Logo.TabIndex = 2;
        c_Logo.TabStop = false;
        // 
        // c_TitleLabel
        // 
        c_TitleLabel.Dock = DockStyle.Fill;
        c_TitleLabel.Font = new Font("Segoe UI Semibold", 15.75F, FontStyle.Bold, GraphicsUnit.Point, 0);
        c_TitleLabel.Location = new Point(6, 70);
        c_TitleLabel.Margin = new Padding(3);
        c_TitleLabel.Name = "c_TitleLabel";
        c_TitleLabel.Size = new Size(162, 34);
        c_TitleLabel.TabIndex = 3;
        c_TitleLabel.Text = "CarePackage";
        c_TitleLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // c_VersionLabel
        // 
        c_VersionLabel.Dock = DockStyle.Fill;
        c_VersionLabel.Location = new Point(6, 110);
        c_VersionLabel.Margin = new Padding(3);
        c_VersionLabel.Name = "c_VersionLabel";
        c_VersionLabel.Size = new Size(162, 18);
        c_VersionLabel.TabIndex = 4;
        c_VersionLabel.Text = "v0.0.0";
        c_VersionLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // tableLayoutPanel1
        // 
        tableLayoutPanel1.ColumnCount = 1;
        tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
        tableLayoutPanel1.Controls.Add(c_VersionLabel, 0, 2);
        tableLayoutPanel1.Controls.Add(c_Logo, 0, 0);
        tableLayoutPanel1.Controls.Add(c_TitleLabel, 0, 1);
        tableLayoutPanel1.Controls.Add(c_GithubLinkLabel, 0, 3);
        tableLayoutPanel1.Dock = DockStyle.Fill;
        tableLayoutPanel1.Location = new Point(0, 0);
        tableLayoutPanel1.Name = "tableLayoutPanel1";
        tableLayoutPanel1.Padding = new Padding(3);
        tableLayoutPanel1.RowCount = 4;
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Absolute, 64F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Absolute, 40F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        tableLayoutPanel1.Size = new Size(174, 158);
        tableLayoutPanel1.TabIndex = 5;
        // 
        // c_GithubLinkLabel
        // 
        c_GithubLinkLabel.AutoSize = true;
        c_GithubLinkLabel.Dock = DockStyle.Fill;
        c_GithubLinkLabel.LinkBehavior = LinkBehavior.HoverUnderline;
        c_GithubLinkLabel.Location = new Point(6, 131);
        c_GithubLinkLabel.Name = "c_GithubLinkLabel";
        c_GithubLinkLabel.Size = new Size(162, 24);
        c_GithubLinkLabel.TabIndex = 5;
        c_GithubLinkLabel.TabStop = true;
        c_GithubLinkLabel.Text = "GitHub";
        c_GithubLinkLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // AboutForm
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(174, 158);
        Controls.Add(tableLayoutPanel1);
        FormBorderStyle = FormBorderStyle.FixedSingle;
        MaximizeBox = false;
        MinimizeBox = false;
        Name = "AboutForm";
        ShowIcon = false;
        ShowInTaskbar = false;
        StartPosition = FormStartPosition.CenterParent;
        Text = "About";
        ((ISupportInitialize)c_Logo).EndInit();
        tableLayoutPanel1.ResumeLayout(false);
        tableLayoutPanel1.PerformLayout();
        ResumeLayout(false);
    }

    #endregion

    private Controls.InterpolatedPictureBox c_Logo;
    private Label c_TitleLabel;
    private Label c_VersionLabel;
    private TableLayoutPanel tableLayoutPanel1;
    private LinkLabel c_GithubLinkLabel;
}

