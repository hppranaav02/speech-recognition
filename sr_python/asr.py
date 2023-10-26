#From https://towardsdatascience.com/building-a-speech-recognizer-in-python-2dad733949b4

# import the speech recognition module
import speech_recognition as sr

# define the speech recognizer
r = sr.Recognizer()

# define the input audio file
audio_file = sr.AudioFile('../honnavalli_pradeep_pranaav.wav')

# perform the actual speech recognition
with audio_file as source: 
   r.adjust_for_ambient_noise(source) 
   audio = r.record(source)

# get the transcription of the speech 
result_google = r.recognize_google(audio)
result_sphinx = r.recognize_sphinx(audio)

# print the results 
with open('result_google.txt',mode ='w') as file: 
   file.write(result_google) 
   print("ASR ready: written in file result_google.txt")

with open('result_sphinx.txt',mode ='w') as file: 
   file.write(result_sphinx) 
   print("ASR ready: written in file result_sphinx.txt")