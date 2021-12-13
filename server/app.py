from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodbus.client.sync import ModbusTcpClient as ModbusClient

# configuration
DEBUG = True
temp1 = 0
temp2 = 0
temp3 = 0
# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/', methods=['GET', 'POST'])
def update_temperature():
    response_object = {'status': 'Temperature updated succesfully!'}
    if request.method == 'POST':
        post_data = request.get_json()
        temp1 = post_data.get("temp1")
        temp2 = post_data.get("temp2")
        temp3 = post_data.get("temp3")
        print(temp1, temp2, temp3)
        print("Writing new temperature values ...")
        wr = client.write_registers(1, [temp1, temp2, temp3])
    return jsonify(response_object)


if __name__ == '__main__':
    client = ModbusClient('localhost', port=12345)
    client.connect()
    app.run()
