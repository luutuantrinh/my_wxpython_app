import wx
import os
import json
from views.about_view import AboutView

class MainAppView(wx.Frame):
    def __init__(self, parent, title, lang='en'):
        super(MainAppView, self).__init__(parent, title=title, size=(800, 600))

        self.lang = lang  # Set language

        # Load language content
        self.load_language_content()

        # Create status bar
        self.status_bar = self.CreateStatusBar()
        self.status_bar.SetStatusText("Ready")

        # Create a panel for the navigation bar
        nav_panel = wx.Panel(self)
        nav_panel.SetBackgroundColour(wx.Colour(240, 240, 240))

        nav_sizer = wx.BoxSizer(wx.VERTICAL)

        # Add workspace name
        workspace_label = wx.StaticText(nav_panel, label=self.content['workspace_name'], style=wx.ALIGN_CENTER)
        workspace_label.SetForegroundColour(wx.Colour(0, 0, 0))
        workspace_label.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD))

        # Add logo
        logo_path = r"media\pngwing.com.png"
        if os.path.exists(logo_path):
            image = wx.Image(logo_path, wx.BITMAP_TYPE_PNG)
            
            # Calculate new dimensions while keeping aspect ratio
            max_size = 100  # replace with desired max width or height
            width = image.GetWidth()
            height = image.GetHeight()
            if width > height:
                new_width = max_size
                new_height = max_size * height / width
            else:
                new_height = max_size
                new_width = max_size * width / height
            
            # Scale the image
            image = image.Scale(int(new_width), int(new_height), wx.IMAGE_QUALITY_HIGH)
            
            # Convert the wx.Image back to a wx.Bitmap
            logo = wx.Bitmap(image)
            
            logo_image = wx.StaticBitmap(nav_panel, bitmap=logo)
            nav_sizer.Add(logo_image, 0, wx.ALL | wx.CENTER, 10)

        workspace_sub_label = wx.StaticText(nav_panel, label=self.content['workspace_subname'], style=wx.ALIGN_CENTER)
        workspace_sub_label.SetForegroundColour(wx.Colour(100, 100, 100))

        nav_sizer.Add(workspace_label, 0, wx.ALL | wx.CENTER, 10)
        nav_sizer.Add(workspace_sub_label, 0, wx.ALL | wx.CENTER, 5)

        # Add search bar
        search_panel = wx.Panel(nav_panel)
        search_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        search_sizer = wx.BoxSizer(wx.HORIZONTAL)
        search_icon = wx.StaticText(search_panel, label="🔍")
        search_text = wx.TextCtrl(search_panel, style=wx.NO_BORDER)
        search_text.SetHint(self.content['search_hint'])
        search_text.SetBackgroundColour(wx.Colour(255, 255, 255))
        search_text.SetForegroundColour(wx.Colour(0, 0, 0))
        search_sizer.Add(search_icon, 0, wx.ALL, 5)
        search_sizer.Add(search_text, 1, wx.ALL, 5)
        search_panel.SetSizer(search_sizer)

        nav_sizer.Add(search_panel, 0, wx.ALL | wx.EXPAND, 10)

        # Add menu items as buttons
        menu_items = [
            (self.content['menu_dashboard'], "Dashboard"),
            (self.content['menu_orders'], "Orders"),
            (self.content['menu_products'], "Products"),
            (self.content['menu_customers'], "Customers"),
            (self.content['menu_about'], "About")
        ]
        
        self.content_panel = wx.Panel(self)
        self.content_panel.SetBackgroundColour(wx.Colour(255, 255, 255))
        self.content_sizer = wx.BoxSizer(wx.VERTICAL)
        self.content_panel.SetSizer(self.content_sizer)

        for label, item in menu_items:
            btn = wx.Button(nav_panel, label=label)
            btn.Bind(wx.EVT_BUTTON, self.on_menu_item_click)
            btn.item = item
            nav_sizer.Add(btn, 0, wx.ALL | wx.EXPAND, 5)

        nav_panel.SetSizer(nav_sizer)

        # Main sizer
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)
        main_sizer.Add(nav_panel, 0, wx.EXPAND | wx.ALL, 0)
        main_sizer.Add(self.content_panel, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(main_sizer)

        self.Centre()
        self.Show()

    def load_language_content(self):
        lang_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'languages.json')
        with open(lang_file_path, 'r', encoding='utf-8') as f:
            languages = json.load(f)
        self.content = languages.get(self.lang, languages['en'])

    def on_menu_item_click(self, event):
        button = event.GetEventObject()
        item = button.item
        self.status_bar.SetStatusText(f"{item} is running")
        
        # Clear previous content
        for child in self.content_panel.GetChildren():
            child.Destroy()

        if item == "About":
            dlg = AboutView(self, lang=self.lang)
            dlg.ShowModal()
        else:
            # Display the selected menu item content
            content_label = wx.StaticText(self.content_panel, label=f"{item} content is displayed here")
            content_label.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE.NORMAL, wx.FONTWEIGHT_NORMAL))
            self.content_sizer.Add(content_label, 0, wx.ALL | wx.CENTER, 10)
            self.content_panel.Layout()
