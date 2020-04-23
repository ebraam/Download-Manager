import PyQt5
from PyQt5.QtWidgets import *

from PyQt5 import QtCore, QtGui, uic, QtWidgets
import urllib.request
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("layout.ui", self)
        self.title = "Downloader"
        self.width = 571
        self.height = 230
        self.icon = "icon.png"
        self.Handel_UI()
        self.Handel_button()

    def Handel_UI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setFixedSize(self.width, self.height)
        self.le_url.setPlaceholderText("URL")
        self.le_save.setPlaceholderText("Save Location")
        # self.lbl_url = QLabel("url")
        # self.lbl_save = QLabel("save Location")
        self.show()

    def Handel_button(self):
        self.btn_Download.clicked.connect(self.Handel_Download)
        self.btn_Browse.clicked.connect(self.Handel_browse)
    def Handel_browse(self):
        save_location = QFileDialog.getSaveFileName(self, caption="Save As", directory=".", filter="All Files(*.*)")
        text = str(save_location)
        name = text.split(",")
        save = name[0]
        s = save[2:-1]
        self.le_save.setText(s)

    def Handel_progress(self, blocknum, blocksize, totalsize):
        size = blocknum*blocksize
        percentage = (size // totalsize)*100
        self.progressBar.setValue(percentage)
    def Handel_Download(self):
        url = self.le_url.text()
        save_location = self.le_save.text()
        try:

            urllib.request.urlretrieve(url, save_location, self.Handel_progress)

            QMessageBox.information(self, "Download Complete", "Your Download Complete")

        except Exception:
            QMessageBox.warning(self, "Download Field", "Download Failed")
           

        self.le_url.setPlaceholderText("URL")
        self.le_save.setPlaceholderText("Save Location")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
