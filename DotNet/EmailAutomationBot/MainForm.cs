using System;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Windows.Forms;

namespace EmailAutomationBot
{
    /// <summary>
    /// Main form for Email & Document Automation Bot
    /// Provides UI for running automation, stopping execution, and viewing logs
    /// </summary>
    public partial class MainForm : Form
    {
        private readonly AutomationEngine automationEngine;

        public MainForm()
        {
            InitializeComponent();
            
            // Initialize automation engine
            automationEngine = new AutomationEngine();
            
            // Subscribe to engine events
            automationEngine.OutputReceived += OnAutomationOutput;
            automationEngine.ErrorReceived += OnAutomationError;
            automationEngine.ExecutionCompleted += OnAutomationCompleted;
            
            // Set initial UI state
            UpdateStatusLabel("Ready to start automation", Color.Green);
            AppendOutput("=== Email & Document Automation Bot ===");
            AppendOutput("Configure your email credentials in environment variables:");
            AppendOutput("  EMAIL_HOST, EMAIL_USER, EMAIL_PASSWORD");
            AppendOutput("");
            AppendOutput("Click 'Run Automation' to start processing emails.");
            AppendOutput("========================================");
            AppendOutput("");
        }

        /// <summary>
        /// Handle Run Automation button click
        /// </summary>
        private async void btnRunAutomation_Click(object sender, EventArgs e)
        {
            try
            {
                // Update UI state
                btnRunAutomation.Enabled = false;
                btnStopAutomation.Enabled = true;
                UpdateStatusLabel("Running automation...", Color.Orange);
                
                AppendOutput("");
                AppendOutput($"[{DateTime.Now:HH:mm:ss}] Starting automation...");
                
                // Start automation asynchronously
                bool success = await automationEngine.StartAutomationAsync();
                
                if (!success && !automationEngine.IsRunning)
                {
                    // Failed to start
                    UpdateStatusLabel("Failed to start automation", Color.Red);
                    btnRunAutomation.Enabled = true;
                    btnStopAutomation.Enabled = false;
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    $"Failed to start automation: {ex.Message}",
                    "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error
                );
                
                btnRunAutomation.Enabled = true;
                btnStopAutomation.Enabled = false;
                UpdateStatusLabel("Error starting automation", Color.Red);
            }
        }

        /// <summary>
        /// Handle Stop Automation button click
        /// </summary>
        private void btnStopAutomation_Click(object sender, EventArgs e)
        {
            try
            {
                AppendOutput("");
                AppendOutput($"[{DateTime.Now:HH:mm:ss}] Stopping automation...");
                
                automationEngine.StopAutomation();
                
                // Update UI state
                btnRunAutomation.Enabled = true;
                btnStopAutomation.Enabled = false;
                UpdateStatusLabel("Automation stopped", Color.Gray);
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    $"Error stopping automation: {ex.Message}",
                    "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error
                );
            }
        }

        /// <summary>
        /// Handle View Logs button click
        /// Opens log file in default text editor
        /// </summary>
        private void btnViewLogs_Click(object sender, EventArgs e)
        {
            try
            {
                string logPath = automationEngine.GetLogFilePath();
                string fullLogPath = Path.GetFullPath(logPath);
                
                if (File.Exists(fullLogPath))
                {
                    // Open log file with default application
                    Process.Start(new ProcessStartInfo
                    {
                        FileName = fullLogPath,
                        UseShellExecute = true
                    });
                    
                    AppendOutput($"Opening log file: {fullLogPath}");
                }
                else
                {
                    MessageBox.Show(
                        $"Log file not found at:\n{fullLogPath}\n\nRun the automation at least once to generate logs.",
                        "Log File Not Found",
                        MessageBoxButtons.OK,
                        MessageBoxIcon.Information
                    );
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(
                    $"Failed to open log file: {ex.Message}",
                    "Error",
                    MessageBoxButtons.OK,
                    MessageBoxIcon.Error
                );
            }
        }

        /// <summary>
        /// Handle Clear Output button click
        /// </summary>
        private void btnClearOutput_Click(object sender, EventArgs e)
        {
            txtOutput.Clear();
            AppendOutput($"[{DateTime.Now:HH:mm:ss}] Output cleared.");
        }

        /// <summary>
        /// Handle output received from automation engine
        /// </summary>
        private void OnAutomationOutput(object? sender, string message)
        {
            // Ensure UI update happens on UI thread
            if (InvokeRequired)
            {
                Invoke(new Action<object?, string>(OnAutomationOutput), sender, message);
                return;
            }
            
            AppendOutput(message);
        }

        /// <summary>
        /// Handle error output received from automation engine
        /// </summary>
        private void OnAutomationError(object? sender, string message)
        {
            // Ensure UI update happens on UI thread
            if (InvokeRequired)
            {
                Invoke(new Action<object?, string>(OnAutomationError), sender, message);
                return;
            }
            
            AppendOutput($"ERROR: {message}", Color.Red);
        }

        /// <summary>
        /// Handle automation completion
        /// </summary>
        private void OnAutomationCompleted(object? sender, bool success)
        {
            // Ensure UI update happens on UI thread
            if (InvokeRequired)
            {
                Invoke(new Action<object?, bool>(OnAutomationCompleted), sender, success);
                return;
            }
            
            // Update UI state
            btnRunAutomation.Enabled = true;
            btnStopAutomation.Enabled = false;
            
            if (success)
            {
                UpdateStatusLabel("Automation completed successfully", Color.Green);
                AppendOutput("");
                AppendOutput($"[{DateTime.Now:HH:mm:ss}] ✓ Automation completed successfully!");
            }
            else
            {
                UpdateStatusLabel("Automation failed", Color.Red);
                AppendOutput("");
                AppendOutput($"[{DateTime.Now:HH:mm:ss}] ✗ Automation failed. Check logs for details.");
            }
        }

        /// <summary>
        /// Append text to output console
        /// </summary>
        private void AppendOutput(string message, Color? color = null)
        {
            txtOutput.AppendText(message + Environment.NewLine);
            
            // Auto-scroll to bottom
            txtOutput.SelectionStart = txtOutput.Text.Length;
            txtOutput.ScrollToCaret();
        }

        /// <summary>
        /// Update status label with color
        /// </summary>
        private void UpdateStatusLabel(string text, Color color)
        {
            lblStatus.Text = $"Status: {text}";
            lblStatus.ForeColor = color;
        }

        /// <summary>
        /// Form closing event - ensure automation is stopped
        /// </summary>
        protected override void OnFormClosing(FormClosingEventArgs e)
        {
            if (automationEngine.IsRunning)
            {
                var result = MessageBox.Show(
                    "Automation is still running. Do you want to stop it and exit?",
                    "Confirm Exit",
                    MessageBoxButtons.YesNo,
                    MessageBoxIcon.Question
                );
                
                if (result == DialogResult.Yes)
                {
                    automationEngine.StopAutomation();
                }
                else
                {
                    e.Cancel = true;
                }
            }
            
            base.OnFormClosing(e);
        }
    }
}
