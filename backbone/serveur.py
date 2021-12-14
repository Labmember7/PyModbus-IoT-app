from pymodbus.version import version
from pymodbus.server.sync import StartTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext
from threading import Thread
import time

def run_slave():
    print("Modbus server/slave started...")
    # Tcp:
    StartTcpServer(context, address=("localhost", 12345))


def update_slave_values():
    #Updating holding registers
    while(True):
        f = open("vals.txt", "r")
        vals = f.read().split(" ")
        f.close()
        vals = [int(i) for i in vals]
        if store.getValues(3, 0, len(vals)) != vals:
            print("New temperature values : ",vals)
            store.setValues(3, 0, vals)
            print("Holding registers have been updated to => ", store.getValues(3, 0, 9))
        else:
            print(time.ctime()," | Temperature didn't change : ", vals)
        time.sleep(5)

if __name__ == '__main__':
    

    store = ModbusSlaveContext(
    di=ModbusSequentialDataBlock(0, [5]*10),
    co=ModbusSequentialDataBlock(0, [6]*10),
    hr=ModbusSequentialDataBlock(0, [7]*10),
    ir=ModbusSequentialDataBlock(0, [8]*10))
    
    '''
    di : Discrete Input
    co : Coils
    hr : Holding Registers
    ir : Internal registers
    '''

    context = ModbusServerContext(slaves=store, single=True)
    t1 = Thread(target=run_slave)
    t1.start()

    time.sleep(2)
    
    t2 = Thread(target=update_slave_values)
    t2.start()
    
    t1.join(1)
    t2.join(1)
