import wx

class DashboardView(wx.Panel):
    def __init__(self, parent):
        super(DashboardView, self).__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Dashboard content is displayed here")
        sizer.Add(label, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
