import csv

def opt3():
    file_path = "cryptoProfile AMENDED.csv"  # Ensure the correct path to your CSV

    # Read the CSV file into a header and data rows (2D list)
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        all_rows = list(reader)
        
    if not all_rows:
        print("The CSV file is empty.")
        return

    header = all_rows[0]
    data = all_rows[1:]

    # Get the indexes for each required column for convenience
    
    name_idx = header.index("Name")
    market_cap_idx = header.index("Market Cap")
    quantity_idx = header.index("Quantity")
    buy_in_price_idx = header.index("Buy In Price")
    market_price_idx = header.index("Market Price")
    
    while True:
        print("-----------------------------------------------")
        print("No - CryptoCurrency")
        print("---------------------------")
        # List all cryptocurrencies by their Name field using range() instead of enumerate
        for i in range(len(data)):
            print(f"{i} - {data[i][name_idx]}")
        print("---------------------------")
        
        selection = input(f"Enter a number (0 to {len(data)-1}) for your selection or E to exit: ")

        if selection.lower() == "e":
            break
        elif selection.isdigit() and 0 <= int(selection) < len(data):
            index = int(selection)
            current_row = data[index]
            print("\n-------------------------------")
            print(f"Index: {index}")
            print(f"1. Name           : {current_row[name_idx]}")
            print(f"2. Market Cap     : {current_row[market_cap_idx]}")
            print(f"3. Quantity       : {current_row[quantity_idx]}")
            print(f"4. Buy In Price   : {current_row[buy_in_price_idx]}")
            print(f"5. Market Price   : {current_row[market_price_idx]}")
            print("E. Edit Completed. Exit")
            print("-------------------------------")
            
            while True:
                field_selection = input("What do you want to edit? (Enter number or E to exit): ")

                if field_selection.lower() == "e":
                    break
                elif field_selection in ["1", "2", "3", "4", "5"]:
                    # Map the selection to the corresponding header field.
                    field_map = {
                        "1": "Name",
                        "2": "Market Cap",
                        "3": "Quantity",
                        "4": "Buy In Price",
                        "5": "Market Price"
                    }
                    field_name = field_map[field_selection]

                    # Determine the column index for the field.
                    col_idx = header.index(field_name)

                    new_value = input(f"Enter new {field_name}: ")

                    # Validate numeric input for specific fields.
                    if field_name in ["Quantity", "Buy In Price", "Market Price"]:
                        if not new_value.isdigit():
                            print("Invalid input. Please enter a numeric value.")
                            continue
                        # Convert to integer and back to string if desired.
                        new_value = str(int(new_value))

                    # Update the value in our 2D list.
                    data[index][col_idx] = new_value
                    print(f"Updated {field_name} to {new_value}\n")
                else:
                    print("Invalid Option, please try again.")
        else:
            print("Invalid input. Please enter a valid selection.")

    # Write the updated header and data rows back to the CSV file.
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

    print("Changes saved successfully!")

# Call the function
opt3()