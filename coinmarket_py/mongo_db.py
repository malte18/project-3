import pymongo
import time, requests, json
import schedule
import functools

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

cryptodb = myclient["btc"]

mycol = cryptodb["price"]

# list of db names
print(myclient.list_database_names())


# dblist = myclient.list_database_names()
# if "btc" in dblist:
#   print("The database exists.")
# else:
#     print("error")


COINMARKETCAP_PRO_API_KEY = "9a9aa344-688d-4917-982d-61963234e18b"


print(time.tzname)
print(time.time())


# TODO: section: insert json from API call into MongoDB
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD'
url_2 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
 'Accept': 'application/json',
 'Accept-Encoding': 'deflate, gzip',
 'X-CMC_PRO_API_KEY': COINMARKETCAP_PRO_API_KEY,
}

r = requests.get(url, headers=headers)


# This decorator can be applied to
def with_logging(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('LOG: Running job "%s"' % func.__name__)
        result = func(*args, **kwargs)
        print('LOG: Job "%s" completed' % func.__name__)
        return result
    return wrapper

@with_logging
def test_call():
    if r.status_code == 200:
        response = json.loads(r.text)

        mycol.insert_one(response)
        print("successfully inserted %s" % response)

        # lastUpdated = response['data']['BTC']['quote']['USD']['last_updated']

        # timestamp = dt.datetime.strptime(lastUpdated, '%Y-%m-%dT%H:%M:%S.000Z')

        # print(timestamp)

    else:
        print(" %s is not a valid url " %url_2)



@with_logging
def print_time():
    print(time.time())


schedule.every(1).minutes.do(print_time)


# TODO: section: execute API call every "minutes"
schedule.every(10).minutes.do(test_call)

while 1:
    schedule.run_pending()
    time.sleep(1)



# collection names
# print(cryptodb.list_collection_names())

