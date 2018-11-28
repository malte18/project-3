import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
import schedule
import time
import functools

db = client.btc


collection = db.price


# x = collection.find_one()
query_1 = {"data": {"BTC": {"id": 1}}}

# basic queries, doc_4 is most relevant
doc = collection.find({}, {"data": {"BTC": {"id": 1}}})
doc_2 = collection.find({}, {"data.BTC.quote.USD.price": 1})
doc_3 = collection.find({}, {"data.BTC.quote.USD.percent_change_24h": 1})
doc_4 = collection.distinct("data.BTC.quote.USD.price")  # {"$gt": 3699}
# doc_4 = collection.distinct({"data.BTC.quote.USD.price": {$gt: 3697}}, {"data.BTC.quote.USD.price": 1})


# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed' % func.__name__)
        return result
    return wrapper


def return_list():
    for x in doc_2:

        list = []

        list.append(x["data"])

        print(list)
        # myValues[i] = x["data"]

        # print(x)

@with_logging
def return_json_1():
    print(doc_4)

# Here we do some basic shit, playing around with numbers and returning messages
@with_logging
def return_json_2():
    current_price = doc_4[-1] # TODO: the list item picked once must not move when array gets bigger OR think about algorithm
    price_before = doc_4[-2]
    spread = current_price - price_before
    # current_spread = spread/80
    spread_needed = 80 - spread
    price_goal = doc_4[-1] + spread_needed
    price_increase_needed = current_price/price_goal

    if spread > 80:
        print("invest")
    else:
        print(" \n We do not advice you to invest right now. \n \n Here are the facts why: \n \n")
        print(" 1.) The current price of BTC is at {} \n ".format(doc_4[-1]))
        print(" 2.) the price needs to increas by {}$ \n".format(spread_needed))
        print(" 3.) dcrypt propses an investment once the price is at {} \n".format(price_goal))
        print(" 4.) This means that the price has to increase by {}% \n".format(price_increase_needed))


# TODO: section: execute API call every "minutes", scheduled see below
schedule.every(10).minutes.do(return_json_1)
schedule.every(10).minutes.do(return_json_2)

while 1:
    schedule.run_pending()
    time.sleep(1)


# return_json_1()
# return_json_2()
# for y in doc_3:
# print(y['price'])

