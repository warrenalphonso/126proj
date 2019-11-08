# Following a guide at https://zach.se/generate-audio-with-python/
import itertools
import math
import random

# Returns generator of sine wave 
def sine_wave(freq=440.0, framerate=44100, amp=0.5):
    period = int(framerate / freq)
    if amp > 1.0: amp = 1.0
    if amp < 0.0: amp = 0.0
    lookup_table = [float(amp) * math.sin(2.0 * math.pi * float(freq) * (float(i % period) / float(framerate))) for i in range(period)]
    return (lookup_table[i % period] for i in itertools.count(0))

# Completely random audio with amplitude half our sine amplitude
def white_noise(amp=0.5):
    framerate = 44100
    noise_gen = (float(amp) * random.uniform(-1, 1) for _ in itertools.count(0))
    return itertools.cycle(itertools.islice(noise_gen, framerate))

