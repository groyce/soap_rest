import requests

def current_stock_price(symbol):
    symbol_f = str(symbol)
    main_api = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='
    api_key = '&interval=1min&apikey=YOUR_KEY_HERE'
    url = main_api + symbol_f + api_key
    json_data = requests.get(url).json()
    mkt_dt = (json_data["Meta Data"]["3. Last Refreshed"])
    open_price = float(json_data["Time Series (1min)"][mkt_dt]["1. open"])
    share_value = open_price
    return share_value

def main():
    print("Stock Price Program")
    print()

    symbol = str(input("Enter Stock Symbol:\t\t"))
    share_value = float(current_stock_price(symbol))
    print (str(share_value))

if __name__ == "__main__":
    main()




