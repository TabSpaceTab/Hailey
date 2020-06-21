from flask import Flask, render_template, request
import os

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

    file = open("out.txt")
    line = file.read().replace("\n"," ")
    file.close()
    
  return render_template("index.html",out = line)

if __name__ == '__main__':
  app.run(debug=True)