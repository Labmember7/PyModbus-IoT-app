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
    while (True):
        time.sleep(4)
        print("Reading temperature registers ...")
        rr2 = client.read_holding_registers(0, 9, unit=UNIT)
        print(rr2.registers[0:3])
        try:
            if max(rr2.registers)>30:
                print("Temperature is high -> AC is ON")
                m.onButton()
            else:
                print("Temperature is ok  -> AC is OFF")
                m.offButton()
        except:
            client.close()
            quit()

#----------------------------------------------------------------------
if __name__ == '__main__':
    
    print("Running client/Master")
    client = ModbusClient('localhost', port=12345)
    client.connect()
    Thread(target=run_sync_client).start()

    #Launching UI
    root = Tk()
    m = MainWindow(root)
    Thread(target=root.mainloop()).start()
    


