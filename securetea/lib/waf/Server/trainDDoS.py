import tensorflow as tf # add dependecies in requirements
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

class TrainDDoS:
    
    """
    Class responsible for training a ML model that uses Bidirections LSTM classifier and also predict
    the class of live features from the incoming request

    """
    
    def __int__(self):
        
        """

        A constructor that initialise the required variables

        """
        
        self.data_normal.columns = [ 'frame.len', 'frame.protocols', 'ip.hdr_len',
                                    'ip.len', 'ip.flags.rb', 'ip.flags.df', 'p.flags.mf', 'ip.frag_offset',
                                    'ip.ttl', 'ip.proto', 'ip.src', 'ip.dst', 'tcp.srcport', 'tcp.dstport',
                                    'tcp.len', 'tcp.ack', 'tcp.flags.res', 'tcp.flags.ns', 'tcp.flags.cwr',
                                    'tcp.flags.ecn', 'tcp.flags.urg', 'tcp.flags.ack', 'tcp.flags.push',
                                    'tcp.flags.reset', 'tcp.flags.syn', 'tcp.flags.fin', 'tcp.window_size',
                                    'tcp.time_delta','class']
        
        self.data_attack.columns = [ 'frame.len', 'frame.protocols', 'ip.hdr_len',
                                    'ip.len', 'ip.flags.rb', 'ip.flags.df', 'p.flags.mf', 'ip.frag_offset',
                                    'ip.ttl', 'ip.proto', 'ip.src', 'ip.dst', 'tcp.srcport', 'tcp.dstport',
                                    'tcp.len', 'tcp.ack', 'tcp.flags.res', 'tcp.flags.ns', 'tcp.flags.cwr',
                                    'tcp.flags.ecn', 'tcp.flags.urg', 'tcp.flags.ack', 'tcp.flags.push',
                                    'tcp.flags.reset', 'tcp.flags.syn', 'tcp.flags.fin', 'tcp.window_size',
                                    'tcp.time_delta','class']
        
        self.data_normal = self.data_normal.drop(['ip.src', 'ip.dst','frame.protocols'],axis=1)
        self.data_attack = self.data_attack.drop(['ip.src', 'ip.dst','frame.protocols'],axis=1)
        
        self.features = [ 'frame.len', 'ip.hdr_len',
                            'ip.len', 'ip.flags.rb', 'ip.flags.df', 'p.flags.mf', 'ip.frag_offset',
                            'ip.ttl', 'ip.proto', 'tcp.srcport', 'tcp.dstport',
                            'tcp.len', 'tcp.ack', 'tcp.flags.res', 'tcp.flags.ns', 'tcp.flags.cwr',
                            'tcp.flags.ecn', 'tcp.flags.urg', 'tcp.flags.ack', 'tcp.flags.push',
                            'tcp.flags.reset', 'tcp.flags.syn', 'tcp.flags.fin', 'tcp.window_size',
                            'tcp.time_delta']
        
        self.X_train = None 
        self.X_test = None
        self.Y_train = None 
        self.Y_test = None
        
        
    def normalize(self):
        
        """
        A method that is responsible for normalizing and splitting the data of the dataset .

        Args: None
        Returns: None


        """
        
        self.X_normal= self.data_normal[self.features].values
        self.X_attack= self.data_attack[self.features].values
        self.Y_normal= self.data_normal['class']
        self.Y_attack= self.data_attack['class']
        self.X=np.concatenate((self.X_normal, self.X_attack))
        self.Y=np.concatenate((self.Y_normal, self.Y_attack))
        
        self.scalar = StandardScaler(copy=True, with_mean=True, with_std=True)
        self.scalar.fit(self.X)
        self.X = self.scalar.transform(self.X)
        
        for i in range(0,len(self.Y)):
            if self.Y[i] =="attack":
              self.Y[i]=0
            else:
              self.Y[i]=1
              
        self.I = np.asarray(self.I).astype('float32')
        self.Y = np.asarray(self.Y).astype('int32')
        
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.I, self.Y[25:100000], test_size = 0.2)
        
    
    def Pipeline(self):
        
        """
        A method that is responsible for creating the input pipeline of the model .

        Args: None
        Returns: model (tf.keras.Sequential)


        """
        
        self.model = tf.keras.Sequential()

        self.model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(64, activation='tanh', kernel_regularizer='l2')))
        self.model.add(tf.keras.layers.Dense(128, activation = 'relu', kernel_regularizer='l2'))
        self.model.add(tf.keras.layers.Dense(1, activation = 'sigmoid', kernel_regularizer='l2'))

        self.model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])

        return self.model
    
    def train(self):
        
        """
        A method that is responsible for training a model from the given dataset and dumping the object file .

        Args: None
        Returns: None


        """
        
        self.normalize()
        self.model = self.Pipeline()
        
        self.history = self.model.fit(self.X_train, self.Y_train, epochs = 30,validation_split=0.2, verbose = 0)
        
        self.model.save('../data/bidirection_lstm.h5')