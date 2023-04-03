import os
import datetime
import json
from sqlalchemy import create_engine, Integer, String, Column, MetaData, select, Table, DateTime

class DatabaseLogs:
    """
       A class that stores the IDS logs in a sqlite3 database.
       function insert_log accepts logs of the user and stores it in database.
       function retrive_log takes the users ID as input and returns the corresponding logs.



    """
    
    def __init__(self, data):
        """
        Initializing the variables
        """
        
        self.data = data
        
        self.user = self.data['user']
        self.msg = self.data['msg']
        self.From = "None"
        if self.data['From']:
            self.From = self.data['From']
        
        
        self.db_path = "../db/logs.sqlite3"
        self.db_name = "logs.sqlite3"
        
        # creates the sqlite3 database if it does not exits
        
        self.db_exits = True
        
        if not os.path.isfile(self.db_path):
            os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
            
            with open(self.db_path, "w") as f:
                self.db_exits = False
            
        self.abs_path = os.path.abspath(self.db_path)
        self.sqlite_abs_path = f"sqlite:///{self.abs_path}"
            
        self.engine = create_engine(self.sqlite_abs_path, echo=True)
        self.metadata = MetaData()
        
        self.users = Table('user_logs', self.metadata,
                        Column('id', Integer, primary_key=True, autoincrement=True),
                        Column('userID', String),
                        Column('From', String),
                        Column('date', DateTime)
                        )
        
        if not self.db_exits:
            self.metadata.create_all(self.engine)
            
    
    # insert the waf logs in database
        
    def insert_log(self):
        
        with self.engine.connect() as conn:
            conn.execute(self.users.insert().values(userID=self.user, From=self.From, From=self.From, date=datetime.datetime.now()))
            
    # retrive the waf logs from the database        
            
    def retrive_log(self):
        
        self.conn = self.engine.connect()
        
        self.query = select(self.users).where(self.users.c.userID == self.user)
        
        self.res = self.conn.execute(self.query).fetchall()
        
        json_data = {'msg': self.res[0][2],
                     'From': self.res[0][3]
                     }
        
        self.jsonDump = json.dumps(json_data)
        
        return self.jsonDump   