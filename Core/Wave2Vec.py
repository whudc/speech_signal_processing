import numpy as np
import torch
from huggingsound import SpeechRecognitionModel
from scipy.io.wavfile import write as write_wav
from tqdm import tqdm
from transformers import Wav2Vec2ForSequenceClassification, Wav2Vec2FeatureExtractor

from Core import SDRBase, EN_LABELS, ZH_LABELS
from Utils.record import as2np


class SdrEnModel(SDRBase):
    def __init__(self):
        super(SdrEnModel, self).__init__()
        self.model_name = "skpawar1305/wav2vec2-base-finetuned-digits"
        self.model = Wav2Vec2ForSequenceClassification.from_pretrained(self.model_name)
        self.feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(self.model_name)

    def inference(self, chunk):
        inputs = self.feature_extractor(chunk, sampling_rate=16000, padding=True, return_tensors="pt")

        logits = self.model(**inputs).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        labels = [self.model.config.id2label[_id] for _id in predicted_ids.tolist()]
        if not len(labels):
            return None
        return labels[0]

    def predict_single(self, chunk: np.ndarray):
        label = self.inference(chunk)
        if label is None:
            return None
        if label not in EN_LABELS:
            return None
        return label

    def predict_seq(self, data: np.ndarray):
        chunks = self._split_singles(data)
        labels = []
        for chunk in tqdm(chunks):
            # sd.play(as2np(chunk), samplerate=16000)
            # sd.wait()
            label = self.predict_single(chunk)
            if label is not None:
                labels.append(label)
        return labels


class SdrZhModel(SDRBase):
    def __init__(self):
        super(SdrZhModel, self).__init__()
        self.model = SpeechRecognitionModel("wbbbbb/wav2vec2-large-chinese-zh-cn")

    def __dump_test_file(self, data):
        test_file = 'test_inference.wav'
        write_wav(test_file, 16000, data)  # Save as WAV
        return test_file

    def inference(self, chunk):
        dataset = [self.__dump_test_file(chunk)]
        preds = self.model.transcribe(dataset)[0]['transcription']  # string
        return list(preds)

    def predict_single(self, chunk: np.ndarray):
        labels = self.inference(chunk)
        if not len(labels):
            return None
        label = labels[0]
        if label is None:
            return None
        if label not in ZH_LABELS:
            return None
        return label

    def predict_seq(self, data: np.ndarray):
        labels = self.inference(data)
        labels = [label for label in labels if label in ZH_LABELS]
        return labels
