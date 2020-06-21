from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/my-link/')
def my_link():
  os.system('python3 main.py --text "Hello" --quiet "-"')

  return 'haha'

if __name__ == '__main__':
  app.run(debug=True)