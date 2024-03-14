import requests

API_KEY = 'fd1464d747619ec8ea636e0d592b5224'  # Replace 'YOUR_API_KEY' with your actual Fixer API key

def getRates():
    endpoint = 'http://data.fixer.io/api/latest'
    params = {'access_key': API_KEY}

    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['rates']
    else:
        print('Failed to retrieve data:', response.status_code)
        return None

def convertCurrency(amount, fromcurr, tocurr, rates):

    if rates is None:
        return None

    from_rate = rates.get(fromcurr)
    to_rate = rates.get(tocurr)

    if from_rate is None or to_rate is None:
        print('Invalid currency')
        return None

    converted_amount = amount * (to_rate / from_rate)
    return converted_amount

if __name__ == '__main__':
    fromcurr = input("Enter the currency you want to convert: ")
    amount = int(input("Enter the amount: "))
    tocurr = input("Enter the currency you want to convert to: ")
    
    rates = getRates() 
    
    converted = convertCurrency(amount, fromcurr, tocurr, rates)
    if converted:
        print('Converted amount:', converted)
