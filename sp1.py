import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)

volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
while True:


    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()
            engine.say(text)
            engine.runAndWait()
            print(f"Recognized {text}")





    except speech_recognition.UnknownValueError():
        engine.say('''sorry i did not get what you say''')
        recognizer = speech_recognition.Recognizer()
        continue
