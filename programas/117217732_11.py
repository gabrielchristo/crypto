def aif(n):
    l=[]
    cont=[]
    for i in range(2,n):
        while(n%i==0): 
            n/=i
            if(i not in l):cont.append(i)
            l.append(i)
        if i in l:print i,l.count(i)
    if(l==[]):print n,'1'
    return l,cont

def main():
    k=input()
    for i in range(k):
        p=input()
        l,cont=aif(p-1)
        j,g=1,1
        while(j<=len(cont)):
            a=2
            while((pow(a,(p-1)/cont[j-1])-1)%p==0):
                a+=1
            h=(pow(a,(p-1)/pow(cont[j-1],l.count(cont[j-1]))))%p
            print cont[j-1],a,h
            g=(g*h)%p
            j+=1
        print g,'\n---'

if __name__=='__main__':
    main()
