import speech_recognition as sr
from playsound import playsound
import RPi.GPIO as GPIO
import os

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(26,GPIO.OUT)
r = sr.Recognizer()
mic = sr.Microphone()

while 1:
    try:
        with mic as source:
             audio = r.listen(source)
        voice = r.recognize_google(audio)
        print(voice)
        
        if("what is my name" in voice):
            print("Your name is Mart Rietdijk. The best person in this entire universe")
        elif("lights off" in voice):
            print("Lights shutting off")
            GPIO.output(26, GPIO.LOW)
            playsound('./audio_files/lights_off.mp3')
        elif("lights on" in voice):
            print("Lights on")
            GPIO.output(26, GPIO.HIGH)
    except:
        pass
