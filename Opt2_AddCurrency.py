print("-----------------------------------------------")
int(input("Select an option: "))
str(input("Enter Cryptocurrency Name : "))
while True:
 Marketcap=str(input("Enter Market Cap of Crypto: High, Mid, Low: "))
 if Marketcap == "High" or Marketcap == "Mid" or Marketcap == "Low" :
   int(input("Enter Quantity of Crypto Bought = "))
   break
 else:
  print("Invalid input. Please type 'high', 'medium', or 'low'.")
float(input("Enter Buy In Price of Crypto = "))
float(input("Enter market Price of Crypto = "))
print("-----------------------------------------------")