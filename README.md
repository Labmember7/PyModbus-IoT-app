<h1 align="center"> Iot App using modbus </h1> 

This is a project that simulates an Iot system. It consists of an air conditioner, three seperate heat sensors and a Modbus server (equivalent to Modbus Card)

<img src="https://user-images.githubusercontent.com/60778237/205506997-04f1a1b4-e267-43eb-9d0a-354a1d31b5b5.png" width="200" />

<div align="center"> 
<img src="https://user-images.githubusercontent.com/60778237/205505008-7539241d-b792-4d9f-baf2-6eda317210f8.png" width="500" />
</div>

<div align="center"> 
<img src="https://user-images.githubusercontent.com/60778237/205507784-10a68935-9e96-4bfb-a386-9e1f64a16243.png" width="500" />
</div>


![image]()

## Want to use this project?

1. Fork/Clone

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3.9 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ python app.py
    ```

    Navigate to [http://localhost:5000](http://localhost:5000)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run serve
    ```

    Navigate to [http://localhost:8080](http://localhost:8080)
