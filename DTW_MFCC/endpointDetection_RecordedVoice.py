import wave
import numpy as np
from DTW_MFCC.endpointDetection import EndPointDetect

from tqdm import tqdm


# 将语音文件存储成 wav 格式
def save_wave_file(filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)  # 声道
    wf.setsampwidth(4)
    wf.setframerate(16000)  # 采样频率 8000 or 16000
    wf.writeframes(b"".join(data))
    wf.close()


def endPointDetection(count = 5, datapath="./dataset/"):
    labels = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for label in tqdm(labels):
        for j in range(count):
            f = wave.open(datapath + label + "_" + str(j + 1) + ".wav", "rb")
            # getparams() 一次性返回所有的WAV文件的格式信息
            params = f.getparams()
            # nframes 采样点数目
            nchannels, sampwidth, framerate, nframes = params[:4]
            # readframes() 按照采样点读取数据
            str_data = f.readframes(nframes)
            wave_data = np.frombuffer(str_data, dtype='int16')
            f.close()
            end_point_detect = EndPointDetect(wave_data)
            N = end_point_detect.wave_data_detected
            # 输出为 wav 格式
            m = 0
            while m < len(N) - 1:
                save_wave_file("./ProcessedData/" + label + "_" + str(j + 1) + ".wav",
                               wave_data[N[m] * 256: N[m + 1] * 256])
                m = m + 2

if __name__=="__main__":
    endPointDetection()