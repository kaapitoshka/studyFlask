from flask import Flask,jsonify, abort
from sqlt import *


empl = [
    {
        "Name": "Junky",
        "Position":"Admin",
        "Tel.":"88005553535",
        "id":1
    },
    {
        "Name": "Funky",
        "Position": "ex-admin",
        "Tel.": "9990001234",
        "id": 2

    }
]
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return """<h1>Hello Username</h1>"""

@app.route('/todo/api/v1.0/empl', methods=["GET"])
def get_tasks():
    return jsonify({'List of empl': qur})

@app.route('/todo/api/v1.0/empl/<int:emp_id>', methods=["GET"])
def get_tasks1(emp_id):
    dd=[x for x in qur if x[0]==emp_id]
    if len(dd)==0:
        abort(404)
    else:
        return jsonify({'empl is': dd})

if __name__ == '__main__':
    app.run(port=8877, debug=True)