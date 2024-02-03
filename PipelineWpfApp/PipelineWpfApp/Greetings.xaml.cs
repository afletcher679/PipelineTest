using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace PipelineWpfApp
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void DisplayButton_Click(object sender, RoutedEventArgs e)
        {
            if (HelloButton.IsChecked == true)
            {
                ShowBox.Text = "Hello!";
            } 
            else if (GoodbyeButton.IsChecked == true)
            {
                ShowBox.Text = "Goodbye!";
            }
        }
    }
}