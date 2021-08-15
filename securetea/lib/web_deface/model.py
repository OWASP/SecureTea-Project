# -*- coding: utf-8 -*-
u"""Machine Learning module for SecureTea Web Deface Detection.

Project:
    ╔═╗┌─┐┌─┐┬ ┬┬─┐┌─┐╔╦╗┌─┐┌─┐
    ╚═╗├┤ │  │ │├┬┘├┤  ║ ├┤ ├─┤
    ╚═╝└─┘└─┘└─┘┴└─└─┘ ╩ └─┘┴ ┴
    Author: Aman Singh <dun930n.m45732@gmail.com> , Aug 1 2021
    Version: 1.4
    Module: SecureTea

"""
from securetea.lib.web_deface.deface_logger import DefaceLogger
import pandas as pd
from pathlib import Path
import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import accuracy_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from nltk.stem.snowball import SnowballStemmer
from string import punctuation
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
import pickle

class MLModel(object):
    """
    ML Model class to train and test for RandomForest Classifier for
    Defacement prediction 
    """
    def __init__(self, debug=False):
        """
        Dataset file have texts from defaced webpages and Text from Normal webpages
        """

        self.logger = DefaceLogger(
                __name__,
                debug=debug
        )
        #initialize path of datasets
        self.NORMAL_DATA_PATH = str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/data1.csv"
        self.DEFACED_DATA_PATH = str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/data.csv"

        self.prediction()

    def prepare_dataset(self):
        """
        Preparing Dataset

        We are going to work just on two categories, positives and negatives. 
        Therefore, we select 5,000 rows for each category and copy them into the Pandas Dataframe 
        """

        fields = ['status', 'content']

        #Defacement Text Vectorization
        df = pd.read_csv(
            self.DEFACED_DATA_PATH,
            usecols= fields, nrows=5000)
        stemmer = SnowballStemmer('english')
        df['content'] = df['content'].apply(
            lambda x: ' '.join(stemmer.stem(y) for y in x.split())
        )
        df['content'] = df['content'].apply(
            lambda x: ' '.join(word for word in x.split() if word not in (stopwords.words()))
        )
        df_Positive = df['content'].copy()
        df_Positive = df_Positive.str.replace('\d+', '', regex=True)

        #Normal Text vectorization

        df = pd.read_csv(
            self.NORMAL_DATA_PATH,
            usecols= fields, nrows=5000)
        stemmer = SnowballStemmer('english')
        df['content'] = df['content'].apply(
            lambda x: ' '.join(stemmer.stem(y) for y in x.split())
        )

        df['content'] = df['content'].apply(
            lambda x: ' '.join(word for word in x.split() if word not in (stopwords.words()))
        )

        df_Negative = df['content'].copy()
        df_Negative = df_Negative.str.replace('\d+', '', regex=True)


        self.NEG_DF = df_Negative
        self.POS_DF = df_Positive

    def Vectorization(self):
        """
        Transforms text to feature vectors

        Using TF-IDF, word scores are used instead of word count, therefore we can say TF-IDF measures relevance, not frequency.
        we have used Scikit-Learn TfidfVectorizer for each column and building an N-gram model for vectorization that can be used as input to the estimator.
        """
        df_Positive = self.POS_DF
        df_Negative = self.NEG_DF

        tfidf = TfidfVectorizer(min_df=2,max_df=0.5, ngram_range=(1,3))
        features = tfidf.fit_transform(df_Positive)
        df_Positive = pd.DataFrame(
            features.todense(),
            columns=tfidf.get_feature_names()
        )
        df_Positive['Target'] = '1'

        tfidf = TfidfVectorizer(min_df=2,max_df=0.5, ngram_range=(1,3))
        features = tfidf.fit_transform(df_Negative)
        df_Negative = pd.DataFrame(
            features.todense(),
            columns=tfidf.get_feature_names()
        )
        df_Negative['Target'] = '0'

        df = df_Positive.append(df_Negative)
        df = df.fillna(0)

        self.DATA_FRAME = df

    def get_correlation(self, data, threshold):
        corr_col = set()
        cormat = data.corr()
        for i in range(len(cormat.columns)):
            for j in range(i):
                if abs(cormat.iloc[i,j]) > threshold:
                    colname = cormat.columns[i]
                    corr_col.add(colname)
        return corr_col
    
    def train_test_model(self):
        df = self.DATA_FRAME

        df.to_csv(str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/df.csv")
        x = df.drop('Target',axis=1)
        y = df['Target']
        
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size = 0.4, random_state = 0, stratify = y)

        constant_filter = VarianceThreshold(threshold = 0.0002)
        constant_filter.fit(x_train)

        # Export the features
        feature_list = x_train[x_train.columns[
            constant_filter.get_support(indices=True)]]
        

        x_train_filter = constant_filter.transform(x_train)
        x_test_filter = constant_filter.transform(x_test)

        x_train_filter = pd.DataFrame(x_train_filter)
        x_test_filter = pd.DataFrame(x_test_filter)

        corr_features = self.get_correlation(x_train_filter, 0.70)

        x_train_uncorr = x_train_filter.drop(labels= corr_features, axis = 1)
        x_test_uncorr = x_test_filter.drop(labels= corr_features, axis = 1)
        x_train_uncorr = pd.DataFrame(x_train_uncorr)
        x_test_uncorr = pd.DataFrame(x_test_uncorr)
        lda = LDA(n_components=1)
        x_train_lda = lda.fit_transform(x_train_uncorr, y_train)
        x_test_lda = lda.fit_transform(x_test_uncorr, y_test)
        self.runRandomForest(x_train, x_test, y_train, y_test)

    def runRandomForest(self,x_train, x_test, y_train, y_test):
        model = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
        model.fit(x_train, y_train)
        self.model = model
        y_pred = model.predict(x_test)
        '''
        msg = 'Model accuracy is: ' + str(accuracy_score(y_test, y_pred))
        self.logger.log(
                        msg,
                        logtype="info"
                    )
        '''
        
    def prediction(self):
        self.prepare_dataset()
        self.Vectorization()
        self.train_test_model()
        filename = str(Path(os.path.dirname(__file__)).parent) + "/web_deface/config/finalized_model.sav"
        pickle.dump(self.model, open(filename, 'wb'))
        return
