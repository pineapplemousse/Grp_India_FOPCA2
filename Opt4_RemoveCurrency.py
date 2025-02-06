import csv

def opt4():
    
    filename = "cryptoProfile AMENDED.csv"
    
    
    file = open(filename, "r")
    reader = csv.reader(file)
    all_rows = list(reader)
    file.close()
    
    
    if len(all_rows) == 0:
        print("The file is empty!")
        return
    
    
    header = all_rows[0]
    data = all_rows[1:]
    
    
    if len(data) == 0:
        print("There are no cryptocurrencies to remove.")
        return
    
    
    print("Which cryptocurrency do you want to remove?")
    for i in range(len(data)):
        
        print(str(i) + " - " + data[i][0])
    print("E - Exit")
    
    
    choice = input("Enter the number of the cryptocurrency to remove or E to exit: ")
    
    
    if choice.upper() == "E":
        print("Exiting...")
        return
    
    
    try:
        index = int(choice)
    except:
        print("That's not a valid number!")
        return
    
    
    if index < 0 or index >= len(data):
        print("Invalid index!")
        return
    
    
    removed_crypto = data[index][0]
    
    
    del data[index]
    print("Removed " + removed_crypto)
    
    
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)
    file.close()
    
    print("The file has been updated.")
