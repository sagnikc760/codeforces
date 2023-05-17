def main():
    n = int(input())
    value = 0
    for _ in range(n):
        q = input()
        if('++' in q):
            value+=1
        elif('--' in q):
            value-=1
    print(value)

main()