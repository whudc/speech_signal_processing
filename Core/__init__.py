from abc import ABC

import numpy as np

from pydub import AudioSegment
from pydub.silence import split_on_silence
import sounddevice as sd
from scipy.io.wavfile import write as write_wav
from Utils.record import as2np
import os
EN_LABELS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ZH_LABELS = ['一', '二', '三', '四', '五', '六', '七', '八', '九', '零']


class SDRBase(ABC):
    """Speech Digit Recognition Base"""

    def __init__(self, ):
        pass

    def predict_single(self, data: np.ndarray):
        raise NotImplemented()

    def predict_seq(self, data: np.ndarray):
        raise NotImplemented()

    def _split_singles(self, data):
        test_file = 'test_inference.wav'
        write_wav(test_file, 16000, data)  # Save as WAV
        as_data = AudioSegment.from_wav(test_file)
        # as_data = np2as(data)
        db = as_data.dBFS
        # sd.play(as2np(as_data), samplerate=16000, blocking=True)
        chunks = split_on_silence(as_data, min_silence_len=20, keep_silence=40, silence_thresh=db - 5)
        chunks = [as2np(chunk) for chunk in chunks]
        os.remove(test_file)
        return chunks
