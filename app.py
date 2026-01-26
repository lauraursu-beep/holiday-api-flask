from flask import Flask, jsonify, render_template,request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def create_table():
    with open('file.json', 'r')as file:
        holidays = json.load(file)

    return render_template('table.html', data=holidays)

@app.route('/jsonify', methods=['GET'])
def get_holiday():
    with open('file.json', 'r') as f:
        holidays = json.load(f)
    return jsonify(holidays)  

@app.route('/holiday', methods=['POST'])
def create_holiday():
    holidays = request.get_json()
    return jsonify({
        'message': 'Holiday created',
        'holiday': holidays
    }), 201


if __name__ == '__main__':
    app.run(debug=True)

