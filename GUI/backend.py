import os
import sys
import time

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication
from PyQt5.Qt import QThread, pyqtSignal
from Core.Wave2Vec import SdrEnModel, SdrZhModel
from DTW_MFCC.VoiceRecog import train_model, speech_recognition
from GUI.frontend import Ui_MainWindow

from Utils.record import record_once

app = QApplication(sys.argv)


class GuiRecord(QThread):
    finish_signal = pyqtSignal(dict)

    def __init__(self, outputdir, label, finish_callback=None):
        super().__init__()
        self.outputdir = outputdir
        self.label = label
        if finish_callback is not None:
            self.finish_signal.connect(finish_callback)
        self.record_data = None

    def run(self):
        try:
            self.record_data = record_once(1, 16000, 3, self.label, output_dir=self.outputdir)
        except:
            self.finish_signal.emit({'status': 404, 'msg': 'Record Failed'})
            return
        self.finish_signal.emit({'status': 0, 'msg': 'Record successfully'})

    def get_record(self) -> np.ndarray:
        return self.record_data


class SoundGuiBackend(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # 创建窗体对象
        self.record_pushButton.clicked.connect(self.start_record)
        self.recognition_pushButton.clicked.connect(self.start_recognition)
        # self.start_train_pushButton.clicked.connect(self.start_train)
        # self.single_digital_radioButton.setChecked(True)
        # self.single_digital_radioButton.setChecked(True)
        # self.zh_radioButton.setChecked(True)
        # self.en_radioButton.setChecked(False)

        self.record_train_thread = None
        self.record_test_thread = None
        self.mode = 0
        """
        模式选择：
            0: 中文 单个数字
            1: 英文 单个数字
            2: 中文 数字序列
            3: 英文 数字序列
        """
        print("Loading Models")
        self.dl_en_model = SdrEnModel()
        self.ml_en_model = None
        self.dl_zh_model = SdrZhModel()
        self.ml_zh_model = None
        print("Models Loaded")

    def mode_select(self):
        if self.single_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.mode = 0
        elif self.single_radioButton.isChecked() and self.en_radioButton.isChecked():
            self.mode = 1
        elif self.seq_radioButton.isChecked() and self.zh_radioButton.isChecked():
            self.mode = 2
        else:
            self.mode = 3

    def sequence_record_train(self, outputdir):
        """
        录制训练集数字序列
        :return:
        """
        label = self.digital_sequence_textEdit.toPlainText()
        self.record_train_thread = GuiRecord(outputdir, label, self.record_callback)
        self.record_train_thread.start()
        # record_once(1, 16000, 4, label, outputdir)

    def single_record_train(self, outputdir):
        """
        录制训练集单个数字
        :return:
        """
        self.digital_select_comboBox.currentText()
        number = self.digital_select_comboBox.currentText()
        number = int(number)
        numberdict = {0: "zero", 1: "one", 2: "two",
                      3: "three", 4: "four",
                      5: "five", 6: "six",
                      7: "seven", 8: "eight",
                      9: "nine"}
        label = numberdict.get(number)

        self.record_train_thread = GuiRecord(outputdir, label, self.record_callback)
        self.record_train_thread.start()
        # record_once(1, 16000, 3, label, output_dir=outputdir)

    def record_callback(self, data: dict):
        dlg = QMessageBox(parent=self)
        dlg.setWindowTitle('Record Success')
        dlg.setText(data['msg'])
        dlg.exec()

    def start_record(self):
        self.mode_select()
        if self.mode == 0:
            self.single_record_train("dataset_zh/single")
        elif self.mode == 1:
            self.single_record_train("dataset_en/single")
        elif self.mode == 2:
            self.sequence_record_train("dataset_zh/seq/")
        else:
            self.sequence_record_train("dataset_en/seq/")

    def start_train(self):
        if self.mode == 0:
            self.ml_zh_model = train_model("dataset_zh/single")
        elif self.mode == 1:
            self.ml_en_model = train_model("dataset_en/single")
        QMessageBox.information(self, '提示', '训练完成')

    # TODO: 机器学习/深度学习选项组合
    def single_zh_recognition(self):
        data = self.record_test_thread.get_record()
        if self.ml_radioButton.isChecked():
            label = speech_recognition(self.ml_zh_model, np.array(data))
            self.machine_learning_result_textBrowser.setText(str(label))
        else:
            label = self.dl_zh_model.predict_single(data)
            self.deep_learning_result_textBrowser.setText(str(label))

    def single_en_recognition(self):
        data = self.record_test_thread.get_record()
        if self.ml_radioButton.isChecked():
            pass
            # label = speech_recognition(self.ml_en_model, data)
        else:
            label = self.dl_en_model.predict_single(data)
        self.deep_learning_result_textBrowser.setText(str(label))

    def sequence_zh_recognition(self):
        data = self.record_test_thread.get_record()
        labels = self.dl_zh_model.predict_seq(data)
        self.deep_learning_result_textBrowser.setText(str(labels))
        pass

    def sequence_en_recognition(self):
        data = self.record_test_thread.get_record()
        labels = self.dl_en_model.predict_seq(data)
        self.deep_learning_result_textBrowser.setText(str(labels))
        pass

    def start_recognition(self):
        # 先录制
        self.record_test_thread = GuiRecord('test', 'test')
        self.record_test_thread.run()
        # while self.record_train_thread.isRunning():
        #     app.processEvents()
        if self.record_test_thread.get_record() is None:
            self.record_callback({'msg': 'Record Failed'})
            return

        if self.mode == 0:
            self.single_zh_recognition()
        elif self.mode == 1:
            self.single_en_recognition()
        elif self.mode == 2:
            self.sequence_zh_recognition()
        else:
            self.sequence_en_recognition()
