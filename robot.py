from gtts import gTTS
import playsound
print("Hey!, Welcome To Robot Speaker")
while True:
    n=input("What do you want me to speak. Enter (q) if you want to quit :")
    if n=="q":
        bye=gTTS(text="Bye",lang="en")
        bye.save("bye.mp3")
        playsound.playsound("bye.mp3")
        break
    voice=gTTS(text=n,lang="en")
    voice.save("voice.mp3")
    playsound.playsound("voice.mp3")
        
