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
    
    data[0] = ["No", "Name", "Market Cap", "QtyBought", "Bought Price", "Current Price"]

    # Create a PrettyTable instance
    table = PrettyTable()

    # Set table headers
    table.field_names = data[0]
    
    i = 1
    # Add the remaining rows to the table
    for row in data[1:]:
      table.add_row([i]+ row)
      i += 1

    # Remove market cap
    table.del_column('Market Cap')

    # Add total invested
  
    TotalInvested = []
    for row in data[1:]:
      a = float(row[2])*float(row[3])
      TotalInvested.append(a)
    table.add_column('Total Invested', TotalInvested)

    # Add invested portfolio size
    InvestedPortfolioSize = []
    SumOfTotalInvested = sum(TotalInvested)  #Use the Total Invested values

    for invested in TotalInvested:
      b = (invested / SumOfTotalInvested) * 100 # Calculate the percentage
      b = round(b, 2)  # Round to 2 decimal places
      b = (f'{b}%')
      InvestedPortfolioSize.append(b)

    table.add_column('Invested Portfolio Size', InvestedPortfolioSize)

    # Add total current value
    TotalCurrentValue = []
    for row in data[1:]:
      c = float(row[2])*float(row[4])
      TotalCurrentValue.append(c)
    table.add_column('Total Current Value', TotalCurrentValue)

    # Add profit / loss
    ProfitLoss = []
    for i in range(len(TotalCurrentValue)):
      d = TotalCurrentValue[i] - TotalInvested[i]
      ProfitLoss.append(d)
    table.add_column('Profit/Loss', ProfitLoss)
    
    # Add current portfolio size
    CurrentPortfolioSize = []
    SumOfTotalCurrentValue = sum(TotalCurrentValue)
    for value in TotalCurrentValue:
      PercentageOfTotalCurrentValue = (value / SumOfTotalCurrentValue)*100
      e = round(PercentageOfTotalCurrentValue, 2)
      e = (f'{e}%')
      CurrentPortfolioSize.append(e)
    table.add_column('Current Portfolio Size', CurrentPortfolioSize)
    

    # Add sum row
    SumRow = ['Sum'] + ['-']*9

    SumOfProfitLoss = sum(ProfitLoss)
      
    SumRow[5] = SumOfTotalInvested
    SumRow[7] = SumOfTotalCurrentValue
    SumRow[8] = SumOfProfitLoss

    table.add_row(SumRow)

    # Print the formatted table
    print(table)
  
  except FileNotFoundError:
    print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")

# Call the function
