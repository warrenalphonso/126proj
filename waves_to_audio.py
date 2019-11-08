# Following a guide at https://zach.se/generate-audio-with-python/
import gen_waves
import itertools 
import wave
import struct

waves = (gen_waves.sine_wave(440.0), gen_waves.sine_wave(440.0))

# We're only going to play same sound through both channels of an audio file
# Returns a generator which yields sums of samples
def compute_samples(waves, nsamples=None):
    # islice: returns an iterator that returns elements from the input iterable
    # zip: takes in multiple iterables and returns an iterator of tuples with both entries
    # map: takes a function and multiple iteratables; returns an iterator that computes the function using arguments from each of the iterables 
    summed_waves = map(sum, zip(*waves))
    return itertools.islice(summed_waves, nsamples)

samples = compute_samples(waves)

sampwidth = 2 # size of sample in bytes - we have 16 bit audio 
framerate = 44100 
duration = 5 # in seconds
nframes = framerate * duration
w = wave.open('audio.wav', 'w')
w.setparams((1, sampwidth, framerate, nframes, 'NONE', 'not compressed'))

max_amplitude = 32767.0 
samples = (int(sample * max_amplitude) for sample in samples)

struct.pack('h', 1000)
