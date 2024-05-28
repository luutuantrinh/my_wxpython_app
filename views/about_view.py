import wx
import wx.html
import json
import os

class AboutView(wx.Dialog):
    def __init__(self, parent, lang='en'):
        super(AboutView, self).__init__(parent, title="About", size=(500, 400))

        # Load language content
        lang_file_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'config', 'languages.json')
        with open(lang_file_path, 'r', encoding='utf-8') as f:
            languages = json.load(f)
        
        content = languages.get(lang, languages['en'])

        html_content = f"""
        <!DOCTYPE html>
        <html lang="{lang}">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{content['about_title']}</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #f8f9fa;
                }}
                .container {{
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    font-size: 24px;
                    color: #333333;
                }}
                p {{
                    font-size: 14px;
                    color: #666666;
                }}
                a {{
                    color: #007bff;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .btn {{
                    display: inline-block;
                    padding: 10px 20px;
                    margin-top: 20px;
                    font-size: 14px;
                    font-weight: 600;
                    color: #ffffff;
                    background-color: #007bff;
                    border: none;
                    border-radius: 4px;
                    text-align: center;
                    cursor: pointer;
                    text-decoration: none;
                }}
                .btn:hover {{
                    background-color: #0056b3;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{content['about_title']}</h1>
                <p>{content['about_description']}</p>
                <p>{content['developer']}</p>
                <p>{content['position']}</p>
                <p>{content['linkedin']}</p>
                <p>{content['experience']}</p>
                <a href="#" class="btn" onclick="window.close();">{content['close_button']}</a>
            </div>
        </body>
        </html>
        """

        html_window = wx.html.HtmlWindow(self)
        html_window.SetPage(html_content)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(html_window, 1, wx.EXPAND)
        self.SetSizer(sizer)
