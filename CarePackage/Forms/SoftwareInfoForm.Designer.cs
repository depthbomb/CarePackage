using System.ComponentModel;

namespace CarePackage.Forms;

partial class SoftwareInfoForm
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
        tableLayoutPanel1 = new TableLayoutPanel();
        C_RequiresAdminValue = new Label();
        C_ShouldCacheDownloadUrlValue = new Label();
        C_IsArchiveValue = new Label();
        C_DownloadNameValue = new Label();
        C_CategoryValue = new Label();
        C_NameValue = new Label();
        C_KeyValue = new Label();
        C_KeyLabel = new Label();
        C_NameLabel = new Label();
        C_CategoryLabel = new Label();
        C_HomepageLabel = new Label();
        C_IconLabel = new Label();
        C_RequiresAdminLabel = new Label();
        C_ShouldCacheDownloadUrlLabel = new Label();
        C_IsArchiveLabel = new Label();
        C_DownloadNameLabel = new Label();
        C_HomepageLinkLabel = new LinkLabel();
        tableLayoutPanel2 = new TableLayoutPanel();
        C_IconPictureBoxGrayscale = new PictureBox();
        C_IconPictureBox = new PictureBox();
        tableLayoutPanel1.SuspendLayout();
        tableLayoutPanel2.SuspendLayout();
        ((ISupportInitialize)C_IconPictureBoxGrayscale).BeginInit();
        ((ISupportInitialize)C_IconPictureBox).BeginInit();
        SuspendLayout();
        // 
        // tableLayoutPanel1
        // 
        tableLayoutPanel1.ColumnCount = 2;
        tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        tableLayoutPanel1.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        tableLayoutPanel1.Controls.Add(C_RequiresAdminValue, 1, 6);
        tableLayoutPanel1.Controls.Add(C_ShouldCacheDownloadUrlValue, 1, 5);
        tableLayoutPanel1.Controls.Add(C_IsArchiveValue, 1, 4);
        tableLayoutPanel1.Controls.Add(C_DownloadNameValue, 1, 3);
        tableLayoutPanel1.Controls.Add(C_CategoryValue, 1, 2);
        tableLayoutPanel1.Controls.Add(C_NameValue, 1, 1);
        tableLayoutPanel1.Controls.Add(C_KeyValue, 1, 0);
        tableLayoutPanel1.Controls.Add(C_KeyLabel, 0, 0);
        tableLayoutPanel1.Controls.Add(C_NameLabel, 0, 1);
        tableLayoutPanel1.Controls.Add(C_CategoryLabel, 0, 2);
        tableLayoutPanel1.Controls.Add(C_HomepageLabel, 0, 8);
        tableLayoutPanel1.Controls.Add(C_IconLabel, 0, 7);
        tableLayoutPanel1.Controls.Add(C_RequiresAdminLabel, 0, 6);
        tableLayoutPanel1.Controls.Add(C_ShouldCacheDownloadUrlLabel, 0, 5);
        tableLayoutPanel1.Controls.Add(C_IsArchiveLabel, 0, 4);
        tableLayoutPanel1.Controls.Add(C_DownloadNameLabel, 0, 3);
        tableLayoutPanel1.Controls.Add(C_HomepageLinkLabel, 1, 8);
        tableLayoutPanel1.Controls.Add(tableLayoutPanel2, 1, 7);
        tableLayoutPanel1.Dock = DockStyle.Fill;
        tableLayoutPanel1.Location = new Point(0, 0);
        tableLayoutPanel1.Name = "tableLayoutPanel1";
        tableLayoutPanel1.RowCount = 9;
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.RowStyles.Add(new RowStyle(SizeType.Percent, 11.1111107F));
        tableLayoutPanel1.Size = new Size(333, 369);
        tableLayoutPanel1.TabIndex = 0;
        // 
        // C_RequiresAdminValue
        // 
        C_RequiresAdminValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_RequiresAdminValue.AutoSize = true;
        C_RequiresAdminValue.Location = new Point(169, 246);
        C_RequiresAdminValue.Name = "C_RequiresAdminValue";
        C_RequiresAdminValue.Size = new Size(161, 41);
        C_RequiresAdminValue.TabIndex = 15;
        C_RequiresAdminValue.Text = "...";
        C_RequiresAdminValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_ShouldCacheDownloadUrlValue
        // 
        C_ShouldCacheDownloadUrlValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_ShouldCacheDownloadUrlValue.AutoSize = true;
        C_ShouldCacheDownloadUrlValue.Location = new Point(169, 205);
        C_ShouldCacheDownloadUrlValue.Name = "C_ShouldCacheDownloadUrlValue";
        C_ShouldCacheDownloadUrlValue.Size = new Size(161, 41);
        C_ShouldCacheDownloadUrlValue.TabIndex = 14;
        C_ShouldCacheDownloadUrlValue.Text = "...";
        C_ShouldCacheDownloadUrlValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_IsArchiveValue
        // 
        C_IsArchiveValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_IsArchiveValue.AutoSize = true;
        C_IsArchiveValue.Location = new Point(169, 164);
        C_IsArchiveValue.Name = "C_IsArchiveValue";
        C_IsArchiveValue.Size = new Size(161, 41);
        C_IsArchiveValue.TabIndex = 13;
        C_IsArchiveValue.Text = "...";
        C_IsArchiveValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_DownloadNameValue
        // 
        C_DownloadNameValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_DownloadNameValue.AutoSize = true;
        C_DownloadNameValue.Location = new Point(169, 123);
        C_DownloadNameValue.Name = "C_DownloadNameValue";
        C_DownloadNameValue.Size = new Size(161, 41);
        C_DownloadNameValue.TabIndex = 12;
        C_DownloadNameValue.Text = "...";
        C_DownloadNameValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_CategoryValue
        // 
        C_CategoryValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_CategoryValue.AutoSize = true;
        C_CategoryValue.Location = new Point(169, 82);
        C_CategoryValue.Name = "C_CategoryValue";
        C_CategoryValue.Size = new Size(161, 41);
        C_CategoryValue.TabIndex = 11;
        C_CategoryValue.Text = "...";
        C_CategoryValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_NameValue
        // 
        C_NameValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_NameValue.AutoSize = true;
        C_NameValue.Location = new Point(169, 41);
        C_NameValue.Name = "C_NameValue";
        C_NameValue.Size = new Size(161, 41);
        C_NameValue.TabIndex = 10;
        C_NameValue.Text = "...";
        C_NameValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_KeyValue
        // 
        C_KeyValue.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_KeyValue.AutoSize = true;
        C_KeyValue.Location = new Point(169, 0);
        C_KeyValue.Name = "C_KeyValue";
        C_KeyValue.Size = new Size(161, 41);
        C_KeyValue.TabIndex = 9;
        C_KeyValue.Text = "...";
        C_KeyValue.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_KeyLabel
        // 
        C_KeyLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_KeyLabel.AutoSize = true;
        C_KeyLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_KeyLabel.Location = new Point(3, 0);
        C_KeyLabel.Name = "C_KeyLabel";
        C_KeyLabel.Size = new Size(160, 41);
        C_KeyLabel.TabIndex = 0;
        C_KeyLabel.Text = "Key";
        C_KeyLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_NameLabel
        // 
        C_NameLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_NameLabel.AutoSize = true;
        C_NameLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_NameLabel.Location = new Point(3, 41);
        C_NameLabel.Name = "C_NameLabel";
        C_NameLabel.Size = new Size(160, 41);
        C_NameLabel.TabIndex = 1;
        C_NameLabel.Text = "Name";
        C_NameLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_CategoryLabel
        // 
        C_CategoryLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_CategoryLabel.AutoSize = true;
        C_CategoryLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_CategoryLabel.Location = new Point(3, 82);
        C_CategoryLabel.Name = "C_CategoryLabel";
        C_CategoryLabel.Size = new Size(160, 41);
        C_CategoryLabel.TabIndex = 2;
        C_CategoryLabel.Text = "Category";
        C_CategoryLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_HomepageLabel
        // 
        C_HomepageLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_HomepageLabel.AutoSize = true;
        C_HomepageLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_HomepageLabel.Location = new Point(3, 328);
        C_HomepageLabel.Name = "C_HomepageLabel";
        C_HomepageLabel.Size = new Size(160, 41);
        C_HomepageLabel.TabIndex = 7;
        C_HomepageLabel.Text = "Homepage";
        C_HomepageLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_IconLabel
        // 
        C_IconLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_IconLabel.AutoSize = true;
        C_IconLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_IconLabel.Location = new Point(3, 287);
        C_IconLabel.Name = "C_IconLabel";
        C_IconLabel.Size = new Size(160, 41);
        C_IconLabel.TabIndex = 6;
        C_IconLabel.Text = "Icons";
        C_IconLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_RequiresAdminLabel
        // 
        C_RequiresAdminLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_RequiresAdminLabel.AutoSize = true;
        C_RequiresAdminLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_RequiresAdminLabel.Location = new Point(3, 246);
        C_RequiresAdminLabel.Name = "C_RequiresAdminLabel";
        C_RequiresAdminLabel.Size = new Size(160, 41);
        C_RequiresAdminLabel.TabIndex = 5;
        C_RequiresAdminLabel.Text = "Requires Administrator?";
        C_RequiresAdminLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_ShouldCacheDownloadUrlLabel
        // 
        C_ShouldCacheDownloadUrlLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_ShouldCacheDownloadUrlLabel.AutoSize = true;
        C_ShouldCacheDownloadUrlLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_ShouldCacheDownloadUrlLabel.Location = new Point(3, 205);
        C_ShouldCacheDownloadUrlLabel.Name = "C_ShouldCacheDownloadUrlLabel";
        C_ShouldCacheDownloadUrlLabel.Size = new Size(160, 41);
        C_ShouldCacheDownloadUrlLabel.TabIndex = 4;
        C_ShouldCacheDownloadUrlLabel.Text = "Cache Download URL?";
        C_ShouldCacheDownloadUrlLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_IsArchiveLabel
        // 
        C_IsArchiveLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_IsArchiveLabel.AutoSize = true;
        C_IsArchiveLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_IsArchiveLabel.Location = new Point(3, 164);
        C_IsArchiveLabel.Name = "C_IsArchiveLabel";
        C_IsArchiveLabel.Size = new Size(160, 41);
        C_IsArchiveLabel.TabIndex = 3;
        C_IsArchiveLabel.Text = "Is Archive?";
        C_IsArchiveLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_DownloadNameLabel
        // 
        C_DownloadNameLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_DownloadNameLabel.AutoSize = true;
        C_DownloadNameLabel.Font = new Font("Segoe UI", 9F, FontStyle.Bold, GraphicsUnit.Point, 0);
        C_DownloadNameLabel.Location = new Point(3, 123);
        C_DownloadNameLabel.Name = "C_DownloadNameLabel";
        C_DownloadNameLabel.Size = new Size(160, 41);
        C_DownloadNameLabel.TabIndex = 8;
        C_DownloadNameLabel.Text = "Download Name";
        C_DownloadNameLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // C_HomepageLinkLabel
        // 
        C_HomepageLinkLabel.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
        C_HomepageLinkLabel.AutoSize = true;
        C_HomepageLinkLabel.Location = new Point(169, 328);
        C_HomepageLinkLabel.Name = "C_HomepageLinkLabel";
        C_HomepageLinkLabel.Size = new Size(161, 41);
        C_HomepageLinkLabel.TabIndex = 19;
        C_HomepageLinkLabel.TabStop = true;
        C_HomepageLinkLabel.Text = "...";
        C_HomepageLinkLabel.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // tableLayoutPanel2
        // 
        tableLayoutPanel2.ColumnCount = 2;
        tableLayoutPanel2.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        tableLayoutPanel2.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
        tableLayoutPanel2.Controls.Add(C_IconPictureBoxGrayscale, 1, 0);
        tableLayoutPanel2.Controls.Add(C_IconPictureBox, 0, 0);
        tableLayoutPanel2.Dock = DockStyle.Fill;
        tableLayoutPanel2.Location = new Point(166, 287);
        tableLayoutPanel2.Margin = new Padding(0);
        tableLayoutPanel2.Name = "tableLayoutPanel2";
        tableLayoutPanel2.RowCount = 1;
        tableLayoutPanel2.RowStyles.Add(new RowStyle(SizeType.Percent, 50F));
        tableLayoutPanel2.Size = new Size(167, 41);
        tableLayoutPanel2.TabIndex = 20;
        // 
        // C_IconPictureBoxGrayscale
        // 
        C_IconPictureBoxGrayscale.Anchor = AnchorStyles.None;
        C_IconPictureBoxGrayscale.Location = new Point(109, 4);
        C_IconPictureBoxGrayscale.Name = "C_IconPictureBoxGrayscale";
        C_IconPictureBoxGrayscale.Size = new Size(32, 32);
        C_IconPictureBoxGrayscale.SizeMode = PictureBoxSizeMode.CenterImage;
        C_IconPictureBoxGrayscale.TabIndex = 1;
        C_IconPictureBoxGrayscale.TabStop = false;
        // 
        // C_IconPictureBox
        // 
        C_IconPictureBox.Anchor = AnchorStyles.None;
        C_IconPictureBox.Location = new Point(25, 4);
        C_IconPictureBox.Name = "C_IconPictureBox";
        C_IconPictureBox.Size = new Size(32, 32);
        C_IconPictureBox.SizeMode = PictureBoxSizeMode.CenterImage;
        C_IconPictureBox.TabIndex = 0;
        C_IconPictureBox.TabStop = false;
        // 
        // SoftwareInfoForm
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        AutoSize = true;
        ClientSize = new Size(333, 369);
        Controls.Add(tableLayoutPanel1);
        FormBorderStyle = FormBorderStyle.FixedToolWindow;
        MaximizeBox = false;
        MinimizeBox = false;
        Name = "SoftwareInfoForm";
        StartPosition = FormStartPosition.CenterParent;
        Text = "SoftwareInfoForm";
        tableLayoutPanel1.ResumeLayout(false);
        tableLayoutPanel1.PerformLayout();
        tableLayoutPanel2.ResumeLayout(false);
        ((ISupportInitialize)C_IconPictureBoxGrayscale).EndInit();
        ((ISupportInitialize)C_IconPictureBox).EndInit();
        ResumeLayout(false);
    }

    #endregion

    private TableLayoutPanel tableLayoutPanel1;
    private Label C_KeyLabel;
    private Label C_NameLabel;
    private Label C_CategoryLabel;
    private Label C_IsArchiveLabel;
    private Label C_ShouldCacheDownloadUrlLabel;
    private Label C_RequiresAdminLabel;
    private Label C_IconLabel;
    private Label C_HomepageLabel;
    private Label C_DownloadNameLabel;
    private Label C_KeyValue;
    private Label C_NameValue;
    private Label C_CategoryValue;
    private Label C_DownloadNameValue;
    private Label C_IsArchiveValue;
    private Label C_ShouldCacheDownloadUrlValue;
    private Label C_RequiresAdminValue;
    private LinkLabel C_HomepageLinkLabel;
    private TableLayoutPanel tableLayoutPanel2;
    private PictureBox C_IconPictureBox;
    private PictureBox C_IconPictureBoxGrayscale;
}

