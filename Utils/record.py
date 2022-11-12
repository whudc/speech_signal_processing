import os
import time

import librosa
import numpy as np
import sounddevice as sd
from pydub import AudioSegment
from scipy.io.wavfile import write


def as2np(audiosegment: AudioSegment):
    samples = audiosegment.get_array_of_samples()
    samples_float = librosa.util.buf_to_float(samples, n_bytes=audiosegment.frame_width, dtype=np.float32)
    if audiosegment.channels == 2:
        sample_left = np.copy(samples_float[::2])
        sample_right = np.copy(samples_float[1::2])
        sample_all = np.array([sample_left, sample_right])
    else:
        sample_all = samples_float

    return sample_all


def np2as(data: np.ndarray):
    audio_segment = AudioSegment(
        data.tobytes(),
        frame_rate=16000,
        sample_width=data.dtype.itemsize,
        channels=1
    )
    return audio_segment


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
    os.makedirs(output_dir, exist_ok=True)
    WAVE_OUTPUT_FILENAME = os.path.join(output_dir, f"{label}_{int(time.time())}.wav")  # 保存的文件名
    print(f"Recording: {label} -> {WAVE_OUTPUT_FILENAME}")
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
    return myrecording


if __name__ == "__main__":
    record_all()
