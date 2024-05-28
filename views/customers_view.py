import wx

class CustomersView(wx.Panel):
    def __init__(self, parent):
        super(CustomersView, self).__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Customers content is displayed here")
        sizer.Add(label, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
