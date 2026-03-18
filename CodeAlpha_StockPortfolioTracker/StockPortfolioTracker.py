# Hardcoded dictionary for stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "AMZN": 3300,
    "MSFT": 300,
    "NFLX": 400,
    "META": 350,
}

portfolio = {}
total_investment = 0

print("Stock Portfolio Tracker")

# Show available stocks with prices
print("\nAvailable Stocks:")
for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")

# Take user input
while True:
    stock_name = input("\nEnter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))
        portfolio[stock_name] = quantity
    else:
        print("❌ Stock not available in price list.")

# Display portfolio
print("\nYour Portfolio:")

for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment

    print(f"{stock} : {quantity} shares × ₹{price} = ₹{investment}")

# Show total
print("\nTotal Investment Value: ₹", total_investment)

# Save result to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n\n")

    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        investment = price * quantity
        file.write(f"{stock} : {quantity} shares x {price} = {investment}\n")

    file.write(f"\nTotal Investment Value: {total_investment}")

print("\n✅ Portfolio saved to portfolio.txt")
