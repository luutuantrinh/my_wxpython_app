import wx
from controllers.login_controller import LoginController

class MyApp(wx.App):
    def OnInit(self):
        self.controller = LoginController()
        self.controller.show_view()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()
