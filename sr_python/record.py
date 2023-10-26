# Record 60 seconds of audio with sample frequency 16kHz
import sounddevice as sd
from scipy.io.wavfile import write

fs = 16000  # Sample rate
seconds = 60  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)  # Save as WAV file 

# The wav-file has not the right format.
# Use pydub to convert
from pydub import AudioSegment
sound = AudioSegment.from_file('output.wav',format="wav",frame_rate=16000,channels=1)
sound_out = sound.set_sample_width(2)
sound_out.export('output.wav', format="wav")