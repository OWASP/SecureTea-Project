# -*- coding: utf-8 -*-
u""" WAF ML Module .

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Shaik Ajmal R <shaikajmal.r2000@gmail.com>
    Version:
    Module: SecureTea

"""

import pandas as pd
import warnings
import pickle
import joblib
from pathlib import Path
import os

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.compose import ColumnTransformer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from .utils import get3Grams



class WAF:
    """
    Class responsible for training a ML model that uses GaussianNB classifier and also predict
    the class of live features from the incoming request

    """

    def __init__(self,live_data):


        """

        A class that initialise the required variables

        """


        self.live_data=[live_data]



        datapath = Path(os.path.dirname(__file__)).parent / "data/data_updated.csv"
        modelpath = Path(os.path.dirname(__file__)).parent / "data/modeltestgram.sav"



        self.DATA_PATH = datapath
        self.MODEL_PATH = modelpath



        self.data=pd.read_csv(self.DATA_PATH,encoding="cp1252")


        self.target = self.data["label"]
        self.path_vectorizer = TfidfVectorizer(tokenizer=get3Grams,encoding="cp1252")
        self.body_vectorizer = TfidfVectorizer(tokenizer=get3Grams,encoding="cp1252")
        self.model=GaussianNB()

        # Feature selection

        self.X=self.data[['path','body','path_len']]

        self.X_train,self.X_test,self.Y_train,self.Y_test=train_test_split(self.X,self.target,test_size=0.2)






    def train_model(self):

        """
        A method that is responsible for training a model from the given dataset and dumping the object file .

        Args: None
        Returns: None


        """

        # Column Transformer

        self.column_transformer = ColumnTransformer([('tf-1', self.path_vectorizer, 'path'),('tf-2',self.body_vectorizer,'body'),], remainder='passthrough', sparse_threshold=0)

        # Creating Pipeline

        self.pipe = Pipeline([

                  ('TF_IDF Vectorizer', self.column_transformer),
                  ('run_model', self.model)
                ])

        # Train Model

        self.pipe.fit(self.X_train,self.Y_train)

        with open("model", "wb") as f:
            pickle.dump(self.pipe, f)




    def predict_model(self):


        """

        Function Responsible for loading the trainned model and predicting
        the state of the incoming live request.

        Args:None

        return (list): A list containing the predicted output.


        """

        warnings.filterwarnings("ignore",category=UserWarning)

        # Load the model from server
        try:
                  #cdwith open(self.MODEL_PATH,"rb") as f:

                  self.model=joblib.load(self.MODEL_PATH)
        except Exception as E:
            print(E)

        self.live_df = pd.DataFrame(self.live_data,columns=['path','body','path_len','special_char','whitespaces'])
        return self.model.predict(self.live_df)


