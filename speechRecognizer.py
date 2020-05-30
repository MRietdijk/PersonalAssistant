import speech_recognition as sr
from playsound import playsound

r = sr.Recognizer()
mic = sr.Microphone()

while 1:
    try:
        with mic as source:
             audio = r.listen(source)
        voice = r.recognize_google(audio)
        print(voice)
        if("Alex" in voice):
            if("what is my name" in voice):
                print("Your name is Mart Rietdijk. The best person in this entire universe")
            elif("lights off" in voice):
                print("Lights shutting off")
                playsound('./audio_files/lights_off.mp3')
    except:
        pass
