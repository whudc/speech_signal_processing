import sys
from PyQt5.QtWidgets import QApplication
from GUI import backend


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ui = backend.SoundGuiBackend()
    ui.show()
    sys.exit(app.exec_())

