import sys
from PyQt5.QtWidgets import *




class EmptyWindow(QWidget):
    def __init__(self):
        super(EmptyWindow, self).__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Empty Window in PyQt5')
        self.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        window = EmptyWindow(sys.argv)
        sys.exit(app.exec_())
