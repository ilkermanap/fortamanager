

from PyQt5.QtWidgets import (
    QDialog
)

from . import MainUI
from .gui_node import NodeWindow

class MainWindow(QDialog, MainUI):
    def __init__(self, app=None):
        super(MainWindow, self).__init__()
        self.app = app
        self.nodewindow = None
        self.setupUi(self)
        self.show()

    def createNode(self):
        self.nodewindow = NodeWindow(self)
        self.nodewindow.show()

    def getSLA(self):
        pass

    def updateSLAs(self):
        pass
