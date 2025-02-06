
import csv
import matplotlib.pyplot as plt

def opt7():

    csv_filename = 'cryptoProfile AMENDED.csv'
    
    
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    
    valid_numeric_columns = ["Quantity", "Buy In Price", "Market Price"]
    print("Available numeric columns to plot:")
    for col in valid_numeric_columns:
        print(f" - {col}")

    
    chosen_column = input("Enter the column name you want to plot: ")
    if chosen_column not in valid_numeric_columns:
        print(f"Invalid column. Please type either Quantity, Buy In Price, or Market Price.")
        return

    
    names = []
    values = []
    for row in data:
        names.append(row["Name"])
        value = float(row[chosen_column])
        values.append(value)

    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, values, color='skyblue')
    plt.xlabel("Currency")
    plt.ylabel(chosen_column)
    plt.title(f"{chosen_column} for each Currency")
    
    
    
    max_val = max(values) if values else 1
    
    
    for bar in bars:
        
        yval = bar.get_height()
        
        
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02 * max_val, f'{yval}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show() 