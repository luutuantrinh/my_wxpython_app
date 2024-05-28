import wx
import os
from utils.language_manager import language_manager

class MainView(wx.Frame):
    def __init__(self, parent, title, controller):
        super(MainView, self).__init__(parent, title=title, size=(500, 400))
        self.controller = controller
        self.init_ui()
        self.Center()

    def init_ui(self):
        self.panel = wx.Panel(self)
        
        # Tạo một sizer để quản lý bố cục
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        self.title_text = wx.StaticText(self.panel, label=language_manager.get('welcome'), style=wx.ALIGN_CENTER)
        title_font = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.title_text.SetFont(title_font)
        self.title_text.SetForegroundColour(wx.Colour(0, 102, 204))
        
        self.main_sizer.Add(self.title_text, 0, wx.ALL | wx.EXPAND, 15)

        # Thêm khu vực chứa hình ảnh
        image_path = os.path.join(os.path.dirname(__file__), '..', 'media', 'your_image.png')
        if os.path.exists(image_path):
            image = wx.Image(image_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            self.image_ctrl = wx.StaticBitmap(self.panel, wx.ID_ANY, image)
            self.main_sizer.Add(self.image_ctrl, 0, wx.ALL | wx.CENTER, 10)
        
        self.login_button = wx.Button(self.panel, label=language_manager.get('login'), size=(200, 40))
        self.register_button = wx.Button(self.panel, label=language_manager.get('register'), size=(200, 40))
        self.secret_login_button = wx.Button(self.panel, label=language_manager.get('login_with_secret_key'), size=(200, 40))

        # Thêm các button vào sizer
        self.main_sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 10)
        self.main_sizer.Add(self.register_button, 0, wx.ALL | wx.CENTER, 10)
        self.main_sizer.Add(self.secret_login_button, 0, wx.ALL | wx.CENTER, 10)

        # Thêm combo box để chọn ngôn ngữ
        self.language_choice = wx.Choice(self.panel, choices=["English", "Vietnamese"])
        self.language_choice.SetSelection(0)  # Mặc định chọn tiếng Anh
        self.language_choice.Bind(wx.EVT_CHOICE, self.on_language_change)
        self.main_sizer.Add(self.language_choice, 0, wx.ALL | wx.CENTER, 10)
        
        # Thiết lập sự kiện cho các button
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)
        self.register_button.Bind(wx.EVT_BUTTON, self.on_register)
        self.secret_login_button.Bind(wx.EVT_BUTTON, self.on_secret_login)

        self.panel.SetSizer(self.main_sizer)

    def on_login(self, event):
        self.controller.show_login_view()

    def on_register(self, event):
        self.controller.show_register_view()

    def on_secret_login(self, event):
        self.controller.show_secret_login_view()

    def on_language_change(self, event):
        choice = self.language_choice.GetString(self.language_choice.GetSelection())
        if choice == "English":
            language_manager.set_language('en')
        elif choice == "Vietnamese":
            language_manager.set_language('vi')
        self.update_ui()

    def update_ui(self):
        # Cập nhật các nhãn và văn bản với ngôn ngữ mới
        self.title_text.SetLabel(language_manager.get('welcome'))
        self.login_button.SetLabel(language_manager.get('login'))
        self.register_button.SetLabel(language_manager.get('register'))
        self.secret_login_button.SetLabel(language_manager.get('login_with_secret_key'))
        self.panel.Layout()
