import pyttsx3

engine = pyttsx.init()
with open('/out.txt') as f:
    lines = f.readlines()
engine.say(lines)
engine.runAndWait()
engine.runAndWait()