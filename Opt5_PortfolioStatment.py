from prettytable import PrettyTable

def opt5():
  try:
    # Open the file and read its contents
    with open('cryptoProfile AMENDED.csv') as file:
      data = [line.strip().split(',') for line in file]
      
    # Check if the file has any content
    if not data:
      print("The file is empty!")
      return
    
    data[0] = ["No"] + data[0]
    
    # Create a PrettyTable instance
    table = PrettyTable()
    
    # Set the table's field names
    table.field_names = data[0]  # Use the first row as headers
    
    i = 1
    # Add the remaining rows to the table
    for row in data[1:]:
      table.add_row([i]+ row)
      i += 1

    # Remove market cap
    table.del_column('Market Cap')

    # Add total invested
    '''
    TotalInvested = []
    for row in data[1:]:
       a = row[1]*row[2]
       TotalInvested.append(a)
    table.add_column('Total Invested', TotalInvested)
    '''

    # Add invested portfolio size
    '''
    InvestedPortfolioSize = []
    SumOfTotalInvested = 0
    for row in data[1:]:
       SumOfTotalInvested += row[4]
    for row in data[1:]:
       PercentageOfTotalInvested = (row[4] / SumOfTotalInvested)*100
       b = PercentageOfTotalInvested / SumOfTotalInvested
       b = round(b, 2)
       InvestedPortfolioSize.append(b)
    table.add_column('Invested Portfolio Size', InvestedPortfolioSize)
    '''

    # Add total current value
    '''
    TotalCurrentValue = []
    for row in data[1:]:
       c = row[1]*row[3]
       TotalCurrentValue.append(c)
    table.add_column('Total Current Value', TotalCurrentValue)
    '''

    # Add profit / loss
    '''
    ProfitLoss = []
    for row in data[1:]:
        d = row[6] - row[4]
        ProfitLoss.append(d)
    table.add_column('Profit/Loss', ProfitLoss)
    '''

    # Add current portfolio size
    '''
    CurrentPortfolioSize = []
    SumOfTotalCurrentValue = 0
    for row in data[1:]:
       SumOfTotalCurrentValue += row[6]
    for row in data[1:]:
       PercentageOfTotalCurrentValue = (row[6] / SumOfTotalCurrentValue)*100
       e = PercentageOfTotalCurrentValue / SumOfTotalCurrentValue
       e = round(b, 2)
       CurrentPortfolioSize.append(e)
    table.add_column('Current Portfolio Size', CurrentPortfolioSize)
    '''

    # Add sum row
    '''
    SumRow = ['Sum'] + ['-']*8

    SumOfProfitLoss = 0
    for row in data[1:]:
       SumOfProfitLoss += row[7]
      
    SumRow[4] = SumOfTotalInvested
    SumRow[6] = SumOfTotalCurrentValue
    SumRow[7] = SumOfProfitLoss

    table.add_row()
    '''

    # Print the formatted table
    print(table)
  
  except FileNotFoundError:
      print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
  except Exception as e:
      print(f"An error occurred: {e}")

# Call the function
opt5()