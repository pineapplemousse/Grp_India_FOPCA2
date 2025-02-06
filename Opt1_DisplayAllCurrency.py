from prettytable import PrettyTable

def opt1():
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
      
    # Print the formatted table
    print(table)
  
  except FileNotFoundError:
      print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
  except Exception as e:
      print(f"An error occurred: {e}")
