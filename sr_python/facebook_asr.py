import librosa

#Importing Pytorch
import torch

#Importing Wav2Vec
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer

# Loading the audio file

audio, rate = librosa.load("../honnavalli_pradeep_pranaav.wav", sr = 16000)

tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

input_values = tokenizer(audio, return_tensors = "pt").input_values

# Storing logits (non-normalized prediction values)
logits = model(input_values).logits

# Storing predicted ids
prediction = torch.argmax(logits, dim = -1)

# Passing the prediction to the tokenzer decode to get the transcription
transcription = tokenizer.batch_decode(prediction)[0]

file = open('result_facebook.txt', mode='w+')
file.write(transcription.lower())