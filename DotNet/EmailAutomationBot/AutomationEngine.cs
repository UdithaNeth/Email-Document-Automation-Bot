using System;
using System.Diagnostics;
using System.IO;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace EmailAutomationBot
{
    /// <summary>
    /// Manages Python script execution, process lifecycle, and output capture
    /// </summary>
    public class AutomationEngine
    {
        private Process? pythonProcess;
        private CancellationTokenSource? cancellationTokenSource;
        private readonly string pythonScriptPath;
        private readonly string pythonExecutable;

        /// <summary>
        /// Event raised when output is received from Python script
        /// </summary>
        public event EventHandler<string>? OutputReceived;

        /// <summary>
        /// Event raised when an error is received from Python script
        /// </summary>
        public event EventHandler<string>? ErrorReceived;

        /// <summary>
        /// Event raised when automation execution completes
        /// </summary>
        public event EventHandler<bool>? ExecutionCompleted;

        /// <summary>
        /// Indicates whether automation is currently running
        /// </summary>
        public bool IsRunning => pythonProcess != null && !pythonProcess.HasExited;

        public AutomationEngine()
        {
            // Determine Python script path (relative to application directory)
            string baseDir = AppDomain.CurrentDomain.BaseDirectory;
            
            // Try to find the Python folder - handle both debug/release builds and different directory structures
            string[] possiblePaths = {
                Path.GetFullPath(Path.Combine(baseDir, "..", "..", "..", "..", "..", "Python", "main.py")),  // From bin/Debug/net8.0-windows
                Path.GetFullPath(Path.Combine(baseDir, "..", "..", "..", "..", "Python", "main.py")),       // Alternative
                Path.GetFullPath(Path.Combine(baseDir, "..", "..", "..", "Python", "main.py")),             // Alternative
                Path.GetFullPath(Path.Combine(baseDir, "Python", "main.py"))                                 // Same level
            };
            
            pythonScriptPath = "";
            foreach (string path in possiblePaths)
            {
                if (File.Exists(path))
                {
                    pythonScriptPath = path;
                    break;
                }
            }
            
            // If still not found, try searching from project root
            if (string.IsNullOrEmpty(pythonScriptPath))
            {
                string projectRoot = Path.GetFullPath(Path.Combine(baseDir, "..", "..", "..", "..", ".."));
                string searchPath = Path.Combine(projectRoot, "Python", "main.py");
                if (File.Exists(searchPath))
                {
                    pythonScriptPath = searchPath;
                }
            }

            // Use system Python executable
            pythonExecutable = FindPythonExecutable();
        }

        /// <summary>
        /// Locate Python executable on the system
        /// </summary>
        private string FindPythonExecutable()
        {
            // Try common Python executable names
            string[] pythonNames = { "python", "python3", "py" };

            foreach (string name in pythonNames)
            {
                try
                {
                    var testProcess = new Process
                    {
                        StartInfo = new ProcessStartInfo
                        {
                            FileName = name,
                            Arguments = "--version",
                            UseShellExecute = false,
                            RedirectStandardOutput = true,
                            RedirectStandardError = true,
                            CreateNoWindow = true
                        }
                    };

                    testProcess.Start();
                    testProcess.WaitForExit(2000);

                    if (testProcess.ExitCode == 0)
                    {
                        return name;
                    }
                }
                catch
                {
                    // Continue to next option
                }
            }

            return "python"; // Default fallback
        }

        /// <summary>
        /// Start automation execution asynchronously
        /// </summary>
        public async Task<bool> StartAutomationAsync()
        {
            if (IsRunning)
            {
                OnOutputReceived("Automation is already running.");
                return false;
            }

            if (!File.Exists(pythonScriptPath))
            {
                OnErrorReceived($"Python script not found at: {pythonScriptPath}");
                return false;
            }

            try
            {
                // Create cancellation token for stopping automation
                cancellationTokenSource = new CancellationTokenSource();

                // Configure Python process
                pythonProcess = new Process
                {
                    StartInfo = new ProcessStartInfo
                    {
                        FileName = pythonExecutable,
                        Arguments = $"\"{pythonScriptPath}\"",
                        WorkingDirectory = Path.GetDirectoryName(pythonScriptPath),
                        UseShellExecute = false,
                        RedirectStandardOutput = true,
                        RedirectStandardError = true,
                        RedirectStandardInput = true,
                        CreateNoWindow = true,
                        StandardOutputEncoding = System.Text.Encoding.UTF8,
                        StandardErrorEncoding = System.Text.Encoding.UTF8
                    },
                    EnableRaisingEvents = true
                };

                // Attach output handlers
                pythonProcess.OutputDataReceived += (sender, e) =>
                {
                    if (!string.IsNullOrEmpty(e.Data))
                    {
                        OnOutputReceived(e.Data);
                    }
                };

                pythonProcess.ErrorDataReceived += (sender, e) =>
                {
                    if (!string.IsNullOrEmpty(e.Data))
                    {
                        OnErrorReceived(e.Data);
                    }
                };

                pythonProcess.Exited += (sender, e) =>
                {
                    bool success = pythonProcess?.ExitCode == 0;
                    OnExecutionCompleted(success);
                };

                // Start process
                OnOutputReceived($"Starting automation with Python at: {pythonExecutable}");
                OnOutputReceived($"Script path: {pythonScriptPath}");
                OnOutputReceived("----------------------------------------");

                pythonProcess.Start();
                pythonProcess.BeginOutputReadLine();
                pythonProcess.BeginErrorReadLine();

                // Wait for process completion
                await Task.Run(() => pythonProcess.WaitForExit(), cancellationTokenSource.Token);

                return pythonProcess.ExitCode == 0;
            }
            catch (Exception ex)
            {
                OnErrorReceived($"Failed to start automation: {ex.Message}");
                return false;
            }
        }

        /// <summary>
        /// Stop running automation
        /// </summary>
        public void StopAutomation()
        {
            if (!IsRunning)
            {
                OnOutputReceived("No automation is currently running.");
                return;
            }

            try
            {
                OnOutputReceived("Stopping automation...");

                // Cancel token and kill process
                cancellationTokenSource?.Cancel();

                if (pythonProcess != null && !pythonProcess.HasExited)
                {
                    pythonProcess.Kill(entireProcessTree: true);
                    pythonProcess.WaitForExit(3000);
                }

                OnOutputReceived("Automation stopped.");
            }
            catch (Exception ex)
            {
                OnErrorReceived($"Error stopping automation: {ex.Message}");
            }
            finally
            {
                CleanupProcess();
            }
        }

        /// <summary>
        /// Clean up process resources
        /// </summary>
        private void CleanupProcess()
        {
            cancellationTokenSource?.Dispose();
            cancellationTokenSource = null;

            pythonProcess?.Dispose();
            pythonProcess = null;
        }

        /// <summary>
        /// Get path to log file
        /// </summary>
        public string GetLogFilePath()
        {
            string baseDir = Path.GetDirectoryName(pythonScriptPath)!;
            return Path.Combine(baseDir, "..", "logs", "bot.log");
        }

        protected virtual void OnOutputReceived(string message)
        {
            OutputReceived?.Invoke(this, message);
        }

        protected virtual void OnErrorReceived(string message)
        {
            ErrorReceived?.Invoke(this, message);
        }

        protected virtual void OnExecutionCompleted(bool success)
        {
            CleanupProcess();
            ExecutionCompleted?.Invoke(this, success);
        }
    }
}
