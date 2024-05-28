import wx
from utils.language_manager import language_manager

class SecretLoginView(wx.Frame):
    def __init__(self, parent, title, controller):
        super(SecretLoginView, self).__init__(parent, title=title, size=(350, 250))
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.panel = wx.Panel(self)
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        title_text = wx.StaticText(self.panel, label=language_manager.get('login_with_secret_key'), style=wx.ALIGN_CENTER)
        title_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE.NORMAL, wx.FONTWEIGHT_BOLD)
        title_text.SetFont(title_font)
        title_text.SetForegroundColour(wx.Colour(0, 102, 204))
        
        main_sizer.Add(title_text, 0, wx.ALL | wx.EXPAND, 15)

        self.username_label = wx.StaticText(self.panel, label=language_manager.get('username'))
        self.username_text = wx.TextCtrl(self.panel, value="")
        
        self.secret_key_label = wx.StaticText(self.panel, label=language_manager.get('secret_key'))
        self.secret_key_text = wx.TextCtrl(self.panel, value="")

        self.login_button = wx.Button(self.panel, label=language_manager.get('login'), size=(100, 30))
        
        # Thêm các thành phần vào sizer
        main_sizer.Add(self.username_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.username_text, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.secret_key_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.secret_key_text, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 10)
        
        # Thiết lập sự kiện cho button
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)

        self.panel.SetSizer(main_sizer)
        
    def on_login(self, event):
        username = self.username_text.GetValue()
        secret_key = self.secret_key_text.GetValue()
        # Gọi hàm xử lý đăng nhập từ controller
        self.controller.handle_secret_login(username, secret_key)

    def show_message(self, message):
        wx.MessageBox(message, "Info", wx.OK | wx.ICON_INFORMATION)
