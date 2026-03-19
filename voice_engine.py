import pyttsx3
import whisper
import sounddevice as sd
from scipy.io.wavfile import write

# Initialize once
engine = pyttsx3.init()
model = whisper.load_model("base")

# ----------------------------
# SAFE SPEAK FUNCTION
# ----------------------------
def speak(text):
    print("Assistant:", text)
    try:
        engine.stop()  # stop previous speech
        engine.say(text)
        engine.runAndWait()
    except:
        pass  # prevents crash completely


# ----------------------------
# LISTEN FUNCTION (IMPROVED)
# ----------------------------
def listen():
    duration = 5
    fs = 44100

    speak("Listening... Speak clearly")

    try:
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()

        write("voice.wav", fs, recording)

        result = model.transcribe("voice.wav")
        text = result["text"].strip().lower()

        if text == "":
            return None

        speak(f"You: {text}")
        return text

    except:
        return None