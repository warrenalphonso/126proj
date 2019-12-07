import numpy as np
import sounddevice as sd
from scipy.io.wavfile import read, write
import os



#####################################################################################################################

### Import text from a .txt file and store it as a string 
filename = "test.txt"
contents = ""
with open(filename, "r") as f:
    contents = f.read()

### Convert contents to binary string bin_contents 
# Doesn't pad bit strings so they're of different lenghts - that's why I'm separating with spaces
bin_contents = "".join(format(ord(c), '08b') for c in contents) #08b means 0 pad and 8 length

### Frequency encodings in Hz
low_freq = 1000
# high_freq = 1000 # Chose something that's coprime with low_freq
high_freq = 2907 # Chose something that's coprime with low_freq


#####################################################################################################################



fs = 44100 # Usually 44100 or 48000 fps 
t = .01
wave = []
max_amp = 32767 # Signed 16 bit integers

for b in bin_contents:
    if b == '0':
        freq = low_freq 
    elif b == '1':
        freq = high_freq 
    else:
        print(b)    
    waveform = np.sin(2 * np.pi * freq * np.arange(t * fs) / fs) 
<<<<<<< HEAD
    waveform_ints = np.int16(waveform * 32767)
=======
    waveform_ints = np.int16(max_amp * waveform)
>>>>>>> f02b61f6841b45acb80a46f564ab01c9d23a764a
    wave = np.append(wave, waveform_ints)

print(np.shape(wave))

write('first_gen.wav', fs, wave.astype(np.dtype('i2')))

os.system("aplay first_gen.wav")
