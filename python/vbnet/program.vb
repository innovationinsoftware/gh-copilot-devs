Imports System.Windows.Forms

Public Class MainForm
    Inherits Form

    Private Sub New()
        ' Set the form properties
        Me.Text = "Hello App"
        Me.StartPosition = FormStartPosition.CenterScreen
        Me.Size = New Drawing.Size(300, 200)

        ' Create and configure the button
        Dim helloButton As New Button()
        helloButton.Text = "Hello"
        helloButton.Size = New Drawing.Size(100, 50)
        helloButton.Location = New Drawing.Point((Me.ClientSize.Width - helloButton.Width) \ 2, (Me.ClientSize.Height - helloButton.Height) \ 2)
        helloButton.Anchor = AnchorStyles.None

        ' Add the click event handler
        AddHandler helloButton.Click, AddressOf HelloButton_Click

        ' Add the button to the form
        Me.Controls.Add(helloButton)
    End Sub

    Private Sub HelloButton_Click(sender As Object, e As EventArgs)
        MessageBox.Show("Hello, World!")
    End Sub

    <STAThread>
    Public Shared Sub Main()
        Application.EnableVisualStyles()
        Application.SetCompatibleTextRenderingDefault(False)
        Application.Run(New MainForm())
    End Sub
End Class


