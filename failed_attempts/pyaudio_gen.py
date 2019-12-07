# Copied from https://stackoverflow.com/questions/9770073/sound-generation-synthesis-with-python 

import math        #import needed modules
import pyaudio     #sudo apt-get install python-pyaudio

#####################################################################################################################

### Import text from a .txt file and store it as a string 
filename = "test.txt"
contents = ""
with open(filename, "r") as f:
    contents = f.read()

### Convert contents to binary string bin_contents 
# Doesn't pad bit strings so they're of different lenghts - that's why I'm separating with spaces
bin_contents = "".join(format(ord(c), 'b') for c in contents) 

### Frequency encodings in Hz
low_freq = 1000
high_freq = 11907 # Chose something that's coprime with low_freq

#####################################################################################################################

PyAudio = pyaudio.PyAudio     #initialize pyaudio

#See https://en.wikipedia.org/wiki/Bit_rate#Audio
BITRATE = 16000     #number of frames per second/frameset.      

#FREQUENCY = 2000     #Hz, waves per second, 261.63=C4-note.
LENGTH = .01     #seconds to play sound
WAVEDATA = ''

for b in bin_contents: 
    NUMBEROFFRAMES = int(BITRATE * LENGTH)
    RESTFRAMES = NUMBEROFFRAMES % BITRATE 

    if b == '0':
        FREQUENCY = low_freq
    elif b == '1': 
        FREQUENCY = high_freq
    else: 
        print(b)
    #generating waves
    for x in range(NUMBEROFFRAMES):
        WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

    for x in range(RESTFRAMES): 
        WAVEDATA = WAVEDATA+chr(128)




# if FREQUENCY > BITRATE:
#     BITRATE = FREQUENCY+100

# NUMBEROFFRAMES = int(BITRATE * LENGTH)
# RESTFRAMES = NUMBEROFFRAMES % BITRATE
# WAVEDATA = ''    

#generating waves
# for x in range(NUMBEROFFRAMES):
#  WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

# for x in range(RESTFRAMES): 
#  WAVEDATA = WAVEDATA+chr(128)

