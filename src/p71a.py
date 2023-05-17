def main():
    n = int(input())
    for _ in range(n):
        p = input()
        if(len(p)<=10):
            print(p)
        else:
            print(p[0]+str(len(p)-2)+p[-1])

main()