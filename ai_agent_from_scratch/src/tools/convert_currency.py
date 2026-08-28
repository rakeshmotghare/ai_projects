import requests

def convert_currency(amount: float, from_currency: str, to_currency: str) -> str:
    '''Live conversion from Frankfurter API(no key required)'''
    try:
        response = requests.get("https://api.frankfurter.app/latest",
                                params={"base": from_currency.upper(), "symbols": to_currency.upper()},
                                timeout=10)
        response.raise_for_status()  # Raise an error for bad responses
        rate = response.json()
        return str(round(amount * rate["rates"][to_currency.upper()], 2))
    except requests.exceptions.RequestException as exc:
        return f"Currency service unavailable: {exc}"
    except KeyError:
        return f"No rate available for {from_currency.upper()} to {to_currency.upper()}"