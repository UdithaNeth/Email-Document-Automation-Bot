using System;
using System.Windows.Forms;

namespace EmailAutomationBot
{
    /// <summary>
    /// Main entry point for the Email & Document Automation Bot UI
    /// </summary>
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
