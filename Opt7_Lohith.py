#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt

def opt7():
    """
    Reads cryptocurrency data from a CSV file and plots a bar chart for the chosen numeric column.
    
    The CSV file is expected to have the following header:
    Name,Market Cap,Quantity,Buy In Price,Market Price

    The user is prompted to choose one of the numeric columns (Quantity, Buy In Price, or Market Price).
    A bar chart is then generated with the currency names on the x-axis and the chosen values on the y-axis.
    """
    csv_filename = 'cryptoProfile AMENDED.csv'
    
    # Read data from CSV file
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

    # Define the valid numeric columns for plotting
    valid_numeric_columns = ["Quantity", "Buy In Price", "Market Price"]
    print("Available numeric columns to plot:")
    for col in valid_numeric_columns:
        print(f" - {col}")

    # Prompt user to choose a column to plot
    chosen_column = input("Enter the column name you want to plot: ").strip()
    if chosen_column not in valid_numeric_columns:
        print(f"Invalid column. Please choose one of: {', '.join(valid_numeric_columns)}")
        return

    # Extract currency names and the corresponding numeric values from the chosen column
    names = []
    values = []
    for row in data:
        names.append(row["Name"])
        value = float(row[chosen_column])
        values.append(value)

    # Plot a bar chart using Matplotlib
    plt.figure(figsize=(10, 6))
    bars = plt.bar(names, values, color='skyblue')
    plt.xlabel("Currency")
    plt.ylabel(chosen_column)
    plt.title(f"{chosen_column} for each Currency")
    
    # Optionally, add numeric labels above each bar
    max_val = max(values) if values else 1
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.02 * max_val, f'{yval}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show() #print picture