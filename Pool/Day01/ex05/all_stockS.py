import sys

def find_key(companies, value):
    for k, v in companies.items():
        if v == value:
            return k
    return None

def print_name(companies, upper_comp, name):
    k = find_key(companies, name)
    if k != None:
        print(upper_comp.get(k), "is a ticker symbol for", k)
        return 1
    return 0

def print_price(companies, stocks, old_comp, name):
    if name in companies:
        name_of_comp = find_key(old_comp, companies.get(name))
        print(name_of_comp, "stock price is", stocks.get(companies.get(name)))
        return 1
    return 0

def print_info(companies, stocks, name):
    lower_case_companies_ticker = {x: companies[x].lower() for x in companies.keys()}
    lower_case_companies = {x.lower(): companies[x] for x in companies.keys()}
    if print_name(lower_case_companies_ticker, companies, name.lower()) == 0 and print_price(lower_case_companies, stocks,
                                                                               companies, name.lower()) == 0:
        print(name, "is an unknown company or an unknown ticker symbol")

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
    tmp_str = sys.argv[1].replace(" ", "")
    input_list = tmp_str.split(",")
    # if len(input_list) == 3: ?????
    if "" in input_list:
        print("")
    else:
        for i in input_list:
            print_info(companies, stocks, i)

if __name__=='__main__':
    find_info()