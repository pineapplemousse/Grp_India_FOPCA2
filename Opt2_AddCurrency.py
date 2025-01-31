import csv
import os
from prettytable import PrettyTable

FILE_PATH = "cryptoProfile AMENDED.csv"  # Ensure this file exists in your directory

def opt2():
    # Ensure the file exists before writing
    if not os.path.exists(FILE_PATH):
        print(f"Error: The file '{FILE_PATH}' does not exist. Please check the file path.")
        return
    
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
    try:
        # Ensure last line has a newline before appending
        with open(FILE_PATH, "r+", newline='') as file:
            file.seek(0, os.SEEK_END)  # Move to the end of the file
            if file.tell() > 0:  # Check if the file is not empty
                file.seek(file.tell() - 1, os.SEEK_SET)  # Move to the last character
                if file.read(1) != "\n":  # If last character isn't newline, add one
                    file.write("\n")

        # Append new entry without adding an extra blank line
        with open(FILE_PATH, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([crypto_name, Marketcap, quantity, buy_in_price, market_price])
    except Exception as e:
        print(f"Error writing to file: {e}")
        return
    
    # Display the updated CSV as a table
    display_csv_as_table(FILE_PATH)

def display_csv_as_table(file_path):
    """Reads a CSV file and prints it as a formatted table."""
    if not os.path.exists(file_path):
        print("Error: CSV file not found.")
        return

    table = PrettyTable()

    try:
        with open(file_path, "r", newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Read first row as headers
            table.field_names = headers  # Set table headers
            
            for row in reader:
                # Convert numeric values to whole numbers if applicable
                row[3] = int(float(row[3])) if row[3].replace('.', '', 1).isdigit() and float(row[3]).is_integer() else row[3]
                row[4] = int(float(row[4])) if row[4].replace('.', '', 1).isdigit() and float(row[4]).is_integer() else row[4]
                table.add_row(row)
        
        print(table)

    except Exception as e:
        print(f"Error reading file: {e}")

# Call the function
opt2()