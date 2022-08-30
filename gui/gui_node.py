from PyQt5.QtWidgets import (
    QDialog, QFileDialog
)

from gui import NodeUI
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
