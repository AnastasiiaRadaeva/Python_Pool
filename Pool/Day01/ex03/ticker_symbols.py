import sys

def find_key(companies, value):
    for k, v in companies.items():
        if v == value:
            return k

def find_info():
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    if len(sys.argv) != 2:
        exit()
    lower_case_stock = {x.lower(): stocks[x] for x in stocks.keys()}
    lower_case_companies = {x: companies[x].lower() for x in companies.keys()}
    if sys.argv[1].lower() in lower_case_stock:
        print(find_key(lower_case_companies, sys.argv[1].lower()), lower_case_stock.get(sys.argv[1].lower()))
    else:
        print("Unknown ticker")

if __name__=='__main__':
    find_info()