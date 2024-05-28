import wx

class MainAppView(wx.Frame):
    def __init__(self, parent, title):
        super(MainAppView, self).__init__(parent, title=title, size=(600, 400))
        self.init_ui()
        self.Center()

    def init_ui(self):
        panel = wx.Panel(self)

        sizer = wx.BoxSizer(wx.VERTICAL)
        welcome_text = wx.StaticText(panel, label="Welcome to the Main Application", style=wx.ALIGN_CENTER)
        font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        welcome_text.SetFont(font)
        welcome_text.SetForegroundColour(wx.Colour(0, 102, 204))

        sizer.Add(welcome_text, 0, wx.ALL | wx.EXPAND, 15)

        panel.SetSizer(sizer)
