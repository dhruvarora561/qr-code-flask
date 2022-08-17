import pyqrcode
import png
from flask import Flask
from flask import render_template
from flask import request
import os
from os.path import exists
from waitress import serve

app=Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def index():
    if request.method=='POST':
        qrstring=request.form.get('url_for_qr')
        if qrstring=='':
            return "please enter a url"
        else:
            qrcode=pyqrcode.create(qrstring)
            img=qrcode.png("static/qrcode.png",scale=6)
        return render_template('index.html')
    if os.path.exists('static/qrcode.png'):
        os.remove('static/qrcode.png')
    return render_template('index.html')




if (__name__)=='__main__':
#    app.run(debug=False)
     serve(app,url_scheme='https')