import re

def generator_numbers(string=""):
    numbers = re.findall(r'/-?\b\d+[.]\d+\b', string)

    for number in numbers:
        yield int(number)

def sum_profit(string):
    total_profit = sum(generator_numbers(string))
    return total_profit

print(sum_profit('Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів'))
