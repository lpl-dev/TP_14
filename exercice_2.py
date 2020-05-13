from PySide2.QtWidgets import QLabel, QWidget, QPushButton, QApplication, QGridLayout, QTextEdit

class Window(QWidget):
    def __init__(self,title=''):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.g_layout=QGridLayout()
        self.label=QLabel('Laisser un commentaire')
        self.text_edit=QTextEdit()
        self.buttons=[QPushButton('Success'),QPushButton('Cancel')]
        self.g_layout.addWidget(self.label,1,1,1,2)
        self.g_layout.addWidget(self.text_edit,2,1,1,2)
        self.g_layout.addWidget(self.buttons[0],3,1)
        self.g_layout.addWidget(self.buttons[1],3,2)
        self.setLayout(self.g_layout)

if __name__=='__main__':
    app=QApplication([])
    win=Window('IHM')
    win.show()
    app.exec_()