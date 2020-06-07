# -*- coding: utf-8 -*-
"""
Created on Sun May 17 15:50:50 2020

@author: Dell
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle
import flasgger
from flasgger import Swagger

app=Flask(__name__)
Swagger(app)


f1=open('model.pkl','rb')
classifier=pickle.load(f1)

@app.route('/')
def welcome():
    return "Welcome to Front Page"


@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    """
    Authenticate Bank Note's
    ---
    parameters:
        -  name: variance
           in: query
           type: number
           required: true
        -  name: skewnesss
           in: query
           type: number
           required: true
        -  name: curtosis
           in: query
           type: number
           required: true
        -  name: entropy
           in: query
           type: number
           required: true
    responses:
           200:
               description: The output values

    """
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The predicted value is '+str(prediction)
    

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """
    Authenticate Bank Note's
    ---
    parameters:
        -  name: file
           in: formData
           type: file
           required: true
    responses:
           200:
               description: The output values

    """
    df_test=pd.read_csv(request.file.get("file"))
    prediction=classifier.predict(df_test)
    return str(list(prediction))




if __name__=='__main__':
    app.run()
    