import wx

class OrdersView(wx.Panel):
    def __init__(self, parent):
        super(OrdersView, self).__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Orders content is displayed here")
        sizer.Add(label, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
