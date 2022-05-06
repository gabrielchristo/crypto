def impar(E):
    if(E%2==0):return "N"
    else:return "S"
def apm(a,E,m):
        E_ori=E
        r=1
        print r,a,E,impar(E)
        while(E!=0):
            if(impar(E)=="N"):E/=2
            else:
                r=(r*a)%m
                E=(E-1)/2
            a=(a*a)%m
            print r,a,E,impar(E)
        print E_ori,r
        return r
def main():
    n_casos=input()
    for i in range(n_casos):
        inconc=False
        n,b=input()
        k=0
        q=(n-1)
        while(q%2==0):
            k+=1
            q/=2
        print k,q
        t=apm(b,q,n)
        if(t==1 or t==(n-1)):
            print 'INCONCLUSIVO\n---'
            inconc=True
        i=1
        while(i<k):
            q*=2
            t=(t**2)%n
            print q,t
            if(t==(n-1)):
                print 'INCONCLUSIVO\n---'
                inconc=True
                break
            i+=1
        if(inconc==False):print 'COMPOSTO\n---'
if __name__=='__main__':
    main()
