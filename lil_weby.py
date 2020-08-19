import webbrowser
urL='https://www.google.com'
firefox_path="C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
webbrowser.register('firefox', None,webbrowser.BackgroundBrowser(firefox_path),1)
webbrowser.get('firefox').open_new_tab(urL)
