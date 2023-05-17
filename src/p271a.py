def find_next_year(year):
    next_year = year + 1
    while not is_valid_year(next_year):
        next_year += 1
    return next_year

def is_valid_year(year):
    digits = list(str(year))
    digits.sort()
    for i in range(len(digits) - 1):
        if digits[i] == digits[i + 1]:
            return False
    return True


def main():
    y = int(input())
    print(find_next_year(y))


main()
