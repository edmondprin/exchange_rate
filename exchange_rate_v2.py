# test
import requests

def get_amount(): # Prompt the user for a valid positive amount.
    while True:
        amount = input("Enter the amount you want to convert: ")
        try:
            amount = int(amount)
            if amount > 0:
                return amount
            print("Only positive numbers are allowed.")
        except ValueError:
            print("enter an integer.")

def get_currency(): # Prompt the user to choose valid source and target currencies.
    currency_list = ['EUR', 'USD', 'CAD', 'JPY', 'AUD', 'GBP']
    for a in currency_list:
        print(a, end=" | ")
    source_currency = input(f"\nEnter the name of the currency you want to be converted? ").strip().upper()
    while source_currency not in currency_list:
        source_currency = input(f"\nEnter the name of the currency you want to be converted? ").strip().upper()
    currency_list.remove(source_currency)
    for a in currency_list:
            print(a, end=" | ")
    target_currency = input(f"\nEnter the name of the currency you want your amount to be converted into: ").strip().upper()
    while target_currency not in currency_list:
        target_currency = input(f"\nEnter the name of the currency you want your amount to be converted into: ").strip().upper()
    return source_currency, target_currency

def get_exchange_rate(source_currency, target_currency): # Retrieve the latest exchange rate from the API.
    # url = "https://api.frankfurter.dev/v1/latest?base=USD&symbols=EUR"
    url = f"https://api.frankfurter.dev/v1/latest?base={source_currency}&symbols={target_currency}"

    response = requests.get(url, timeout=10)
    response.raise_for_status() # checks for unsuccessful HTTP responses such as 404 or 500

    data = response.json() # Convert the HTTP response body (JSON) into a Python dictionary.
    rate = data["rates"][target_currency]

    return rate


def convert_currency(amount, rate): # Calculate the converted amount.
    result = amount * rate
    return result

def main(): # Coordinate the workflow and handle API-related errors.

    amount = get_amount()
    source_currency, target_currency = get_currency()
        
    try:
        rate = get_exchange_rate(source_currency, target_currency)
        converted_amount = convert_currency(amount, rate)
        print(f"{source_currency} {amount:,.2f} = {target_currency} {converted_amount:,.2f}")
    except requests.exceptions.Timeout:
        print("The request timed out.")
    except requests.exceptions.ConnectionError:
        print("An error occured: It can be lack of internet connection or a typo in the URL.")
    except requests.exceptions.HTTPError:
        print("Server returned and HTTP error.")
    except requests.exceptions.JSONDecodeError:
        print("Unable to decode JSON file.")

if __name__ == "__main__":
    main()


