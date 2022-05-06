def impar(E):
    if(E%2==0):
        return "N"
    else:
        return "S"
def main():
    n=input()
    for i in range(n):
        m,a=input()
        E=(m-1)
        r=1
        print r,a,E,impar(E)
        while(E!=0):
            if(impar(E)=="N"):
                E/=2
            else:
                r=(r*a)%m
                E=(E-1)/2
            a=(a*a)%m
            print r,a,E,impar(E)
        if(r==1): print 'INCONCLUSIVO\n---'
        else: print 'COMPOSTO\n---'
if __name__=='__main__':
    main()
