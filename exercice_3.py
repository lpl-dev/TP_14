from PySide2.QtWidgets import QLabel, QWidget, QApplication, QVBoxLayout, QProgressBar, QPushButton, QLineEdit
from PySide2.QtGui import QIcon
from PySide2.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(400,300)
        self.setWindowTitle('IHM')
        self.icon=QIcon('fr-flag.png')
        self.setWindowIcon(self.icon)

        self.v_layout = QVBoxLayout()

        self.label=QLabel('Hello World')
        self.label.setAlignment(Qt.AlignCenter)

        self.progress_bar=QProgressBar()
        self.progress_bar.setValue(50)

        self.line_edit=QLineEdit()

        self.button=QPushButton('Click me !')
        self.button.setToolTip('Now !')

        self.v_layout.addWidget(self.label)
        self.v_layout.addWidget(self.progress_bar)
        self.v_layout.addWidget(self.line_edit)
        self.v_layout.addWidget(self.button)
        self.setLayout(self.v_layout)


if __name__=='__main__':
    app=QApplication([])
    win=Window()
    win.show()
    app.exec_()