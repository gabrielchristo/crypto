def main():
    n=input()
    for i in range(n):
        a,b=input()
        print a,"\n"+str(b)
        #temp=b #divisor
        while b!=0: #enquanto divisor for diferente de zero
            temp=b
            b=a%b #b igual a resto de a%b
            a=temp #a assume antigo valor de b
            print b
        print '---'
if __name__=='__main__':
    main()
