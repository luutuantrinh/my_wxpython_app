import wx
import wx.adv

class SplashScreen(wx.adv.SplashScreen):
    def __init__(self, image_path, duration, callback):
        image = wx.Image(image_path, wx.BITMAP_TYPE_PNG)

        # Thay đổi kích thước hình ảnh theo tỷ lệ
        width = image.GetWidth()
        height = image.GetHeight()
        max_dimension = 300  # Kích thước tối đa cho chiều rộng hoặc chiều cao

        if width > height:
            new_width = max_dimension
            new_height = int(max_dimension * height / width)
        else:
            new_height = max_dimension
            new_width = int(max_dimension * width / height)

        image = image.Scale(new_width, new_height, wx.IMAGE_QUALITY_HIGH)
        bitmap = wx.Bitmap(image)

        splash_style = wx.adv.SPLASH_CENTRE_ON_SCREEN | wx.adv.SPLASH_TIMEOUT
        wx.adv.SplashScreen.__init__(self, bitmap, splash_style, duration, None)
        self.callback = callback
        self.Bind(wx.EVT_CLOSE, self.on_close)
        wx.Yield()

    def on_close(self, event):
        self.Hide()
        self.callback()
        event.Skip()
