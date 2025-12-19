namespace EmailAutomationBot
{
    partial class MainForm
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

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnRunAutomation = new System.Windows.Forms.Button();
            this.btnStopAutomation = new System.Windows.Forms.Button();
            this.btnViewLogs = new System.Windows.Forms.Button();
            this.txtOutput = new System.Windows.Forms.TextBox();
            this.lblStatus = new System.Windows.Forms.Label();
            this.statusStrip = new System.Windows.Forms.StatusStrip();
            this.statusLabel = new System.Windows.Forms.ToolStripStatusLabel();
            this.panelButtons = new System.Windows.Forms.Panel();
            this.btnClearOutput = new System.Windows.Forms.Button();
            this.statusStrip.SuspendLayout();
            this.panelButtons.SuspendLayout();
            this.SuspendLayout();
            // 
            // btnRunAutomation
            // 
            this.btnRunAutomation.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(0)))), ((int)(((byte)(122)))), ((int)(((byte)(204)))));
            this.btnRunAutomation.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnRunAutomation.Font = new System.Drawing.Font("Segoe UI", 10F, System.Drawing.FontStyle.Bold);
            this.btnRunAutomation.ForeColor = System.Drawing.Color.White;
            this.btnRunAutomation.Location = new System.Drawing.Point(15, 15);
            this.btnRunAutomation.Name = "btnRunAutomation";
            this.btnRunAutomation.Size = new System.Drawing.Size(150, 40);
            this.btnRunAutomation.TabIndex = 0;
            this.btnRunAutomation.Text = "▶ Run Automation";
            this.btnRunAutomation.UseVisualStyleBackColor = false;
            this.btnRunAutomation.Click += new System.EventHandler(this.btnRunAutomation_Click);
            // 
            // btnStopAutomation
            // 
            this.btnStopAutomation.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(232)))), ((int)(((byte)(17)))), ((int)(((byte)(35)))));
            this.btnStopAutomation.Enabled = false;
            this.btnStopAutomation.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnStopAutomation.Font = new System.Drawing.Font("Segoe UI", 10F, System.Drawing.FontStyle.Bold);
            this.btnStopAutomation.ForeColor = System.Drawing.Color.White;
            this.btnStopAutomation.Location = new System.Drawing.Point(180, 15);
            this.btnStopAutomation.Name = "btnStopAutomation";
            this.btnStopAutomation.Size = new System.Drawing.Size(150, 40);
            this.btnStopAutomation.TabIndex = 1;
            this.btnStopAutomation.Text = "■ Stop Automation";
            this.btnStopAutomation.UseVisualStyleBackColor = false;
            this.btnStopAutomation.Click += new System.EventHandler(this.btnStopAutomation_Click);
            // 
            // btnViewLogs
            // 
            this.btnViewLogs.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(106)))), ((int)(((byte)(90)))), ((int)(((byte)(205)))));
            this.btnViewLogs.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnViewLogs.Font = new System.Drawing.Font("Segoe UI", 10F, System.Drawing.FontStyle.Bold);
            this.btnViewLogs.ForeColor = System.Drawing.Color.White;
            this.btnViewLogs.Location = new System.Drawing.Point(345, 15);
            this.btnViewLogs.Name = "btnViewLogs";
            this.btnViewLogs.Size = new System.Drawing.Size(150, 40);
            this.btnViewLogs.TabIndex = 2;
            this.btnViewLogs.Text = "📄 View Logs";
            this.btnViewLogs.UseVisualStyleBackColor = false;
            this.btnViewLogs.Click += new System.EventHandler(this.btnViewLogs_Click);
            // 
            // txtOutput
            // 
            this.txtOutput.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(30)))), ((int)(((byte)(30)))), ((int)(((byte)(30)))));
            this.txtOutput.Dock = System.Windows.Forms.DockStyle.Fill;
            this.txtOutput.Font = new System.Drawing.Font("Consolas", 9F);
            this.txtOutput.ForeColor = System.Drawing.Color.LightGray;
            this.txtOutput.Location = new System.Drawing.Point(0, 110);
            this.txtOutput.Multiline = true;
            this.txtOutput.Name = "txtOutput";
            this.txtOutput.ReadOnly = true;
            this.txtOutput.ScrollBars = System.Windows.Forms.ScrollBars.Both;
            this.txtOutput.Size = new System.Drawing.Size(784, 415);
            this.txtOutput.TabIndex = 3;
            this.txtOutput.WordWrap = false;
            // 
            // lblStatus
            // 
            this.lblStatus.AutoSize = true;
            this.lblStatus.Font = new System.Drawing.Font("Segoe UI", 11F, System.Drawing.FontStyle.Bold);
            this.lblStatus.Location = new System.Drawing.Point(15, 70);
            this.lblStatus.Name = "lblStatus";
            this.lblStatus.Size = new System.Drawing.Size(60, 20);
            this.lblStatus.TabIndex = 4;
            this.lblStatus.Text = "Ready";
            // 
            // statusStrip
            // 
            this.statusStrip.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.statusLabel});
            this.statusStrip.Location = new System.Drawing.Point(0, 525);
            this.statusStrip.Name = "statusStrip";
            this.statusStrip.Size = new System.Drawing.Size(784, 22);
            this.statusStrip.TabIndex = 5;
            this.statusStrip.Text = "statusStrip1";
            // 
            // statusLabel
            // 
            this.statusLabel.Name = "statusLabel";
            this.statusLabel.Size = new System.Drawing.Size(204, 17);
            this.statusLabel.Text = "Email && Document Automation Bot v1.0";
            // 
            // panelButtons
            // 
            this.panelButtons.Controls.Add(this.btnClearOutput);
            this.panelButtons.Controls.Add(this.btnRunAutomation);
            this.panelButtons.Controls.Add(this.lblStatus);
            this.panelButtons.Controls.Add(this.btnStopAutomation);
            this.panelButtons.Controls.Add(this.btnViewLogs);
            this.panelButtons.Dock = System.Windows.Forms.DockStyle.Top;
            this.panelButtons.Location = new System.Drawing.Point(0, 0);
            this.panelButtons.Name = "panelButtons";
            this.panelButtons.Size = new System.Drawing.Size(784, 110);
            this.panelButtons.TabIndex = 6;
            // 
            // btnClearOutput
            // 
            this.btnClearOutput.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(70)))), ((int)(((byte)(70)))), ((int)(((byte)(70)))));
            this.btnClearOutput.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.btnClearOutput.Font = new System.Drawing.Font("Segoe UI", 10F, System.Drawing.FontStyle.Bold);
            this.btnClearOutput.ForeColor = System.Drawing.Color.White;
            this.btnClearOutput.Location = new System.Drawing.Point(510, 15);
            this.btnClearOutput.Name = "btnClearOutput";
            this.btnClearOutput.Size = new System.Drawing.Size(150, 40);
            this.btnClearOutput.TabIndex = 5;
            this.btnClearOutput.Text = "🗑 Clear Output";
            this.btnClearOutput.UseVisualStyleBackColor = false;
            this.btnClearOutput.Click += new System.EventHandler(this.btnClearOutput_Click);
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(784, 547);
            this.Controls.Add(this.txtOutput);
            this.Controls.Add(this.panelButtons);
            this.Controls.Add(this.statusStrip);
            this.MinimumSize = new System.Drawing.Size(800, 586);
            this.Name = "MainForm";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "Email & Document Automation Bot";
            this.statusStrip.ResumeLayout(false);
            this.statusStrip.PerformLayout();
            this.panelButtons.ResumeLayout(false);
            this.panelButtons.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button btnRunAutomation;
        private System.Windows.Forms.Button btnStopAutomation;
        private System.Windows.Forms.Button btnViewLogs;
        private System.Windows.Forms.TextBox txtOutput;
        private System.Windows.Forms.Label lblStatus;
        private System.Windows.Forms.StatusStrip statusStrip;
        private System.Windows.Forms.ToolStripStatusLabel statusLabel;
        private System.Windows.Forms.Panel panelButtons;
        private System.Windows.Forms.Button btnClearOutput;
    }
}
