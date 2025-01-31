def opt2():
  while True:
   print("-----------------------------------------------")
   int(input("Select an option: "))
   crypto_name=str(input("Enter Cryptocurrency Name : "))
   Marketcap=str(input("Enter Market Cap of Crypto: High, Mid, Low: "))
   if Marketcap == "High" or Marketcap == "Mid" or Marketcap == "Low" :
     quantity=input("Enter Quantity of Crypto Bought = ")
     break
   else:
     print("Invalid input. Please type 'High', 'Mid', or 'Low'.")
   buy_in_price=float(input("Enter Buy In Price of Crypto = "))
   market_price=float(input("Enter market Price of Crypto = "))
   print("-----------------------------------------------")
   file_path = "C:\Users\Lenovo\Doceuments\GitHub\Grp_India_FOPCA2\cryptoProfile AMENDED.csv"
   with open(file_path, "a") as file:
     file.write(crypto_name + Marketcap + quantity + buy_in_price + market_price +"\n")  # Adds user input with a newline
   with open(file_path, "r") as file:
     print(file.read()) # Read and print file content

# Call the function
opt2()