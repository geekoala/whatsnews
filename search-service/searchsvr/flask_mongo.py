"""
Author: Wenhua Yang
Date: 09/18/2016
"""

from pymongo import MongoClient


class MongoConnection(object):

    def __init__(self):
        self.connection = None
        self.db = None

    def connect_db(self, application):
        if self.connection is None:
            hosts = application.config['MONGODB_HOSTS']
            self.connection = MongoClient(host=hosts)
            db_name = application.config['MONGODB_DBNAME']
            self.db = self.connection[db_name]
        return self.db

    def close(self):
        if self.connection:
            self.connection.close()
