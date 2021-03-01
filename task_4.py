def main(argv):
    from utils import get_rubles
    if len(argv) <= 1:
        result = get_rubles(input("Укажите валюту: "))
    else:
        result = get_rubles(argv[1])
    return f'{result[0]}, {result[1]}'


'''
print('USD: ', get_rubles('USD'))
print('usd: ', get_rubles('usd'))
print('EUR: ', get_rubles('EUR'))
print('GBR: ', get_rubles('GBR'))
print('AMD: ', get_rubles('AMD'))
print('ver: ', get_rubles('ver'))
print('win: ', get_rubles('win'))
print('xml: ', get_rubles('xml'))
'''

if __name__ == '__main__':
    import sys
    exit(main(sys.argv))
