# qr-code-flask
A web app which can generate QR codes.
In order to install first clone the project then create a virtual environment using 

```
python -m venv env
```

then activate the virtual evironment by first changing the directory then running ``` activate ``` command.
this app is configured to waitress WSGI, this is a production WSGI server. This will run on 127.0.0.1:8080. People usually use some sort of reverse proxy in front of waitress.

In order to run the app just type 
```
python app.py
```
