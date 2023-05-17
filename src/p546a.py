def main():
    k, n, w = map(int, input().split(" "))
    total_score = k * ((w * (w + 1)) // 2)
    if total_score > n:
        print(abs(n - total_score))
    else:
        print(0)


main()
