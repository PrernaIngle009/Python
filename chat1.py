from gtts import gTTS
import playsound
import sys
say=gTTS(text="Welcome,I am a Robo, How May I help You",lang="en")
say.save("Welcome.mp3")
playsound.playsound("Welcome.mp3")
sys.path.append("C:/Python/chat.py")
from chat import *
print(responses[0])
print(responses[1])
while True:
    text=input("Please Ask:")
    if text=="q":
        bye=gTTS(text="Alright See You NextTime!",lang="en")
        bye.save("bye.mp3")
        playsound.playsound("bye.mp3")
        print(responses[3])
    for w in text.split():
        if w.upper()in operations.keys():
            try:
                l=extract_num(text)
                r=operations[w.upper()](l[0],l[1])
                print(r)
                break
            except:
                print("Please ask correct question")
                break
        elif w.upper() in commands.keys():
            commands[w.upper()]()
            break
        else:
            print(responses[4])
            print(responses[5])
