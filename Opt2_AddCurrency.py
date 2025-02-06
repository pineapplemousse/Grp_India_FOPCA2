import csv
import os
from prettytable import PrettyTable

FILE_PATH = "cryptoProfile AMENDED.csv"  

def opt2():
    
    while True:
        print("-----------------------------------------------")        
        crypto_name = input("Enter Cryptocurrency Name: ")
        Marketcap = input("Enter Market Cap of Crypto (High, Mid, Low): ")
        
        if Marketcap in ["High", "Mid", "Low"]:
            quantity = input("Enter Quantity of Crypto Bought = ")
            try:
                buy_in_price = float(input("Enter Buy In Price of Crypto = "))
                market_price = float(input("Enter Market Price of Crypto = "))

                
                buy_in_price = int(buy_in_price) if buy_in_price.is_integer() else buy_in_price
                market_price = int(market_price) if market_price.is_integer() else market_price
                
                break  
            except ValueError:
                print("Invalid price input. Please enter a valid number.")
        else:
            print("Invalid input. Please type 'High', 'Mid', or 'Low'.")
    
    print("-----------------------------------------------")

    
    
    with open(FILE_PATH, "a+", newline='') as file:
        file.seek(0, os.SEEK_END)  
        if file.tell() > 0:  
            file.seek(file.tell() - 1)
            last_char = file.read(1)
            if last_char != "\n":
                file.write("\n")  
        writer = csv.writer(file)
        writer.writerow([crypto_name, Marketcap, quantity, buy_in_price, market_price])