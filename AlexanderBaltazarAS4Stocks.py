def name_stock(stock_name):
    return stock_name

def calculate_change(open_price,close_price):
    result = close_price - open_price
    return result

def calculate_percent_change(open_price,close_price):
    change = close_price - open_price
    return (change / open_price) * 100

def market_status(change):
    if change > 0:
        status = "GAIN"
    elif change < 0:
        status = "LOSS"
    else:
        status = "NO CHANGE"
    return status

def display_summary(stock_name, open_price, close_price, change, percent_change, status):
    print()
    print("DAILY STOCK SUMMARY")
    print("Stock:", stock_name)
    print("Change:", change)
    print("Percent Change", percent_change)
    print("Status:", status)

stock_name = input("Enter Stock Name: ")
open_price = float(input("Enter Opening Price: "))
close_price = float(input("Enter Closing Price: "))

change = calculate_change(open_price,close_price)
percent_change = calculate_percent_change(open_price,close_price)
status = market_status(change)

display_summary(stock_name, open_price, close_price, change, percent_change, status)














    