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
        f = open("vals.txt", "w")
        f.write(str(temp1)+" "+str(temp2)+" " +str(temp3))
        f.close()
    return jsonify(response_object)


# def run_slave():
#     print("Modbus server/slave started...")
#     # Tcp:
#     StartTcpServer(context, address=("localhost", 12345))


# def update_slave_values():
#     #Updating holding registers
#     while(True):
#         print([temp1,temp2,temp3])
#         store.setValues(3, 0, [temp1,temp2,temp3])
#         print("New holding registers are : ", store.getValues(3, 0, 9))
#         time.sleep(4)
        
        
if __name__ == '__main__':
    #Creating the pymodbus server
    # store = ModbusSlaveContext(
    #     di=ModbusSequentialDataBlock(0, [5]*10),
    #     co=ModbusSequentialDataBlock(0, [6]*10),
    #     hr=ModbusSequentialDataBlock(0, [7]*10),
    #     ir=ModbusSequentialDataBlock(0, [8]*10))

    # '''
    # di : Discrete Input
    # co : Coils
    # hr : Holding Registers
    # ir : Internal registers
    # '''

    # context = ModbusServerContext(slaves=store, single=True)
    # t1 = Thread(target=run_slave)
    # t1.start()
    # time.sleep(2)

    # t2 = Thread(target=update_slave_values)
    # t2.start()

    # t1.join(1)
    # t2.join(1)

    # time.sleep(2)
    #Running the flask app
    app.run()
