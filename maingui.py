import sys

from PyQt5.QtWidgets import (
    QApplication
)

from gui import MainWindow
from gui import NodeWindow        
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow(app)
    ret = app.exec_()
    app.exit()
    sys.exit(ret)                    
