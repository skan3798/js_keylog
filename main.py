from flask import Flask, jsonify, request, make_responnse, render_template
import json
from json import JSONEncoder

keylog = []

class Key:
  def __init__(self, time, key_up, key):
    self.time = time
    self.key_up = key_up
    self.key = key

  def toJSON(self):
    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def generateJSON(statusCode, statusMessage, payload):
  return jsonify({
    "statusCode": statusCode,
    "statusMessage": statusMessage,
    "payload": payload
  })

  return 0

#start flask app
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/js_keylog', methods=['POST'])
def addLog():
  # data = request.json
  # #requiredFields = ['time','key-down','key']
  # #check that required fields are in the post, otherwise bad request

  # time = data['time']
  # key_up = data['key-up']
  # key_pressed = data['key']

  # k = Key(time,key_up,key_pressed)

  # keys.append(k)

  # return k.toJSON(), 200

  # return data.toJSON(), 200
  return render_template('js_keylog.html')

@app.route('/js_keylog', methods=['GET'])
def showKeylog():

  return render_template('js_keylog.html')

