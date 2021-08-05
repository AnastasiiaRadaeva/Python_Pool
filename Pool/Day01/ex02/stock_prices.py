import sys

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
    lower_case_dict = {x.lower(): companies[x] for x in companies.keys()}
    if sys.argv[1].lower() in lower_case_dict:
        print(stocks.get(lower_case_dict.get(sys.argv[1].lower())))
    else:
        print("Unknown company")

if __name__=='__main__':
    find_info()