# -*- coding: utf-8 -*-
u"""ML Based Defacement detection module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , July 25 2021
    Version: 1.4
    Module: SecureTea

"""
import os
from securetea.lib.web_deface.deface_logger import DefaceLogger
from securetea.lib.web_deface.utils import *
from securetea.lib.web_deface.file_handler import *
from pathlib import Path
import os
import pandas as pd
import pickle
import html2text
import csv

from sklearn.model_selection import train_test_split 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_selection import VarianceThreshold
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

class DefaceDetect(object):
    """ML based defacement Detector"""
    def __init__(self, debug=False, path=None):
        """
        Initialize DefaceDetect
        debug (bool): Log on terminal or not
        path (str): Path of the directory to scan file for

        Raises:
            None
        Returns:
            None
        """

        #intialize logger
        self.logger = DefaceLogger(
            __name__,
            debug=debug
        )

        # Initialize path of directory to look for
        self._PATH = path
        self._DATASET = str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/dataset.csv"

    def ml_based_scan(self, files_list):
        """
        Scan the files in the directory to detect any traces of Defacement attempts

        Args:
            file_list (dict): list of files in the directory to scan
        """
        filename = str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/finalized_model.sav"
        with open(filename, "rb") as f:
            loaded_model = pickle.load(f)

        #Preparing User Webpage Dataset for Prediction 
        h = html2text.HTML2Text()
        h.ignore_links = True
        fields = ["status", "content"]
        with open(self._DATASET, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(fields)
            for file in files_list:
                code = open(file, 'r').read()
                code = h.handle(code)
                ' '.join(code.split('\n'))
                row = ['true', code]
                csvwriter.writerow(row)
                
        df = pd.read_csv(
            self._DATASET,
            usecols = fields, nrows=5000
        )
        stemmer = SnowballStemmer('english')

        df['content'] = df['content'].apply(
            lambda x: ' '.join(stemmer.stem(y) for y in x.split())
        )

        df['content'] = df['content'].apply(
            lambda x: ' '.join(word for word in x.split() if word not in (stopwords.words()))
        )
        df = df['content'].copy()
        df = df.str.replace('\d+', '')

        tfidf = TfidfVectorizer(min_df=2,max_df=0.5, ngram_range=(1,3))
        features = tfidf.fit_transform(df)
        df = pd.DataFrame(
            features.todense(),
            columns=tfidf.get_feature_names()
        )
        df_model = pd.read_csv(str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/df.csv", index_col=0)
        df = df.reindex(labels=df_model.columns,axis=1)
        df['Target'] = '1'
        df = df.fillna(0)
        x = df.drop('Target',axis=1)
        pred = loaded_model.predict(x)

        return { files_list[i] : pred[i]=='1' for i in range(len(pred))}