import wave
import numpy as np

def wav_to_array(wavpath):
    '''
    Takes a file path, returns a numpy array of samples
    as 16-bit integers.
    '''
    with wave.open(wavpath, 'rb') as wav:
        frames = wav.getnframes()
        wavbytes = wav.readframes(frames)
        wavarray = np.fromstring(wavbytes, np.int16)
    return wavarray

def clip_int(integer, clip):
    if abs(integer) > clip:
        if integer > 0:
            distorted_int = clip
        if integer < 0:
            distorted_int = -clip
    else:
        distorted_int = integer
    return distorted_int

def distort_audio(audioarray, clip):
    distorted_array = np.array(audioarray, dtype=np.int16)
    max_amplitude = max(audioarray)
    for i, value in enumerate(distorted_array):
        distorted_array[i] = clip_int(value) * max_amplitude * 0.4 / clip
    return distorted_array

def array_to_wav(array, wavpath):
    '''
    Save the given audio array as wavpath.
    Audio array should be 16-bit 44.1kHz mono audio signal
    '''
    with wave.open(wavpath, 'wb') as newwav:
        soundbytes = array.tobytes()
        newwav.setnchannels(1)
        newwav.setsampwidth(2)
        newwav.setframerate(44100)
        newwav.writeframes(soundbytes)

