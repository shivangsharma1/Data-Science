# -*- coding: utf-8 -*-
"""
Created on Sun May 17 14:20:23 2020

@author: Dell
"""

from flask import Flask,request
import pandas as pd
import numpy as np
import pickle

app=Flask(__name__)
f1=open('model.pkl','rb')
classifier=pickle.load(f1)

@app.route('/')
def welcome():
    return "Welcome to Front Page"


@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return 'The predicted value is '+str(prediction)
    

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.file.get("file"))
    prediction=classifier.predict(df_test)
    return 'The predicted value is for the csv_file '+str(list(prediction))




if __name__=='__main__':
    app.run()
    