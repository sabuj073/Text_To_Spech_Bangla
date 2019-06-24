from gtts import gTTS
import playsound

myText ="আমি মেহেদি হাসান সবুজ"
myobj = gTTS(text=myText, lang="bn", slow=False)
myobj.save("talk.mp3")
playsound.playsound("talk.mp3", True)