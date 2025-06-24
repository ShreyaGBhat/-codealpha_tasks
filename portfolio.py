stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 310,
    "AMZN": 130
}

portfolio = {}
num_stocks = int(input("How many different stocks do you want to enter? "))

for i in range(num_stocks):
    stock_name = input(f"Enter stock symbol #{i+1} (e.g., AAPL): ").upper()
    if stock_name in stock_prices:
        quantity = int(input(f"How many shares of {stock_name}? "))
        portfolio[stock_name] = quantity
    else:
        print(f"Sorry, {stock_name} is not in our stock list.")

total_value = 0
output_lines = []

print("\n📊 Your Stock Portfolio:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_value += value
    line = f"{stock}: {qty} shares × ${price} = ${value}"
    print(line)
    output_lines.append(line)

print(f"\n💰 Total Investment Value: ${total_value}")

save = input("Do you want to save this result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Your Stock Portfolio:\n")
        for line in output_lines:
            file.write(line + "\n")
        file.write(f"\nTotal Investment Value: ${total_value}\n")
    print("✅ Results saved to 'portfolio_summary.txt'")
