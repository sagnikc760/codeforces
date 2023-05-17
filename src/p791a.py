def main():
    a, b = map(int, input().split(" "))
    count = 0
    while a <= b:
        count += 1
        a = 3 * a 
        b = b * 2 
    print(count)


main()
