def mdc(n1,n2):
    r=None
    while(r!=0):
        r=n1%n2
        n1=n2
        n2=r
    return n1

def main():
    k=input()
    for i in range(k):
        n=input()
        l=[]
        for j in range(n):
            if(mdc(j,n)==1):l.append(j)
        print l

if __name__=='__main__':
    main()
