import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
import schedule
import time
import functools

db = client.btc
collection = db.price


# basic queries, doc_4 is most relevant
doc = collection.distinct("data.BTC.quote.USD.price")  # {"$gt": 3699}


def return_json_1():
    print(doc)


return_json_1()

# TODO: Formulierung der Query:
# What do I need timestamp for?
# --> let's assume 15 minute cycles
# --> price[0]
# --> different approach: start value, starting at 1 point in time.
# --> new values are taken and compared in 15min cycles


# price[0] - price(new_value(15min. cycles))
# if investment triggered:
# --> take value that triggered invest as new foundation?
# bottlenecks: how agile does the code have to be