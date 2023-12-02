# get input
def get_data(): 
    file = input("")

    with open(f'{file}.txt') as f:
        return f.read()

# process funcitional info
def proc_data(data: str) -> list:

    one = data.replace('one', 'one1one')
    two = one.replace('two', 'two2two')
    three = two.replace('three', 'three3three')
    four = three.replace('four', 'four4four')
    five = four.replace('five', 'five5five')
    six = five.replace('six', 'six6six')
    seven = six.replace('seven', 'seven7seven')
    eight = seven.replace('eight', 'eight8eight')
    nine = eight.replace('nine', 'nine9nine')
    return ''.join(n for n in nine if not n.isalpha())

def format_nums(data: list) -> str:
    temp: str = ''

    for n in data.split('\n'):
        temp += '0' if not n else f'{n[0]}{n[-1]}\n'
    
    return sum(int(n) for n in temp.split())

print(format_nums(proc_data(get_data())))