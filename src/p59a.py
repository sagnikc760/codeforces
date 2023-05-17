def main():
    s = input()
    count_upper = sum([1 for i in s if i.isupper()])
    count_lower = sum([1 for i in s if i.islower()])
    if count_lower < count_upper:
        print(s.upper())
    else:
        print(s.lower())


main()
