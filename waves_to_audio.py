# Following a guide at https://zach.se/generate-audio-with-python/
import gen_waves
import itertools 

channels = ((gen_waves.sine_wave(440.0),),
            (gen_waves.sine_wave(440.0),))

waves = (gen_waves.sine_wave(440.0), gen_waves.sine_wave(440.0))

# We're only going to play same sound through both channels of an audio file
# Returns a generator which yields sums of samples
def compute_samples(waves, nsamples=None):
    # islice: returns an iterator that returns elements from the input iterable
    # zip: takes in multiple iterables and returns an iterator of tuples with both entries
    # map: takes a function and multiple iteratables; returns an iterator that computes the function using arguments from each of the iterables 
    summed_waves = map(sum, zip(*waves))
    return itertools.islice(summed_waves, nsamples)


def compute_samples_2(channels, nsamples=None):
    one = (map(sum, zip(*channel)) for channel in channels)
    print(next(one))
    return itertools.islice(zip(*one), nsamples)
    return itertools.islice(zip(*(map(sum, zip(*channel)) for channel in channels)), nsamples)

#compute_samples((gen_waves.sine_wave(), gen_waves.sine_wave()), 100)
#compute_samples_2(channels)
compute_samples(waves)
