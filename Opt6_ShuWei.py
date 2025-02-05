from prettytable import PrettyTable
import requests

def get_conversion_rate(target_currency):
    """
    Retrieve the USD to target_currency conversion rate from exchangerate-api.com.
    """
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        data = response.json()
        rate = data["rates"].get(target_currency)
        return rate
    except Exception as e:
        print("Error retrieving conversion rate from exchangerate-api:", e)

def opt6():
    # Map menu options to currency codes.
    currency_options = {
        0: 'SGD',  # Singapore Dollar
        1: 'MYR',  # Malaysian Ringgit
        2: 'INR',  # Indian Rupee
        3: 'CNY',  # Chinese Yuan
        4: 'JPY',  # Japanese Yen
        5: 'GBP',  # British Pound Sterling
        6: 'AUD',  # Australian Dollar
        7: 'CHF'   # Swiss Franc
    }
    
    # Display the available currencies.
    print("No  -  Currency")
    print("-" * 20)
    for key in currency_options:
        print(str(key) + "  -  " + currency_options[key])
    
    # Ask the user to choose a currency.
    try:
        choice = int(input("Enter the number corresponding to the currency you want to convert to: "))
        if choice not in currency_options:
            print("Invalid choice!")
            return
        target_currency = currency_options[choice]
    except ValueError:
        print("Please enter a valid number!")
        return

    # Get the conversion rate using exchangerate-api.
    conversion_rate = get_conversion_rate(target_currency)
    if conversion_rate == 0:
        print("Failed to retrieve conversion rate. Exiting.")
        return

    # Read the CSV file.
   
    file = open("cryptoProfile AMENDED.csv", "r")
    data = []
    for line in file:
        if line.strip() != "":
            data.append(line.strip().split(","))
    file.close()
    
    if len(data) == 0:
        print("The file is empty!")
        return
        
    # The first row is the header.
    header = data[0]

    # Convert each price from USD to the target currency.
    for row in data[1:]:
        for idx in row[3:]:
            usd_value = float(row[idx])
            converted_value = conversion_rate * usd_value
            row[idx] = round(converted_value, 2)

    # Prepare and display the table with a numbering column.
    header_with_no = ["No"] + header
    table = PrettyTable()
    table.field_names = header_with_no

    row_number = 1
    for row in data[1:]:
        table.add_row([row_number] + row)
        row_number = row_number + 1
    
    print("\nConverted Prices Table:")
    print(table)

# Call the function.
opt6()