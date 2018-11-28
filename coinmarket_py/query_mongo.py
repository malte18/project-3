import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")


db = client.btc


collection = db.price


# x = collection.find_one()
query_1 = {"data": {"BTC": {"id": 1}}}

doc = collection.find({}, {"data": {"BTC": {"id": 1}}})
doc_2 = collection.find({}, {"data.BTC.quote.USD.price": 1})
doc_3 = collection.find({}, {"data.BTC.quote.USD.percent_change_24h": 1})
doc_4 = collection.find({"data.BTC.quote.USD.price": {"$gt": 3699}})
# doc_4 = collection.distinct({"data.BTC.quote.USD.price": {$gt: 3697}}, {"data.BTC.quote.USD.price": 1})

def return_list():
    for x in doc_2:

        list = []

        list.append(x["data"])

        print(list)
        # myValues[i] = x["data"]

        # print(x)


def return_json():
    for y in doc_4:
        list = []

        print(y["data"]["BTC"]["quote"]["USD"]["price"])

        # print(list)


return_json()
# for y in doc_3:
#     print(y['price'])