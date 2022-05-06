def aif(n):
    l=[] 
    for j in range(2,n): 
        while(n%j==0):
            n/=j
            l.append(j) 
        if j in l:print j,l.count(j)
    if(l==[]):print n,'1'
    return l

def mdc(a,b):
    while b:
        a,b=b,a%b
    return a

def fi(n):
    m=n-1
    cont=0
    while m:
        if not mdc(n,m)-1:cont+=1
        m-=1
    print cont

def main():
    k=input()
    for i in range(k):
        cont=0
        n=input()
        l=aif(n)
        fi(n)
        print '---'

if __name__ == '__main__':
    main()
