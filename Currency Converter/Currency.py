import requests

API_KEY = 'fca_live_xGT2EfOtqlvvss4dIkqmvcDS7xRRMaRJcJJiOQRS'
BASE_URL = f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def convert_currency(base, amount):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()["data"]
        converted_values = {currency: rate * amount for currency, rate in data.items()}
        return converted_values
    except Exception as e:
        print("Invalid Currency!")
        return None
while True:
    base = input("Enter the base currency (q for quit): ").upper()

    if base == "Q":
        break

    try:
        amount = float(input("Enter the amount in {} to convert: ".format(base)))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue

    converted_values = convert_currency(base, amount)

    if not converted_values:
        continue

    for currency, value in converted_values.items():
        print(f"{currency}: {value:.2f}")