import os
import time

from PyQt5.QtWidgets import QMainWindow

from GUI.frontend import Ui_MainWindow

from Utils.record import record_all, record_once


class SoundGuiBackend(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 创建窗体对象
        self.start_record_test_pushButton.clicked.connect(self.test_state_select)
        self.start_record_train_pushButton.clicked.connect(self.train_state_select)
        self.train_single_digital_radioButton.setChecked(True)
        self.test_single_digital_radioButton.setChecked(True)
        self.zh_radioButton.setChecked(True)
        self.en_radioButton.setChecked(False)

    def sequence_record_train(self, path):
        """
        录制训练集数字序列
        :return:
        """
        sequence = self.digital_sequence_textEdit.toPlainText()
        file_name = time.time()
        file = os.path.join(path + sequence + str(file_name) + ".wav")
        record_all(5, output_dir=file)

    def single_record_train(self, path):
        """
        录制训练集单个数字
        :return:
        """
        self.digital_select_comboBox.currentText()
        number = self.digital_select_comboBox.currentText()
        number = int(number)
        numberdict = {0: "zero/zero", 1: "one/one", 2: "two/two",
                      3: "three/three", 4: "four/four",
                      5: "five/five", 6: "six/six",
                      7: "seven/seven", 8: "eight/eight",
                      9: "nine/nine"}
        file = numberdict.get(number)
        record_once(1, 16000, 3, file, output_dir=path)

    def train_state_select(self):
        if self.train_single_digital_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.single_record_train("dataset_zh")
        elif self.train_single_digital_radioButton.isChecked() and self.en_radioButton.isChecked():
            self.single_record_train("dataset_en")
        elif self.train_digital_sequence_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.sequence_record_train("dataset_zh/sequence/")
        else:
            self.sequence_record_train("dataset_en/sequence/")

    def single_zh_recognition(self):
        pass

    def single_en_recognition(self):
        pass

    def sequence_zh_recognition(self):
        pass

    def sequence_en_recognition(self):
        pass

    def test_state_select(self):
        if self.test_single_digital_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.single_zh_recognition()
        elif self.test_single_digital_radioButton.isChecked() and self.en_radioButton.isChecked():
            self.single_en_recognition()
        elif self.test_digital_sequence_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.sequence_zh_recognition()
        else:
            self.sequence_en_recognition()
