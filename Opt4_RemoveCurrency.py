import csv

def opt4():
    # Hard-coded file name
    filename = "cryptoProfile AMENDED.csv"
    
    # Open the file and read all rows
    file = open(filename, "r")
    reader = csv.reader(file)
    all_rows = list(reader)
    file.close()
    
    # Check if file has any content
    if len(all_rows) == 0:
        print("The file is empty!")
        return
    
    # The first row is the header; the rest are the data rows.
    header = all_rows[0]
    data = all_rows[1:]
    
    # If there is no data, print a message and exit.
    if len(data) == 0:
        print("There are no cryptocurrencies to remove.")
        return
    
    # Display the list of cryptocurrencies with a number.
    print("Which cryptocurrency do you want to remove?")
    for i in range(len(data)):
        # We assume the first column is the name.
        print(str(i) + " - " + data[i][0])
    print("E - Exit")
    
    # Get the user's choice.
    choice = input("Enter the number of the cryptocurrency to remove or E to exit: ")
    
    # Check if the user wants to exit.
    if choice.upper() == "E":
        print("Exiting...")
        return
    
    # Try to convert the choice into an integer.
    try:
        index = int(choice)
    except:
        print("That's not a valid number!")
        return
    
    # Check if the index is valid.
    if index < 0 or index >= len(data):
        print("Invalid index!")
        return
    
    # Save the name of the cryptocurrency we are about to remove.
    removed_crypto = data[index][0]
    
    # Remove the chosen cryptocurrency.
    del data[index]
    print("Removed " + removed_crypto)
    
    # Write the header and the remaining data back into the CSV file.
    file = open(filename, "w", newline="")
    writer = csv.writer(file)
    writer.writerow(header)
    for row in data:
        writer.writerow(row)
    file.close()
    
    print("The file has been updated.")

opt4()