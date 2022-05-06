from math import sqrt

def main():
    n=input()
    w=int(sqrt(n))
    l=[i for i in range(3,n,2)]
    l2=l[:]
    print l,'\n',w
    i=0
    while i<=w:
        k=l2[i]
        j=k**2
        if j>n:
            break
        print '{} {} {}'.format(k,j,l.index(j))
        l3=[]
        while j<=n:
            l3.append(j) if j in l else None
            j+=k
        [l2.remove(p) if p in l2 else None for p in l3]
        print l3,'\n',l2
        i+=1
    print [2]+l2

if __name__=='__main__':
    main()
        
