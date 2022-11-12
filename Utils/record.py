import os

import sounddevice as sd
from scipy.io.wavfile import write
import random


def record_all(time=2, output_dir="../dataset_test"):  # dataset_zh_seq_test
    CHANNELS = 1
    RATE = 16000
    RECORD_SECONDS = time  # 需要录制的时间
    os.makedirs(output_dir, exist_ok=True)
    while True:
        label = input("Enter Record Label: ")
        if 'q' == label[0]:
            return
        record_once(CHANNELS, RATE, RECORD_SECONDS, label, output_dir)
        while True:
            check = input("Yes/No: ")
            if check[0].lower() != 'n':
                break
            record_once(CHANNELS, RATE, RECORD_SECONDS, label, output_dir)


def record_once(CHANNELS, RATE, RECORD_SECONDS, label, output_dir):
    print(f"Recording: {label}")
    WAVE_OUTPUT_FILENAME = os.path.join(output_dir, f"{label}_{random.randint(10000, 99999)}.wav")  # 保存的文件名
    print(WAVE_OUTPUT_FILENAME)
    if os.path.exists(WAVE_OUTPUT_FILENAME):
        print("File Already Exists")
        return
    myrecording = sd.rec(int(RECORD_SECONDS * RATE), samplerate=RATE, channels=CHANNELS)
    print("ON")
    sd.wait()  # Wait until recording is finished
    print("OFF")
    write(WAVE_OUTPUT_FILENAME, RATE, myrecording)  # Save as WAV
    # file
    sd.play(myrecording, samplerate=RATE)
    sd.wait()


if __name__ == "__main__":
    record_all()
