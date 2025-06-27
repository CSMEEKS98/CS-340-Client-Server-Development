# Author: Makayla L Meeks
# Date: June 18, 2025
# Course: CS 340 Client/Server Development
# Assignment: CRUD


from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password, host, port, db, collection):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = 'aacuser'
        PASS = 'Meeks2417'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 31259
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient(f'mongodb://aacuser:Meeks2417@nv-desktop-services.apporto.com:31259')
        self.database = self.client['AAC']
        self.collection = self.database['animals']

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None: 
            insertSuccess = self.database.animals.insert_one(data)  # data should be dictionary    
            # Check insertSuccess for operation
            if insertSuccess != 0:
                return False
            # default return
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD.
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            data = self.database.animals.find( {}, {"_id": False})
    # Return the dataset else let the error flow up
        return data
        
# Create method to implement the U in CRUD
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData})
        else:
            return "{}"
        # Return the dataset else let the error flow up
            return result.raw_result

#Create method to implement the D in CRUD
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # Return the dataset else let the error flow up
            return result.raw_result
