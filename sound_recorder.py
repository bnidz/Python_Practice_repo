
import pyaudio
import wave
import sys

import sounddevice as sd
import soundfile as sf

import numpy
from scipy.io.wavfile import write

import speech_recognition as sr


def Record():
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 5
    WAVE_OUTPUT_FILENAME = "file.wav"

    audio = pyaudio.PyAudio()

    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print ("recording...")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")


    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    RegocnizeFile()
    Playback_()
    #ReverseFile()

def Playback_():
    filename = 'file.wav'
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    #Exit()


def ReverseFile():

    ifile = wave.open("file.wav")
    samples = ifile.getnframes()
    audio = ifile.readframes(samples)

    # Convert buffer to float32 using NumPy
    audio_as_np_int16 = numpy.frombuffer(audio, dtype=numpy.int16)
    audio_as_np_float32 = audio_as_np_int16.astype(numpy.float32)

    # Normalise float32 array so that values are between -1.0 and +1.0
    max_int16 = 2**15
    audio_normalised = audio_as_np_float32 / max_int16

    reversedFile = audio_normalised[::-1]

    #data = np.random.uniform(-1,1,44100) # 44100 random samples between -1 and 1
    sf.write('file.wav', reversedFile, 44100)
    Playback_()

def RegocnizeFile():
    r = sr.Recognizer()

    with sr.AudioFile("file.wav") as source:
        audio = r.record(source)
    try:
        s = r.recognize_google(audio)
        print("Text: "+s)
    except Exception as e:
        print("Exception: "+str(e))
        Exit()

def Exit():
    print("Finished Playback")
    sys.exit(0)

Record()
