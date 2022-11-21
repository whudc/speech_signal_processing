# -*- coding: utf-8 -*-
import os
import wave
import numpy as np
import scipy.io.wavfile as wav
from python_speech_features import *
from scipy import signal

from DTW_MFCC.endpointDetection import EndPointDetect


# 读取已经用 HTK 计算好的 MFCC 特征

def extract_MFCC(file):
    fs, audio = wav.read(file)
    wav_feature = mfcc(audio, samplerate=fs, numcep=13, winlen=0.025, winstep=0.01, nfilt=26, nfft=512, lowfreq=0,
                       highfreq=None, preemph=0.97)
    d_mfcc_feat = delta(wav_feature, 1)
    d_mfcc_feat2 = delta(wav_feature, 2)
    feature_mfcc = np.hstack((wav_feature, d_mfcc_feat, d_mfcc_feat2))
    return feature_mfcc


def getMFCC(datapath, train_num):
    MFCC = []
    files = os.listdir(datapath)  # 得到文件夹下的所有文件名称
    for file in files:  # 遍历文件夹
        MFCC_rows = []
        if file != "sequence":
            paths = os.path.join(datapath, file)
            paths = os.listdir(paths)
            for open_path in paths:
                file_name = os.path.join(datapath, file + '/' + open_path)
                feature = extract_MFCC(file_name)
                MFCC_rows.append(feature)
            MFCC.append(MFCC_rows)
    return MFCC


# 取出其中的模板命令的 MFCC 特征
def getMFCCModels(MFCC):
    MFCC_models = []
    for i in range(len(MFCC)):
        MFCC_models.append(MFCC[i][0])
    return MFCC_models


# 取出其中的待分类语音的 MFCC 特征
def getMFCCUndetermined(MFCC):
    MFCC_undetermined = []
    for i in range(len(MFCC)):
        for j in range(1, len(MFCC[i])):
            MFCC_undetermined.append(MFCC[i][j])
    return MFCC_undetermined


# DTW 算法...
def dtw(M1, M2):
    # 初始化数组 大小为 M1 * M2
    M1_len = len(M1)
    M2_len = len(M2)
    cost = [[0 for i in range(M2_len)] for i in range(M1_len)]

    # 初始化 dis 数组
    dis = []
    for i in range(M1_len):
        dis_row = []
        for j in range(M2_len):
            dis_row.append(distance(M1[i], M2[j]))
        dis.append(dis_row)

    # 初始化 cost 的第 0 行和第 0 列
    cost[0][0] = dis[0][0]
    for i in range(1, M1_len):
        cost[i][0] = cost[i - 1][0] + dis[i][0]
    for j in range(1, M2_len):
        cost[0][j] = cost[0][j - 1] + dis[0][j]

    # 开始动态规划
    for i in range(1, M1_len):
        for j in range(1, M2_len):
            cost[i][j] = min(cost[i - 1][j] + dis[i][j] * 1, cost[i - 1][j - 1] + dis[i][j] * 2,
                             cost[i][j - 1] + dis[i][j] * 1)
    return cost[M1_len - 1][M2_len - 1]


# 两个维数相等的向量之间的距离
def distance(x1, x2):
    sum = 0
    for i in range(len(x1)):
        sum = sum + abs(x1[i] - x2[i])
    return sum


# 将语音文件存储成 wav 格式
def save_wave_file(filename, data):
    '''save the date to the wavfile'''
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)  # 声道
    wf.setsampwidth(4)  # 采样字节 1 or 2
    wf.setframerate(16000)  # 采样频率 8000 or 16000
    wf.writeframes(b"".join(data))
    wf.close()


def lowpass(wav_data, order, fre_c):
    b, a = signal.butter(order, fre_c)
    filtedData = signal.filtfilt(b, a, wav_data)  # data为要过滤的信号
    return filtedData


def train_model(path):
    # 存储所有语音文件的 MFCC 特征
    # 读取已经用 HTK 计算好的 MFCC 特征
    MFCC = getMFCC(path, 5)
    # 取出其中的模板命令的 MFCC 特征
    MFCC_models = getMFCCModels(MFCC)
    return MFCC_models


def speech_recognition(MFCC_models, wave_data):
    wav.write("./test/recordedVoice_before.wav", 16000, wave_data)
    # 对刚录制的语音进行端点检测
    sample_frequency, audio_sequence = wav.read("./test/recordedVoice_before.wav")
    filterData = lowpass(wave_data, 99, 5000 / sample_frequency)
    end_point_detect = EndPointDetect(filterData)
    # 存储端点检测后的语音文件
    N = end_point_detect.wave_data_detected
    m = 0
    print(N)
    while m < len(N):
        save_wave_file("./test/recordedVoice_after.wav", wave_data[N[m] * 256: N[m + 1] * 256])
        m = m + 2
    MFCC_recorded = extract_MFCC("./test/recordedVoice_after.wav")

    # 进行匹配
    flag = 0
    min_dis = dtw(MFCC_recorded, MFCC_models[0])
    for j in range(1, len(MFCC_models)):
        dis = dtw(MFCC_recorded, MFCC_models[j])
        if dis < min_dis:
            min_dis = dis
            flag = j
    return flag
