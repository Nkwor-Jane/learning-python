"""
The requests module allows you to send HTTP requests using Python.
The HTTP request returns a Response Object with all the response
data (content, encoding, status, etc).
"""
import requests
"""some currency rates to test function:
AUD, CAD, CHF, CNY, GBP, JPY, USD"""

# define to convert currencies
def currency_converter(amount, from_currency, to_currency):
    # set API endpoint for currency conversion
    api_endpoint = f"https://api.exchangeratesapi.io/v1/{from_currency}"

    # set a GET request to the API endpoint
    response = requests.get(api_endpoint)

    # get the JSON data from the response
    data = response.json()

    # extract the exchange rate for target currency
    exchange_rate = data["rates"][to_currency]

    # calculate the converted amount
    converted_amount = amount * exchange_rate

    # return converted amount
    return converted_amount


# prompt the user to enter the amount, source currency and target
amount = float(input("Enter the amount: "))
from_currency = input("Enter the source currency code: ").upper()
to_currency = input("Enter the target currency code: ").upper()

# convert the currency and print the result
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {result} {to_currency}")
