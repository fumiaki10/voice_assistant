import sounddevice as sd
import soundfile as sf
import speech_recognition as sr

filename = "voice.wav"
seconds = 5
samplerate = 44100

print("録音開始。5秒話してください。")
audio = sd.rec(int(seconds * samplerate), samplerate=samplerate, channels=1)
sd.wait()

sf.write(filename, audio, samplerate)
print("録音完了。音声認識します。")

recognizer = sr.Recognizer()

with sr.AudioFile(filename) as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data, language="ja-JP")
    print("認識結果:", text)
except sr.UnknownValueError:
    print("聞き取れませんでした")
except sr.RequestError as e:
    print("音声認識サービスに接続できませんでした:", e)