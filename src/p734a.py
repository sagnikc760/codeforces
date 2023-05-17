def main():
    n = int(input())
    s = input()
    anton_count = sum([1 for i in s if i == "A"])
    danik_count = sum([1 for i in s if i == "D"])
    if(anton_count > danik_count):
        print("Anton")
    elif(danik_count> anton_count):
        print("Danik")
    else:
        print("Friendship")

main()