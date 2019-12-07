import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write 

fs = 44100 # Usually 44100 or 48000 fps 

duration = 5  # seconds
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
sd.wait()
sd.stop()

print(np.shape(myrecording))

print('Done recording')

write('test_output.wav', fs, myrecording)

# Make sure when you do `python -m sounddevice` or `sd.query_devices()`, you're connected to both *in* and *out* channels. 

