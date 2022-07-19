from flask import Flask, render_template, request
import json


app = Flask(__name__)
data =[]
file_data = ""

@app.route('/webhook', methods=['POST'])
def index():
    data1 = request.get_json(force=True)

    data.append(data1)

    return "sucess"


@app.route('/listner', methods=['GET'])
def data_listner():
    if len(data)==0:
        data.append({"data":"NO data found"})
    json_formatted_str = json.loads(json.dumps(data[-1], indent=4))
    return render_template('listner.html', data=json_formatted_str)

@app.route('/filewebhook', methods=['PUT'])
def upload():
    file_data = request.data
    return 'OK'

@app.route('/filelistner', methods=['GET'])
def data_listner():
    return render_template('filelistner.html', data=file_data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

