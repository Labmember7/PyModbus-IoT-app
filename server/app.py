from flask import Flask, jsonify, request
from flask_cors import CORS
from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from threading import Thread
import time
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
        update_slave_values(new_vals=[temp1,temp2,temp3])
    return jsonify(response_object)


def run_slave():
    print("Modbus server started...")
    # Tcp:
    StartTcpServer(context, address=("localhost", 12345))


def update_slave_values(new_vals=[0,0,0]):
    store.setValues(3, 0, new_vals)
    print(store.getValues(3, 0, len(new_vals)))
        
if __name__ == '__main__':
    #Creating the pymodbus server
    store = ModbusSlaveContext(
        di=ModbusSequentialDataBlock(0, [5]*10),
        co=ModbusSequentialDataBlock(0, [6]*10),
        hr=ModbusSequentialDataBlock(0, [7]*10),
        ir=ModbusSequentialDataBlock(0, [8]*10))

    context = ModbusServerContext(slaves=store, single=True)
    t1 = Thread(target=run_slave)
    t1.start()
    t1.join(2)
    #Running the flask app
    app.run()
