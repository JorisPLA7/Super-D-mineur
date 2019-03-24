helppage = "https://github.com/JorisPLA7/Super-D-mineur"
githubpage = "https://github.com/JorisPLA7/Super-D-mineur/"
rulepage = "http://demineur.hugames.fr/help.php"

import webbrowser

def help():
    webbrowser.open(helppage)
def github():
    webbrowser.open(githubpage)
def rules():
    webbrowser.open(rulepage)
if __name__ == '__main__':
    help()
