using System.ComponentModel;

namespace CarePackage.Forms;

partial class SuggestionForm
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
        c_CategorySelectionComboBox = new ComboBox();
        c_LaunchUrlButton = new Button();
        label1 = new Label();
        SuspendLayout();
        // 
        // c_CategorySelectionComboBox
        // 
        c_CategorySelectionComboBox.DropDownStyle = ComboBoxStyle.DropDownList;
        c_CategorySelectionComboBox.FormattingEnabled = true;
        c_CategorySelectionComboBox.Location = new Point(12, 33);
        c_CategorySelectionComboBox.Name = "c_CategorySelectionComboBox";
        c_CategorySelectionComboBox.Size = new Size(175, 23);
        c_CategorySelectionComboBox.TabIndex = 0;
        // 
        // c_LaunchUrlButton
        // 
        c_LaunchUrlButton.AutoSize = true;
        c_LaunchUrlButton.Enabled = false;
        c_LaunchUrlButton.Location = new Point(193, 32);
        c_LaunchUrlButton.Name = "c_LaunchUrlButton";
        c_LaunchUrlButton.Size = new Size(75, 25);
        c_LaunchUrlButton.TabIndex = 1;
        c_LaunchUrlButton.Text = "&Continue";
        c_LaunchUrlButton.UseVisualStyleBackColor = true;
        // 
        // label1
        // 
        label1.AutoSize = true;
        label1.Location = new Point(12, 12);
        label1.Margin = new Padding(3);
        label1.Name = "label1";
        label1.Size = new Size(105, 15);
        label1.TabIndex = 2;
        label1.Text = "Choose a category";
        label1.TextAlign = ContentAlignment.MiddleCenter;
        // 
        // SuggestionForm
        // 
        AutoScaleDimensions = new SizeF(7F, 15F);
        AutoScaleMode = AutoScaleMode.Font;
        ClientSize = new Size(279, 69);
        Controls.Add(label1);
        Controls.Add(c_LaunchUrlButton);
        Controls.Add(c_CategorySelectionComboBox);
        FormBorderStyle = FormBorderStyle.FixedSingle;
        MaximizeBox = false;
        MinimizeBox = false;
        Name = "SuggestionForm";
        ShowIcon = false;
        ShowInTaskbar = false;
        SizeGripStyle = SizeGripStyle.Hide;
        StartPosition = FormStartPosition.CenterParent;
        Text = "Suggest a program";
        ResumeLayout(false);
        PerformLayout();
    }

    #endregion

    private ComboBox c_CategorySelectionComboBox;
    private Button c_LaunchUrlButton;
    private Label label1;
}

