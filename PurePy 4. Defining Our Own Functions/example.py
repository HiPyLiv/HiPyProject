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

def reverse_audio(audioarray):
    return np.flipud(audioarray)

reverse_audio = np.flipud

def clip_int(integer, clip, boost):
    '''
    Reduces the absolute value of an integer
    to clip, the scales the integer up by factor boost.
    Returns an integer
    '''
    if abs(integer) > clip:
        if integer > 0:
            dist = clip
        if integer < 0:
            dist = -clip
    else:
        dist = integer
    return int(dist * boost)

def distort_audio(audioarray, clip):
    '''
    Distorts audio signal by clipping it beyond
    a certain magnitude.
    Returns distorted copy.
    '''
    boost = max(audioarray) * 0.4 / clip
    clipped_array = np.zeros(len(audioarray), dtype=np.int16)
    for i, value in enumerate(audioarray):
        clipped_array[i] = clip_int(value, clip, boost)
    return clipped_array

def echo_audio(audioarray, decay, time):
    '''
    Simple echo effect. Takes decay factor and
    time lag as floats (time in seconds).
    '''
    frames = int(time*44100)
    # Empty array twice length of original
    echo_array = np.zeros(len(audioarray)*2, dtype=np.int16)
    # copy audioarray into the echoarray
    echo_array[:len(audioarray)] = audioarray
    
    # add the echo effect
    for i,value in enumerate(echo_array):
        if value != 0:
            echo_array[i+frames] += int(value*decay)
    return echo_array

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

