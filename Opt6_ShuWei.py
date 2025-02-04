# Convert crypto prices to other forms of currency
#Copy pasted from chatGPT, needs amendment

from prettytable import PrettyTable
from forex_python.converter import CurrencyRates

# Create a CurrencyRates instance
c = CurrencyRates()

'''
# Get exchange rate from USD to EUR
rate = c.get_rate('USD', 'EUR')
print(f"Exchange rate (USD to EUR): {rate}")

# Convert 100 USD to EUR
amount_in_eur = c.convert('USD', 'EUR', 100)
print(f"100 USD in EUR: {amount_in_eur}")
'''

def opt6():
    print('No  -  Currency')
    print('-'*20)
    print('0  -  Singapore Dollar\n1  -  Malaysian Ringgit\n2  -  Indian Rupee\n3  -  Chinese Yuan\n4  -  Japanese Yen\n5  -  British Pound Sterling\n6  -  Australian Dollar\n7  -  Swiss Franc')
    
    currency = input('Enter the currency you want to convert to: ')
    rate = c.get_rate('USD', 'SGD')
    try:
     # Open the file and read its contents
     with open('cryptoProfile AMENDED.csv') as file:
         data = [line.strip().split(',') for line in file]
      
     # Check if the file has any content
     if not data:
         print("The file is empty!")
         return
    
     # Add numbers at the start
     data[0] = ["No"] + data[0]

     # Create a PrettyTable instance
     table = PrettyTable()
    
     # Set the table's field names
     table.field_names = data[0]  # Use the first row as headers
    
     # Add the remaining rows to the table
     i = 1
     for row in data[1:]:
         table.add_row([i]+ row)
         i += 1

     # Ascertain currency
     if currency == 0:
         # Change currency
         for item in data[1:]:
             for value in item[3:]:
                 amount_in_sgd = c.convert('USD', 'SGD', item)
                 data[value] = amount_in_sgd
      
     # Print the formatted table
     print(table)
  
    except FileNotFoundError:
      print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
    except Exception as e:
      print(f"An error occurred: {e}")

# Call the function
opt6()