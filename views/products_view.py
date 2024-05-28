import wx

class ProductsView(wx.Panel):
    def __init__(self, parent):
        super(ProductsView, self).__init__(parent)

        sizer = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(self, label="Products content is displayed here")
        sizer.Add(label, 0, wx.ALL | wx.CENTER, 10)

        self.SetSizer(sizer)
