import json
from datetime import datetime

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "exchange_rate.json")

def load_exchange_rates(file_path:str) -> dict:
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    """
    Convert an amount from one currency to another based on exchange rates.

    Args:
        amount: The amount to convert
        from_currency: The currency to convert from
        to_currency: The currency to convert to
        rates: The exchange rates data

    Returns:
        The converted amount or None if conversion is not possible
    """

    if rates is None:
        return None
    
    if from_currency == to_currency:
        return amount

    # Cek apakah mata uang ada
    if from_currency not in rates or to_currency not in rates:
        print(f"Error: Currency {from_currency} or {to_currency} not found in rates.")
        return None

    # Konversi ke base currency (USD)
    amount_in_base = amount / rates[from_currency]

    # Konversi ke target currency
    converted_amount = amount_in_base * rates[to_currency]

    return converted_amount

data = load_exchange_rates(FILE_PATH)
rates = data["rates"] if data else None
amount = 100000
converted = convert_currency(amount, 'IDR', 'USD', rates)

if converted is not None:
    print(f"{amount:,} IDR is equal to {converted:.4f} USD")

