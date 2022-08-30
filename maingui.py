import sys


from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox, QFileDialog
)

from gui import MainUI, NodeUI
from forta import Node
from linux import User, Server

class NodeWindow(QDialog, NodeUI):
    def __init__(self, parent=None):
        super(NodeWindow, self).__init__()
        self.server = None
        self.parent = parent
        self.setupUi(self)

    def testConnection(self):
        self.server = Server(self.editIPADDR.text())
        if self.editPassword.text() == "":
            pw = None
        else:
            pw = self.editPassword.text()
        self.server.set_user(User(username = self.editUsername.text(),
                                  password = pw,
                                  keyfile = self.editSSHKeyFile.text()))

        state = self.server.test()
        if state:
            self.lblTest.setText("Connected")
        else:
            self.lblTest.setText("NOT Connected")
    def saveNode(self):
        pass

    def sshkey(self):
            
        fname, ftype = QFileDialog.getOpenFileName(self,
                                                   'Open SSH Private Key File',
                                                   '',"")
        self.editSSHKeyFile.setText(fname)

        
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

        pass

    def getSLA(self):
        pass

    def updateSLAs(self):
        pass
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)                    
