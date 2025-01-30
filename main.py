from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys

class FileExplorer (QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")

        layout = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath('')

        self.tree = QTreeView()
        self.tree.setModel(self.model)

        self.tree.setRootIndex(self.model.index(''))

        layout.addWidget(self.tree)
        self.setLayout(layout)

        self.resize(800, 600)
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())