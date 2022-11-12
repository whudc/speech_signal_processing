import os.path

import pyaudio
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave


class recoder:
    NUM_SAMPLES = 2000  # pyaudio内置缓冲大小
    SAMPLING_RATE = 16000  # 取样频率
    LEVEL = 500  # 声音保存的阈值
    COUNT_NUM = 20  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
    SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
    TIME_COUNT = 15  # 录音时间

    Voice_String = []

    def savewav(self, filename):
        dirpath = os.path.dirname(filename)
        os.makedirs(dirpath, exist_ok=True)
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.SAMPLING_RATE)
        wf.writeframes(np.array(self.Voice_String).tostring())
        # wf.writeframes(self.Voice_String.decode())
        wf.close()
        print("保存成功")

    def recoder(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        save_count = 0
        save_buffer = []
        time_count = self.TIME_COUNT
        print("请在3秒内完成声音录制")
        while True:
            time_count -= 1
            # print time_count
            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(self.NUM_SAMPLES)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum(audio_data > self.LEVEL)
            # print(np.max(audio_data))
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.COUNT_NUM:
                save_count = self.SAVE_LENGTH
            else:
                save_count -= 1

            if save_count < 0:
                save_count = 0
            if save_count > 0:
                save_buffer.append(string_audio_data)
            else:
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    return True
            if time_count == 0:
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    return True
                else:
                    return False

    def play_wav(self, wav_path):
        CHUNK = 1024
        # print("wav_path :",wav_path )
        #
        wf = wave.open(wav_path, 'rb')
        # print("samplewidth:", wf.getsampwidth())
        # print("channles:",wf.getnchannels())
        # print("framerate:",wf.getframerate())
        p = pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        data = wf.readframes(CHUNK)
        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close()
        wf.close()
        p.terminate()
