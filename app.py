from flask import Flask, render_template, request
import os
import gtts
import playsound

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/', methods=['GET','POST'])
def my_link():
  if request.method == 'POST':
    option = request.form['sentence']
    cmd = 'python3 printer.py --text "%s" --quiet "-"'%(option)
    os.system(cmd)
    file_to_read = 'out.txt'
    f = open(file_to_read, 'r')
    file_text = f.read()
    f.close()

    audio_created = gtts.gTTS(text=file_text, lang='en')
    audio_created.save('result.mp3')
    

    file = open("out.txt")
    line = file.read().replace("\n"," ")
    file.close()
    
    
  return render_template("index.html",out = line)

@app.route('/speak/', methods =['GET','POST'])
def speak():
  playsound.playsound('result.mp3')


if __name__ == '__main__':
  app.run(debug=True)