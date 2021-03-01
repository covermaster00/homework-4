def get_rubles(currency):
    from requests import get, utils
    from decimal import Decimal
    from datetime import date
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    currency = currency.upper()
    # Значение валюты в <type: Decimal>
    if content.find(f'<CharCode>{currency}') == -1:
        rub = None
    else:
        _ = content[content.find('<Value>', content.find(currency)) + 7: content.find('</Value>', content.find(currency))]
        rub = Decimal(_.replace(',', '.')).quantize(Decimal('1.00'))
    # Значение даты в <type: date>
    str_date = content.find('<ValCurs Date=')
    if str_date == -1:
        date1 = None
    else:
        date1 = (content[content.find('<ValCurs Date=') + 15: content.find('<ValCurs Date=') + 25]).split('.')
        date1.reverse()
        date1 = date.fromisoformat('-'.join(date1))
    return rub, date1


if __name__ == '__main__':
    exit('This is module')
