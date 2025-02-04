from prettytable import PrettyTable
from forex_python.converter import CurrencyRates
import requests

def get_fallback_rate_exchangerateapi(target_currency):
    """
    Retrieve the USD to target_currency conversion rate from exchangerate-api.com.
    """
    try:
        url = "https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"HTTP error: {response.status_code}")
        data = response.json()
        if "rates" not in data:
            raise Exception(f"Unexpected response structure from exchangerate-api.com: {data}")
        rate = data["rates"].get(target_currency)
        if rate is None:
            raise Exception(f"Target currency '{target_currency}' not found in response: {data}")
        return rate
    except Exception as e:
        print("Fallback rate retrieval (exchangerate-api) error:", e)
        return None

def opt6():
    # Create a CurrencyRates instance from forex-python.
    c = CurrencyRates()
    
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
    print('No  -  Currency')
    print('-' * 20)
    for key, value in currency_options.items():
        print(f"{key}  -  {value}")
    
    # Ask the user to choose a currency.
    try:
        choice = int(input('Enter the number corresponding to the currency you want to convert to: '))
        if choice not in currency_options:
            print("Invalid choice!")
            return
        target_currency = currency_options[choice]
    except ValueError:
        print("Please enter a valid number!")
        return

    # First try using forex-python.
    try:
        conversion_rate = c.get_rate('USD', target_currency)
        print(f"Conversion rate from USD to {target_currency} (forex-python): {conversion_rate:.4f}\n")
    except Exception as e:
        print(f"Error retrieving conversion rate (forex-python): {e}")
        print("Attempting fallback rate retrieval from exchangerate-api.com...")
        conversion_rate = get_fallback_rate_exchangerateapi(target_currency)
        if conversion_rate is None:
            print("Failed to retrieve conversion rate from both sources. Exiting.")
            return
        else:
            print(f"Conversion rate from USD to {target_currency} (exchangerate-api): {conversion_rate:.4f}\n")
    
    # Read the CSV file.
    try:
        with open('cryptoProfile AMENDED.csv', 'r') as file:
            # Read each nonempty line and split by commas.
            data = [line.strip().split(',') for line in file if line.strip()]
        
        if not data:
            print("The file is empty!")
            return
    except FileNotFoundError:
        print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
        return
    except Exception as e:
        print(f"An error occurred while reading the CSV file: {e}")
        return

    # The first row is the header.
    header = data[0]
    # Identify columns with "price" in their header (case-insensitive).
    price_indices = [i for i, col in enumerate(header) if "price" in col.lower()]
    if not price_indices:
        print("No price column found in the CSV file.")
        return

    # Convert each price from USD to the target currency.
    for row in data[1:]:
        for idx in price_indices:
            try:
                usd_value = float(row[idx])
            except ValueError:
                # Skip cells that cannot be converted to float.
                continue
            try:
                converted_value = conversion_rate * usd_value
                print(f"Converted {usd_value} USD to {target_currency}: {converted_value:.2f}")
                row[idx] = f"{converted_value:.2f}"
            except Exception as e:
                print(f"Error converting value {row[idx]}: {e}")
                continue

    # Prepare and display the table with a numbering column.
    header_with_no = ["No"] + header
    table = PrettyTable()
    table.field_names = header_with_no

    for i, row in enumerate(data[1:], start=1):
        table.add_row([i] + row)
    
    print("\nConverted Prices Table:")
    print(table)

# Call the function.
opt6()
