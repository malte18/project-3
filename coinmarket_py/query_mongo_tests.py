import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
import schedule
import time
import datetime
import functools
import calendar

db = client.btc
collection = db.price


# basic queries, doc_4 is most relevant
doc = collection.distinct("status.timestamp")  # {"$gt": 3699}
doc_2 = collection.find({"status.timestamp": "2018-11-27T10:49:31.008Z"})
doc_3 = collection.distinct("data.BTC.quote.USD.price")


print(datetime.time)

def return_json_1():
    b = time.strptime(doc[0], '%Y-%m-%dT%H:%M:%S.%fZ')
    a = time.strptime(doc[5], '%Y-%m-%dT%H:%M:%S.%fZ')
    # a = time.strptime(doc[3], '%Y-%m-%dT%H:%M:%S.%fZ')

    b = time.mktime(b)
    # a = time.mktime(a)

    print(doc[3])

        # i = time.strptime(doc[i], '%Y-%m-%dT%H:%M:%S.%fZ')
        # i = time.mktime(i)
        #
        # if (i - b)/360 > 24:
        #     print(i)



    # b = calendar.timegm(b)
    # a = calendar.timegm(a)
    # c = (a - b)/60/60


def return_json_2():
    for y in doc_2:
        base_price = y["data"]["BTC"]["quote"]["USD"]["price"]

        print(base_price)

return_json_1()
return_json_2()

# TODO: update base_value every 15 minutes

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