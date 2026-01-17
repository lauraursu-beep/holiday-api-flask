from flask import Flask, jsonify,request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_holiday():
    with open('file.json', 'r') as f:
        data = json.load(f)
    return jsonify(data)  

@app.route('/holiday', methods=['POST'])
def create_holiday():
    data = request.get_json()
    return jsonify({
        'message': 'Holiday created',
        'holiday': data
    }), 201


if __name__ == '__main__':
    app.run(debug=True)

