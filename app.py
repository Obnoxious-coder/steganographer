from flask import Flask,render_template,request

# coding=utf-8
import sys
import os
import glob
import re
import numpy as np
app = Flask(__name__)






@app.route("/")
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        print("file recieved")
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        
    return render_template('home.html')





if __name__ == '__main__':
    app.run(debug=True)