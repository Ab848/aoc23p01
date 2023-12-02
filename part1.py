def get_data():
    file = input("data: ")

    with open(f'{file}.txt') as f:
        return f.read()

def filter_for_nums(x: str) -> str:
    return ''.join(n for n in x if not n.isalpha())

def format_nums(x: str) -> str:
    temp: str = ''

    for n in x.split('\n'):
        temp += '0' if not n else f'{n[0]}{n[-1]}\n'
    
    return sum(int(n) for n in temp.split())


print(format_nums(filter_for_nums(get_data())))
