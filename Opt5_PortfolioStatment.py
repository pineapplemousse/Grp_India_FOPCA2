from prettytable import PrettyTable
def opt5():
  with open('cryptoProfile AMENDED.csv') as file:
      data = [line.split(',') for line in file]
      table = PrettyTable()     
      table.field_names = [data[0]]
      for row in data[1:]:
         table.add_row(row)
      print(table)

opt5()