def main():
    n=input()
    for i in range(n):
        a,b,m=input()
        print a%m,b%m,(a+b)%m,(a-b)%m,(a*b)%m
if __name__=='__main__':
    main()
