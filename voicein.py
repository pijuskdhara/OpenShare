#https://www.simplilearn.com/tutorials/python-tutorial/speech-recognition-in-python
import re
from threading import Thread
import time

import speech_recognition as sr

flag = True
text = ''
def callBack(recognizer, audio):
    global flag
    global text
    try:
        text  = recognizer.recognize_google(audio)
        print('CB: '+text)
        
        if text.strip()=='stop listening':
            flag = False
    except:
        print('error')
    

def runListener():
    r = sr.Recognizer()
    

    mic = sr.Microphone()
    with mic as source2:
        r.adjust_for_ambient_noise(source=source2,duration=0.2)
        # audio2 = r.listen(source2)
        # callBack(r,audio)
    audio = r.listen_in_background(mic,callBack)
def resetText():
    global text
    text = ''
def run(cline):
    print('Say somthing: ')
    runListener()
    
    while True:
        # print('>> '+text)
        cline[1] = text
        resetText()
        time.sleep(1)
cmd = [1,2]
run(cmd)
# print(cmd)
