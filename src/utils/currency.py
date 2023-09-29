from forex_python.converter import CurrencyRates

c = CurrencyRates()

CURRENCIES = [
    "EUR - European Euro",
    "JPY - Japanese Yen",
    "BGN - Bulgarian Lev",
    "CZK - Czech Koruna",
    "DKK - Danish Krone",
    "GBP - British Pound",
    "HUF - Hungarian Forint",
    "PLN - Polish Zloty",
    "RON - Romanian Leu",
    "SEK - Swedish Krona",
    "CHF - Swiss Franc",
    "ISK - Icelandic Króna",
    "NOK - Norwegian Krone",
    "TRY - Turkish New Lira",
    "AUD - Australian Dollar",
    "BRL - Brazilian Real",
    "CAD - Canadian Dollar",
    "CNY - Chinese/Yuan Renminbi",
    "HKD - Hong Kong Dollar",
    "IDR - Indonesian Rupiah",
    "INR - Indian Rupee",
    "KRW - South Korean Won",
    "MXN - Mexican Peso",
    "MYR - Malaysian Ringgit",
    "NZD - New Zealand Dollar",
    "PHP - Philippine Peso",
    "SGD - Singapore Dollar",
    "THB - Thai Baht",
    "ZAR - South African Rand",
]


def convert_currency(amount, from_currency, to_currency):
    return round(c.convert(from_currency, to_currency, amount), 2)
