import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt

import QCandyUi
from GUI import backend
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
if __name__ == '__main__':

    app = QApplication(sys.argv)

    ui = backend.SoundGuiBackend()
    form = QCandyUi.CandyWindow.createWindow(ui, theme="blueDeep", ico_path="WHUEIS.jpg",
                                             title="WHU FYT DC LD QH Speech Digit Signal Recognition GUI v1.0")
    form.show()
    sys.exit(app.exec_())

