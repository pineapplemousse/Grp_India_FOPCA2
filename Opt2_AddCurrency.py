print("-----------------------------------------------")
opt=int(input("Select an option: "))
crypto=str(input("Enter Cryptocurrency Name : "))
while True:
 Marketcap=str(input("Enter Market Cap of Crypto: High, Mid, Low: "))
 if Marketcap == "High" or Marketcap == "Mid" or Marketcap == "Low" :
   int(input("Enter Quantity of Crypto Bought = "))
   break
 else:
  print("Invalid input. Please type 'High', 'Med', or 'Low'.")
buy_in_price=float(input("Enter Buy In Price of Crypto = "))
market_price=float(input("Enter market Price of Crypto = "))
print("-----------------------------------------------")
