from gtts import gTTS
from playsound import playsound
from os import remove

def english_lang(text):
	tts = gTTS(text,lang='en')
	tts.save(r"audio/en_audio.mp3")
	playsound(r"audio/en_audio.mp3")

def arabic_lang(text):
	tts = gTTS(text,lang='ar')
	tts.save("audio/ar_audio.mp3")
	playsound(r"audio/ar_audio.mp3")

def deutsch_lang(text):
		tts = gTTS(text,lang='de')

		tts.save(r"/du_audio.du_audio.mp3")
		playsound(r"/du_audio.du_audio.mp3")
		remove(r"/du_audio.du_audio.mp3")
