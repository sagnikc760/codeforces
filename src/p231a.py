def main():
    n = int(input())
    count = 0 
    for _ in range(n):
        a,b,c = map(int,input().split(' '))
        if(a==1 and b==1 and c==1):
            count+=1
        elif(a==0 and b==1 and c==1):
            count+=1
        elif(a==1 and b==0 and c==1):
            count+=1
        elif(a==1 and b==1 and c==0):
            count+=1
    print(count)

main()
