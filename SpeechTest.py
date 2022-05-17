import speech_recognition as sr


def runListener():
    r = sr.Recognizer()
    text = ''
    audio = ''
    mic = sr.Microphone()
    with mic as source2:
        # r.adjust_for_ambient_noise(source=source2,duration=0.2)
        print('listening ...')
        audio = r.listen(source2)
        print('recognising ...')
        text  = r.recognize_google(audio)
        
    return text
def takeInput(args):
    print(args)
    text=''
    while text=='' or text==None:
        text = runListener()
    print('voice input: '+text)
    return text

#---------------main--------------------------------------
vaName = 'Jessica'
args = 'hi.'
while True:
    cmd = takeInput(args)
    args = ''
    print(cmd)
    