import subprocess
import pkg_resources
import os
import platform

# Kiểm tra xem Python đã được cài đặt hay chưa
try:
    subprocess.check_output("python --version", shell=True)
except subprocess.CalledProcessError:
    # Nếu chưa, cài đặt Python
    if platform.system() == "Windows":
        print("Please install Python from https://www.python.org/downloads/windows/")
    elif platform.system() == "Darwin":
        os.system("brew install python3")
    elif platform.system() == "Linux":
        os.system("sudo apt-get install python3.8")

REQUIRED_PACKAGES = [
    'wxPython',
    'Fernet',
    'requests',
    'cryptography'
]

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
for i in installed_packages])
for package in REQUIRED_PACKAGES:
    if package not in installed_packages_list:
        subprocess.check_call(["python", '-m', 'pip', 'install', package])
        
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
