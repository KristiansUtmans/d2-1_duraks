from flask import Flask, render_template, request
from file_proc import write_file, read_file

app = Flask(__name__)

@app.route('/')
def index():
  return "<a href ='/home'>Hey!</a>"

@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/about')
def about():
  return render_template('about.html', active_page = 'about')

@app.route('/contact')
def contact():
  return render_template('contact.html', phone = "1111111")

@app.route('/params')
def params():
  return render_template('params.html', args = request.args.to_dict())

@app.route('/post', methods = ['POST'])
def post():
  return request.get_json()

@app.route('/read_from_file')
def readFromFile():
  content = read_file()
  return content

@app.route('/write_to_file', methods = ['POST'])
def writeToFile():
  request_type = request.content_type
  if (request_type == "application/json"):
    contentJSON = request.get_json()
    write_file(contentJSON['data'])
    return contentJSON
  else:
    return f"Request type: '{request_type} not supported!"

@app.route('/get_file', methods = ['POST', 'GET'])
def get_file():
  if request.method == 'GET':
    return readFromFile()
  elif request.method == 'POST':
    return writeToFile()

if __name__ == '__main__':
  app.run(host = '0.0.0.0', port = 5211, threaded = True, debug = True)