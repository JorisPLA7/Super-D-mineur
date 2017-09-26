helppage = "https://github.com/JorisPLA7/Super-D-mineur"
githubpage = "https://github.com/JorisPLA7/Super-D-mineur/"
rulepage = "http://www.tuks.ovh/github_webpages/super-D-mineur/gagner%20au%20d%c3%a9mineur.html"

import webbrowser

def help():
    webbrowser.open(helppage)
def github():
    webbrowser.open(githubpage)
def rules():
    webbrowser.open(rulepage)
if __name__ == '__main__':
    help()
