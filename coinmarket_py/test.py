
import time, requests, json
import datetime as dt

COINMARKETCAP_PRO_API_KEY = "9a9aa344-688d-4917-982d-61963234e18b"


print(time.tzname)
print(time.time())


# TODO: section: URLS from coinmarketcap
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?symbol=BTC&convert=USD'
url_2 = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
 'Accept': 'application/json',
 'Accept-Encoding': 'deflate, gzip',
 'X-CMC_PRO_API_KEY': COINMARKETCAP_PRO_API_KEY,
}


# TODO: Section: get all data concerning one Coin
r = requests.get(url, headers=headers)

def test_call():
    if r.status_code == 200:
        response = json.loads(r.text)
        print(response)

        # lastUpdated = response['data']['BTC']['quote']['USD']['last_updated']

        # timestamp = dt.datetime.strptime(lastUpdated, '%Y-%m-%dT%H:%M:%S.000Z')

        # print(timestamp)

    else:
        print(" %s is not a valid url " %url_2)



# TODO: Section: cryptocompare API // shit is good here
request = requests.get('https://min-api.cryptocompare.com/data/histoday?fsym=BTC&tsym=USD')

if request.content != '':
   response = request.content
   response = json.loads(response)
   print(response)


# TODO: 1.) write simple script to insert jsonobject into mongodb
# TODO: 2.) read data from database
# TODO: 3.) think about the structure of your *fucking* algorithm
# TODO: 4.) derive simple conclusions


