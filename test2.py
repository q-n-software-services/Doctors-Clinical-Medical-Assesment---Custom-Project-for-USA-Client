
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from test import *


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 300, 220)
        # self.setWindowIcon(QIcon('web.png'))

        self.centralWidget = QFrame()
        self.centralLayout = QVBoxLayout()
        self.centralWidget.setLayout(self.centralLayout)

        self.spoiler1 = Spoiler(addRemoveOption='Add', title='Group 1')
        self.spoiler2 = Spoiler(addRemoveOption='Add', title='Group 2')
        for i in range(3):
            leaf = LeafSpoiler(root=self.spoiler1)
            self.spoiler1.addChild(leaf)

            leaf = LeafSpoiler(root=self.spoiler2)
            self.spoiler2.addChild(leaf)
        self.centralLayout.addWidget(self.spoiler1)
        self.centralLayout.addWidget(self.spoiler2)

        self.setCentralWidget(self.centralWidget)
        self.show()



if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())

