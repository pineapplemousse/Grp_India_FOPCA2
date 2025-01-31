# Convert crypto prices to other forms of currency
from forex_python.converter import CurrencyRates

# Create a CurrencyRates instance
c = CurrencyRates()

# Get exchange rate from USD to EUR
rate = c.get_rate('USD', 'EUR')
print(f"Exchange rate (USD to EUR): {rate}")

# Convert 100 USD to EUR
amount_in_eur = c.convert('USD', 'EUR', 100)
print(f"100 USD in EUR: {amount_in_eur}")