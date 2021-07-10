from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QApplication
from PyQt5 import QtWebEngineWidgets, QtGui
from PyQt5.QtCore import QUrl
import const

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Whatsie")
        self.setWindowIcon(QtGui.QIcon("../assets/logo.png"))
        self.resize(800, 701)
        self.root = QVBoxLayout()
        self.root.setContentsMargins(0,0,0,0)
        self.setLayout(self.root)
        self.webView = QtWebEngineWidgets.QWebEngineView()
        self.webView.page().profile().setHttpUserAgent(const.user_agent)
        self.webView.load(QUrl(const.site))
        self.webView.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.root.addWidget(self.webView)
    
    def navigate_to_url(self, site): 
        q = QUrl(sit) 
        if q.scheme() == "": 
            q.setScheme("http") 
        self.tabs.currentWidget().setUrl(q) 
  

def main():
    import sys
    app = QApplication(sys.argv)
    demo = MainWindow()
    demo.show()
    sys.exit(app.exec_())

if (__name__=="__main__"):
    main()