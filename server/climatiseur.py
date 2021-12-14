from pymodbus.client.sync import ModbusTcpClient as ModbusClient
from tkinter import *
from threading import Thread
import time
UNIT = 0x1


class MainWindow():

    #----------------

    def __init__(self, main):

        # canvas for image
        self.canvas = Canvas(main,width=400,height=400)
        self.canvas.grid(row=0, column=0)

        # images
        self.my_images = []
        self.my_images.append(PhotoImage(file="off.png"))
        self.my_images.append(PhotoImage(file="on.png"))
        self.my_image_number = 0

        # set first image on canvas
        self.image_on_canvas = self.canvas.create_image(
            0, 0, anchor='nw', image=self.my_images[self.my_image_number])

        # button to change image
        self.button = Button(main, text="ON/OFF", command=self.onButton)
        self.button.grid(row=1, column=0)

    #----------------

    def onButton(self):
        # next image
        self.my_image_number = 1
        # change image
        self.canvas.itemconfig(self.image_on_canvas,
                               image=self.my_images[self.my_image_number])

    #----------------
   #----------------

    def offButton(self):
        # next image
        self.my_image_number = 0
        # change image
        self.canvas.itemconfig(self.image_on_canvas,
                               image=self.my_images[self.my_image_number])

    #----------------

def run_sync_client():
    i = 0
    while (i < 50):
        print("Reading temperature registers ...")
        #wr = client.write_registers(1, [7, 21, 77])
        rr2 = client.read_holding_registers(0, 7, unit=UNIT)
        print(rr2.registers)

        time.sleep(3)
        try:
            if max(rr2.registers)>30:
                m.onButton()
            else:
                print("Temperature is ok !")
                m.offButton()
        except:
            quit()
        i += 1
    client.close()
    # arguments = {
    # 'read_address':    1,
    # 'read_count':      3,
    # 'write_address':   1,
    # 'write_registers': [20,21,23],
    # }
    # print("Read write registeres simulataneously")
    # rq = client.readwrite_registers(unit=UNIT, **arguments)
    # rr = client.read_holding_registers(1, 3, unit=UNIT)
    # print(rq.registers)
    # print(rr.registers)
    #client.close()

#----------------------------------------------------------------------
if __name__ == '__main__':
    
    print("Running client")
    client = ModbusClient('localhost', port=12345)
    client.connect()
    Thread(target=run_sync_client).start()

    print("Launching UI")
    root = Tk()
    m = MainWindow(root)
    Thread(target=root.mainloop()).start()
    


