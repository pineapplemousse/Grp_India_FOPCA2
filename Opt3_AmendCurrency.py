import csv
from prettytable import PrettyTable
def opt3():
 file_path = "cryptoProfile AMENDED.csv"  # Ensure this file exists in your directory 
 with open (file_path, mode='r', newline='') as file:
  reader=csv.reader(file)
  all_rows=list(reader)

  if not all_rows:
   print("The csv file is empty.")
   header = all_rows[0]
   data=all_rows[1:]
   try:
  while True:
   print("No - CryptoCurrency")
   print("---------------------------")
   print("0 - Bitcoin\n1 - Etherum\n2 -Solana\n3 - Decentraland\n4 - The Sandbox\n5 - Dodgecoin\n6 - Shiba Inu")
   print("---------------------------")
   selection=input("Enter 0 to 6 for your selection or E to exit : ").strip()
   index=print(f"Index                : {selection}")
  
   for i in range(len(data)):
    print(f"{i}-{data[i][name_idx]}")
  
  
   if edit<0 or edit>6:
    print("Invalid Option, Please try again.")

     
  

  
