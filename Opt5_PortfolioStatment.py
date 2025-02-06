from prettytable import PrettyTable

def opt5():
  try:
    
    with open('cryptoProfile AMENDED.csv') as file:
      data = [line.strip().split(',') for line in file]
      
    
    if data == 0:
      print("The file is empty!")
      return
    
    data[0] = ["No", "Name", "Market Cap", "QtyBought", "Bought Price", "Current Price"]

    
    table = PrettyTable()

    
    table.field_names = data[0]
    
    i = 1
    
    for row in data[1:]:
      table.add_row([i]+ row)
      i += 1

    
    table.del_column('Market Cap')

    
    
    TotalInvested = []
    for row in data[1:]:
      a = float(row[2])*float(row[3])
      TotalInvested.append(a)
    table.add_column('Total Invested', TotalInvested)

    
    InvestedPortfolioSize = []
    SumOfTotalInvested = sum(TotalInvested)  

    for invested in TotalInvested:
      b = (invested / SumOfTotalInvested) * 100 
      b = round(b, 2)  
      b = (f'{b}%')
      InvestedPortfolioSize.append(b)
    table.add_column('Invested Portfolio Size', InvestedPortfolioSize)

    
    TotalCurrentValue = []
    for row in data[1:]:
      c = float(row[2])*float(row[4])
      TotalCurrentValue.append(c)
    table.add_column('Total Current Value', TotalCurrentValue)

    
    ProfitLoss = []
    for i in range(len(TotalCurrentValue)):
      d = TotalCurrentValue[i] - TotalInvested[i]
      ProfitLoss.append(d)
    table.add_column('Profit/Loss', ProfitLoss)
    
    
    CurrentPortfolioSize = []
    SumOfTotalCurrentValue = sum(TotalCurrentValue)
    for value in TotalCurrentValue:
      PercentageOfTotalCurrentValue = (value / SumOfTotalCurrentValue)*100
      e = round(PercentageOfTotalCurrentValue, 2)
      e = (f'{e}%')
      CurrentPortfolioSize.append(e)
    table.add_column('Current Portfolio Size', CurrentPortfolioSize)
    

    
    SumRow = ['Sum'] + ['-']*9

    SumOfProfitLoss = sum(ProfitLoss)
      
    SumRow[5] = SumOfTotalInvested
    SumRow[7] = SumOfTotalCurrentValue
    SumRow[8] = SumOfProfitLoss

    table.add_row(SumRow)

    
    print(table)
  
  except FileNotFoundError:
    print("Error: The file 'cryptoProfile AMENDED.csv' was not found.")
  except Exception as e:
    print(f"An error occurred: {e}")


