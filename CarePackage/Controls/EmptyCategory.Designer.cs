namespace CarePackage.Controls
{
    partial class EmptyCategory
    {
        /// <summary> 
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

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
            c_MainTableLayout = new TableLayoutPanel();
            c_CenterTableLayout = new TableLayoutPanel();
            c_HeadingTableLayout = new TableLayoutPanel();
            c_Heading = new Label();
            c_Subheading = new LinkLabel();
            c_WarningImage = new InterpolatedPictureBox();
            c_MainTableLayout.SuspendLayout();
            c_CenterTableLayout.SuspendLayout();
            c_HeadingTableLayout.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)c_WarningImage).BeginInit();
            SuspendLayout();
            // 
            // c_MainTableLayout
            // 
            c_MainTableLayout.ColumnCount = 3;
            c_MainTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            c_MainTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 50F));
            c_MainTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 25F));
            c_MainTableLayout.Controls.Add(c_CenterTableLayout, 1, 1);
            c_MainTableLayout.Dock = DockStyle.Fill;
            c_MainTableLayout.GrowStyle = TableLayoutPanelGrowStyle.FixedSize;
            c_MainTableLayout.Location = new Point(0, 0);
            c_MainTableLayout.Name = "c_MainTableLayout";
            c_MainTableLayout.RowCount = 3;
            c_MainTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 43.5967255F));
            c_MainTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 12.80654F));
            c_MainTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 43.5967369F));
            c_MainTableLayout.Size = new Size(1237, 652);
            c_MainTableLayout.TabIndex = 0;
            // 
            // c_CenterTableLayout
            // 
            c_CenterTableLayout.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            c_CenterTableLayout.ColumnCount = 2;
            c_CenterTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 15.7894735F));
            c_CenterTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 84.2105255F));
            c_CenterTableLayout.Controls.Add(c_HeadingTableLayout, 1, 0);
            c_CenterTableLayout.Controls.Add(c_WarningImage, 0, 0);
            c_CenterTableLayout.Location = new Point(309, 284);
            c_CenterTableLayout.Margin = new Padding(0);
            c_CenterTableLayout.Name = "c_CenterTableLayout";
            c_CenterTableLayout.RowCount = 1;
            c_CenterTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 100F));
            c_CenterTableLayout.Size = new Size(618, 83);
            c_CenterTableLayout.TabIndex = 0;
            // 
            // c_HeadingTableLayout
            // 
            c_HeadingTableLayout.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            c_HeadingTableLayout.ColumnCount = 1;
            c_HeadingTableLayout.ColumnStyles.Add(new ColumnStyle(SizeType.Percent, 100F));
            c_HeadingTableLayout.Controls.Add(c_Heading, 0, 0);
            c_HeadingTableLayout.Controls.Add(c_Subheading, 0, 1);
            c_HeadingTableLayout.Location = new Point(97, 0);
            c_HeadingTableLayout.Margin = new Padding(0);
            c_HeadingTableLayout.Name = "c_HeadingTableLayout";
            c_HeadingTableLayout.RowCount = 2;
            c_HeadingTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 60F));
            c_HeadingTableLayout.RowStyles.Add(new RowStyle(SizeType.Percent, 40F));
            c_HeadingTableLayout.Size = new Size(521, 83);
            c_HeadingTableLayout.TabIndex = 0;
            // 
            // c_Heading
            // 
            c_Heading.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            c_Heading.AutoSize = true;
            c_Heading.Font = new Font("Segoe UI Semibold", 12F, FontStyle.Bold, GraphicsUnit.Point, 0);
            c_Heading.Location = new Point(3, 3);
            c_Heading.Margin = new Padding(3);
            c_Heading.Name = "c_Heading";
            c_Heading.Size = new Size(515, 43);
            c_Heading.TabIndex = 0;
            c_Heading.Text = "There are no programs in this category yet.";
            c_Heading.TextAlign = ContentAlignment.MiddleLeft;
            // 
            // c_Subheading
            // 
            c_Subheading.ActiveLinkColor = SystemColors.HotTrack;
            c_Subheading.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            c_Subheading.AutoSize = true;
            c_Subheading.LinkArea = new LinkArea(20, 4);
            c_Subheading.LinkColor = SystemColors.Highlight;
            c_Subheading.Location = new Point(3, 52);
            c_Subheading.Margin = new Padding(3);
            c_Subheading.Name = "c_Subheading";
            c_Subheading.Size = new Size(515, 28);
            c_Subheading.TabIndex = 1;
            c_Subheading.TabStop = true;
            c_Subheading.Text = "You can suggest one here!";
            c_Subheading.TextAlign = ContentAlignment.MiddleLeft;
            c_Subheading.UseCompatibleTextRendering = true;
            // 
            // c_WarningImage
            // 
            c_WarningImage.Anchor = AnchorStyles.Top | AnchorStyles.Bottom | AnchorStyles.Left | AnchorStyles.Right;
            c_WarningImage.Image = Resources.Images.warning;
            c_WarningImage.InterpolationMode = System.Drawing.Drawing2D.InterpolationMode.High;
            c_WarningImage.Location = new Point(0, 0);
            c_WarningImage.Margin = new Padding(0);
            c_WarningImage.Name = "c_WarningImage";
            c_WarningImage.Size = new Size(97, 83);
            c_WarningImage.SizeMode = PictureBoxSizeMode.Zoom;
            c_WarningImage.TabIndex = 1;
            c_WarningImage.TabStop = false;
            // 
            // EmptyCategory
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            BackColor = Color.White;
            Controls.Add(c_MainTableLayout);
            Name = "EmptyCategory";
            Size = new Size(1237, 652);
            c_MainTableLayout.ResumeLayout(false);
            c_CenterTableLayout.ResumeLayout(false);
            c_HeadingTableLayout.ResumeLayout(false);
            c_HeadingTableLayout.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)c_WarningImage).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private TableLayoutPanel c_MainTableLayout;
        private TableLayoutPanel c_CenterTableLayout;
        private TableLayoutPanel c_HeadingTableLayout;
        private Label c_Heading;
        private LinkLabel c_Subheading;
        private InterpolatedPictureBox c_WarningImage;
    }
}
