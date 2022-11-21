from flask import Flask
from flask import jsonify

app=Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status_code': 1,'message':'successfully enrouted to home'})

@app.route('/playground')
def playground():
    return jsonify({'status_code':1,'message':'successfully enrouted to playground'})

@app.route('/theatre')
def theatre():
    return jsonify({'status_code':1,'message':'successfully enrouted to Movie Theatre'})

if __name__=="__main__":
    app.run()
