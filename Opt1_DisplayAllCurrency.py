from prettytable import PrettyTable

def opt1():
  try:
    
    with open('cryptoProfile AMENDED.csv') as file:
      data = [line.strip().split(',') for line in file]
      
    
    if data == 0:
      print("The file is empty!")
      return
    
    
    data[0] = ["No"] + data[0]

    
    table = PrettyTable()
    
    
    table.field_names = data[0]  
    
    
    i = 1
    for row in data[1:]:
      table.add_row([i]+ row)
      i += 1
      
    
    print(table)
  
  except Exception as e:
      print(f"An error occurred: {e}")