import gtts
import playsound


file_to_read = 'out.txt'
f = open(file_to_read, 'r')
file_text = f.read()
f.close()

filename = 'result.mp3'
# audio_created = gtts.gTTS(text=file_text, lang='en')
# audio_created.save('result.mp3')

playsound.playsound(filename)
