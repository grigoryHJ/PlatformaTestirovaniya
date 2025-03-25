from vosk import Model, KaldiRecognizer
from gtts import gTTS
from playsound import playsound
import pyaudio
import wave
import os
import json


def transcribe(output, model_path, sec):
    CHUNK = 1024
    FRT = pyaudio.paInt16
    CHAN = 1
    RT = 44100
    REC_SEC = sec

    p = pyaudio.PyAudio()

    stream = p.open(format=FRT, channels=CHAN, rate=RT, input=True, frames_per_buffer=CHUNK)
    print("rec")
    frames = []
    for i in range(0, int(RT / CHUNK * REC_SEC)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("done")
    stream.stop_stream()
    stream.close()
    p.terminate()

    w = wave.open(output, 'wb')
    w.setnchannels(CHAN)
    w.setsampwidth(p.get_sample_size(FRT))
    w.setframerate(RT)
    w.writeframes(b''.join(frames))
    w.close()

    model = Model(model_path)
    wf = wave.open(output, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            print("Процесс распознавания...")  # Логирование процесса

    result = rec.FinalResult()
    with open("output.json", 'w') as file:
        file.write(result)
    with open("output.json", "r") as f:
        data = json.loads(f.read())
        print(data['text'])
    # return result


def speak(text, lang='ru'):
    output = "output.mp3"
    tts = gTTS(lang=lang, text=text)
    tts.save(output)
    playsound(output)
    os.remove(output)
