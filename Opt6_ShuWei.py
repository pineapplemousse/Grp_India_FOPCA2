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
    while True:
        
        currency_options = {
            0: 'SGD',  
            1: 'MYR',  
            2: 'INR',  
            3: 'CNY',  
            4: 'JPY',  
            5: 'GBP',  
            6: 'AUD',  
            7: 'CHF'   
        }
        
        
        print("No  -  Currency")
        print("-" * 20)
        for key in currency_options:
            print(str(key) + "  -  " + currency_options[key])
        
    
        choice = input("Enter the number corresponding to the currency you want to convert to, or press 'E' to exit: ")
        if choice.lower() == 'e':
            break
        elif int(choice) not in currency_options:
            print("Invalid choice!")
            continue
        choice = int(choice)
        target_currency = currency_options[choice]


        
        conversion_rate = get_conversion_rate(target_currency)
        if conversion_rate == 0:
            print("Failed to retrieve conversion rate.")
            return

        
        with open('cryptoProfile AMENDED.csv') as file:
            data = [line.strip().split(',') for line in file]
        
        if len(data) == 0:
            print("The file is empty!")
            return
            
        
        data[0] = ["No"] + data[0]

        
        for row in data[1:]:
            for i in range(3, len(row)):
                usd_value = float(row[i])
                converted_value = conversion_rate * usd_value
                row[i] = round(converted_value, 2)

        
        table = PrettyTable()
        table.field_names = data[0]
        
        i = 1
        for row in data[1:]:
           table.add_row([i]+ row)
           i += 1

        row_number = 1
        for row in data[1:]:
            table.add_row([row_number] + row)
            row_number = row_number + 1
        
        print("\nConverted Prices Table:")
        print(table)