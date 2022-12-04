<h1 align="center"> IoT APP using PyModbus </h1> 

This is a project that simulates an IoT system. It consists of an air conditioner, three seperate heat sensors and a Modbus server (equivalent to Modbus Card).

<img src="https://user-images.githubusercontent.com/60778237/205506997-04f1a1b4-e267-43eb-9d0a-354a1d31b5b5.png" width="200" /> 
 
<h2 align="center"> Code structure  </h2> 


<div align="center"> 
    <img src="https://user-images.githubusercontent.com/60778237/205507784-10a68935-9e96-4bfb-a386-9e1f64a16243.png" width="500" />
    
    <The global structure of the project>
</div>


The code is structured as follows :


1- The client == climatiseur (Air conditioner) in `backbone\climatiseur.py` : A modbus client that receives an order from the modbus server to whether turn ON/OFF the air conditioner 

    - ON if at least one among the the three sensors detected a temperature >= 30°C.
    - OFF else.
    - Used `tkinter` to show the status of the air conditioner.

2- The Modbus server represented by the `backbone\serveur.py` : This file is responsible for starting a TCP server.
    
    - Reads the temperature values of the sensors from the file `backbone\vals.txt`  every 5 seconds and saves it into 3 different memory blocks.
    - It emits the values of these blocks every two seconds for the clients available (listening).
    
3- The sensors represented by the `front\` folder which is a VueJS app :
    
    - It consists of a UI containing three temperature sliders to modify each representing the captured temperature.
    - A button to send the values using a Http POST request to the `backbone\app.py`, which is a flask api that saves the received values into a the file `backbone\vals.txt`.

<div align="center"> 
    <img src="https://user-images.githubusercontent.com/60778237/205505008-7539241d-b792-4d9f-baf2-6eda317210f8.png" width="500" />

    <The temperature sliders UI for the corresponding sensors>
</div>

4- The flask API using `backbone\app.py` :
    
    - An exposed API to receive the POST requests from the sensors (the front vue app).
    - Saves the received requests into `backbone\vals.txt`.

 
## Want to use this project?

1. Fork/Clone

2. Run the modbus server in one terminal window:

    ```sh
    $ cd backbone
    $ python -m venv env
    $ source env/bin/activate 
    (env)$ pip install -r requirements.txt
    (env)$ python serveur.py
    ```

    Navigate to [http://localhost:PORT](http://localhost:PORT)
    
2. Run the server-side modbus client in another terminal window:
    
    ```sh
    (env)$ python climatiseur.py
    ```
    
2. Run the server-side Flask app in another terminal window:

    ```sh
    (env)$ python app.py
    ```

3. Run the front Vue app in a different terminal window:
    ```sh
    $ cd ..
    $ cd front
    $ npm install
    $ npm run serve
    ```

Navigate to [http://localhost:8080](http://localhost:8080). 
    
Now you can modify the temps in the front app. I suggest you try having only one value over 30 while the others are below, and another try by having all the values below 30 and look at the UI window opened by the `climatiseur.py` script. The air conditioner will turn ON and OFF correspondingly.

## Conclusion

This is just a simulation scenario for learning purposes.
    
## References

- VueJS https://vuejs.org/
- Pymodbus https://pymodbus.readthedocs.io/en/latest/
- Flask https://flask.palletsprojects.com/en/2.2.x/
    
