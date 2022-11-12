import os
import time

from PyQt5.QtWidgets import QMainWindow

from GUI.frontend import Ui_MainWindow

from Utils.sound_recoder import recoder


class SoundGuiBackend(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 创建窗体对象
        self.r = recoder()
        self.start_record_test_pushButton.clicked.connect(self.test_state_select)
        self.start_record_train_pushButton.clicked.connect(self.train_state_select)
        self.train_single_digital_radioButton.setChecked(True)
        self.test_single_digital_radioButton.setChecked(True)
        self.zh_radioButton.setChecked(True)
        self.en_radioButton.setChecked(False)

    def sequence_zh_record_train(self):
        """
        录制中文训练集数字序列
        :return:
        """
        sequence = self.digital_sequence_textEdit.toPlainText()
        file_name = time.time()
        file = os.path.join("dataset_zh/sequence/" + sequence + str(file_name) + ".wav")
        self.r.recoder()
        self.r.savewav(file)

    def sequence_en_record_train(self):
        """
        录制英文训练集数字序列
        :return:
        """
        sequence = self.digital_sequence_textEdit.toPlainText()
        file_name = time.time()
        file = os.path.join("dataset_en/sequence/" + sequence + str(file_name) + ".wav")
        self.r.recoder()
        self.r.savewav(file)

    def single_zh_record_train(self):
        """
        录制中文训练集单个数字
        :return:
        """
        self.digital_select_comboBox.currentText()
        number = self.digital_select_comboBox.currentText()
        number = int(number)
        numberdict = {0: "dataset_zh/zero/zero", 1: "dataset_zh/one/one", 2: "dataset_zh/two/two",
                      3: "dataset_zh/three/three",
                      4: "dataset_zh/four/four", 5: "dataset_zh/five/five", 6: "dataset_zh/six/six",
                      7: "dataset_zh/seven/seven",
                      8: "dataset_zh/eight/eight", 9: "dataset_zh/nine/nine"}
        file = numberdict.get(number)
        file_name = time.time()
        file = os.path.join(file + str(file_name) + ".wav")
        self.r.recoder()
        self.r.savewav(file)

    def single_en_record_train(self):
        """
        录制英文训练集单个数字
        :return:
        """
        self.digital_select_comboBox.currentText()
        number = self.digital_select_comboBox.currentText()
        number = int(number)
        numberdict = {0: "dataset_en/zero/zero", 1: "dataset_en/one/one", 2: "dataset_en/two/two",
                      3: "dataset_en/three/three",
                      4: "dataset_en/four/four", 5: "dataset_en/five/five", 6: "dataset_en/six/six",
                      7: "dataset_en/seven/seven",
                      8: "dataset_en/eight/eight", 9: "dataset_en/nine/nine"}
        file = numberdict.get(number)
        file_name = time.time()
        file = os.path.join(file + str(file_name) + ".wav")
        print(file)
        self.r.recoder()
        self.r.savewav(file)

    def train_state_select(self):
        if self.train_single_digital_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.single_zh_record_train()
        elif self.train_single_digital_radioButton.isChecked() and self.en_radioButton.isChecked():
            self.single_en_record_train()
        elif self.train_digital_sequence_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.sequence_zh_record_train()
        else:
            self.sequence_en_record_train()

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
