import wx
from utils.language_manager import language_manager
from utils.logger import app_logger

class LoginView(wx.Dialog):
    def __init__(self, parent, title, controller):
        super(LoginView, self).__init__(parent, title=title, size=(350, 250))
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.panel = wx.Panel(self)
        
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        
        title_text = wx.StaticText(self.panel, label=language_manager.get('login'), style=wx.ALIGN_CENTER)
        title_font = wx.Font(16, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title_text.SetFont(title_font)
        title_text.SetForegroundColour(wx.Colour(0, 102, 204))
        
        main_sizer.Add(title_text, 0, wx.ALL | wx.EXPAND, 15)

        self.username_label = wx.StaticText(self.panel, label=language_manager.get('username'))
        self.username_text = wx.TextCtrl(self.panel, value="")
        
        self.password_label = wx.StaticText(self.panel, label=language_manager.get('password'))
        self.password_text = wx.TextCtrl(self.panel, value="", style=wx.TE_PASSWORD)

        self.login_button = wx.Button(self.panel, label=language_manager.get('login'), size=(100, 30))
        
        # Thêm các thành phần vào sizer
        main_sizer.Add(self.username_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.username_text, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.password_label, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.password_text, 0, wx.ALL | wx.EXPAND, 5)
        main_sizer.Add(self.login_button, 0, wx.ALL | wx.CENTER, 10)
        
        # Thiết lập sự kiện cho button
        self.login_button.Bind(wx.EVT_BUTTON, self.on_login)

        self.panel.SetSizer(main_sizer)
        
    def on_login(self, event):
        username = self.username_text.GetValue()
        password = self.password_text.GetValue()
        # Gọi hàm xử lý đăng nhập từ controller
        self.controller.handle_login(username, password)

        # Ghi log cho sự kiện đăng nhập
        app_logger.info(f"Login attempt by user: {username}")
    

    def show_message(self, message):
        wx.MessageBox(message, "Info", wx.OK | wx.ICON_INFORMATION)
