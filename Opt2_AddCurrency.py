import csv
import os
from prettytable import PrettyTable

FILE_PATH = "cryptoProfile AMENDED.csv"  # Ensure this file exists in your directory

def opt2():
    # Ensure the file exists before writing
    
    while True:
        print("-----------------------------------------------")        
        crypto_name = input("Enter Cryptocurrency Name: ")
        Marketcap = input("Enter Market Cap of Crypto (High, Mid, Low): ")
        
        if Marketcap in ["High", "Mid", "Low"]:
            quantity = input("Enter Quantity of Crypto Bought = ")
            try:
                buy_in_price = float(input("Enter Buy In Price of Crypto = "))
                market_price = float(input("Enter Market Price of Crypto = "))

                # Convert to whole number if it has no decimal part
                buy_in_price = int(buy_in_price) if buy_in_price.is_integer() else buy_in_price
                market_price = int(market_price) if market_price.is_integer() else market_price
                
                break  # Exit loop after valid input
            except ValueError:
                print("Invalid price input. Please enter a valid number.")
        else:
            print("Invalid input. Please type 'High', 'Mid', or 'Low'.")
    
    print("-----------------------------------------------")

    # **Fix for last-line overwrite & extra blank lines**
        # Append new entry without adding an extra blank line
    with open(FILE_PATH, "a+") as file:                    #append and read
        file.seek(os.SEEK_END)  # Move to the end of the file.
        if file.tell() > 0:        # Check if the file is not empty.
            file.seek(file.tell() - 1)
            if file.read(1) != "\n":
                file.write("\n")  # Only add a newline if needed.
        writer = csv.writer(file)
        writer.writerow([crypto_name, Marketcap, quantity, buy_in_price, market_price])

    
    # Display the updated CSV as a table
    display_csv_as_table(FILE_PATH)

def display_csv_as_table(file_path):
    """Reads a CSV file and prints it as a formatted table."""

    table = PrettyTable()

    with open(file_path, "r", newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)  # Read first row as headers
        table.field_names = headers  # Set table headers
        
        for row in reader:

            table.add_row(row)
    
    print(table)

# Call the function
opt2()