from flask import Flask,request, jsonify
from dataclasses import dataclass
app = Flask(__name__)

@dataclass
class Result:
    result : int

@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    de = Result(data["first"] + data["second"])
    return jsonify(de)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()
    de = Result(data["first"] - data["second"])
    return jsonify(de)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
