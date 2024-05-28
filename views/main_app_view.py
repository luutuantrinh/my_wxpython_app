import wx
import os

class MainAppView(wx.Frame):
    def __init__(self, parent, title):
        super(MainAppView, self).__init__(parent, title=title, size=(800, 600))
        self.init_ui()
        self.Center()

    def init_ui(self):
        panel = wx.Panel(self)

        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Main Feature Label
        main_label = wx.StaticText(panel, label="Main Feature", style=wx.ALIGN_CENTER)
        main_label.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
        main_sizer.Add(main_label, flag=wx.ALIGN_CENTER | wx.TOP, border=20)

        # Subtitle
        subtitle = wx.StaticText(panel, label="All Feature Available Here, Please Click Choose Your Action", style=wx.ALIGN_CENTER)
        subtitle.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        main_sizer.Add(subtitle, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        # Grid for features
        grid_sizer = wx.GridSizer(2, 3, 15, 15)

        features = [
            ("Chức năng 1", "Nội dung chức năng 1"),
            ("Chức năng 2", "Nội dung chức năng 2"),
            ("Chức năng 3", "Nội dung chức năng 3"),
            ("Chức năng 4", "Nội dung chức năng 4"),
            ("Chức năng 5", "Nội dung chức năng 5"),
            ("Chức năng 6", "Nội dung chức năng 6")   
        ]

        # Đường dẫn tương đối đến tệp hình ảnh
        icon_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'media', 'pngwing.com.png'))
        absolute_icon_path = os.path.abspath(icon_path)

        # In ra đường dẫn tuyệt đối để kiểm tra
        print(f"Đường dẫn tuyệt đối đến tệp hình ảnh: {absolute_icon_path}")

        for title, description in features:
            feature_panel = wx.Panel(panel)
            feature_sizer = wx.BoxSizer(wx.VERTICAL)

            try:
                # Load và thay đổi kích thước hình ảnh
                img = wx.Image(icon_path, wx.BITMAP_TYPE_ANY)
                img = img.Scale(50, 50, wx.IMAGE_QUALITY_HIGH)  # Thay đổi kích thước hình ảnh
                feature_icon = wx.StaticBitmap(feature_panel, bitmap=wx.Bitmap(img))
            except Exception as e:
                wx.LogError(f"Failed to load image from file \"{absolute_icon_path}\": {e}")
                continue

            feature_sizer.Add(feature_icon, flag=wx.ALIGN_CENTER)

            feature_title = wx.StaticText(feature_panel, label=title, style=wx.ALIGN_CENTER)
            feature_title.SetFont(wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))
            feature_sizer.Add(feature_title, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

            feature_desc = wx.StaticText(feature_panel, label=description, style=wx.ALIGN_CENTER)
            feature_desc.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
            feature_sizer.Add(feature_desc, flag=wx.ALIGN_CENTER | wx.TOP, border=5)

            feature_panel.SetSizer(feature_sizer)
            grid_sizer.Add(feature_panel, flag=wx.EXPAND)

        main_sizer.Add(grid_sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        panel.SetSizer(main_sizer)

if __name__ == '__main__':
    app = wx.App(False)
    frame = MainAppView(None, title="Main Feature UI")
    frame.Show()
    app.MainLoop()
