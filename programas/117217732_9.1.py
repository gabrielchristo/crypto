def aif(n):
    l=[] 
    for i in range(2,n):
        while(n%i==0): 
            n/=i
            l.append(i)
        if i in l:print i,l.count(i)
    #if(l==[]):print n,'1'           
    return l

def aee(a,b):
    x1=y2=alfa=1 
    x2=y1=beta=0 
    print a,'-',x1,y1,'\n',b,'-',x2,y2
    resto=a%b 
    div=a//b  
    temp=b    
    while(resto!=0):
        alfa=x1-(x2*div) 
        beta=y1-(y2*div) 
        print resto,div,alfa,beta 
        a=temp
        b=resto
        resto=a%b
        div=a//b
        temp=b 
        x1=x2
        y1=y2
        x2=alfa
        y2=beta       
    print resto,div,'- -'
    return alfa,beta

def impar(E):
    if(E%2==0):return "N"
    else:return "S"

def apm_fermat(a,E,m):
    E%=(m-1)
    print E
    r=1
    print r,a,E,impar(E)
    while(E!=0):
        if(impar(E)=="N"):E/=2
        else:
            r=(r*a)%m
            E=(E-1)/2
        a=(a*a)%m
        print r,a,E,impar(E)
    return r

def acr(l1,l2):
    alfa,beta=aee(l2[0],l2[1])
    print alfa,beta
    mod=l2[0]*l2[1]
    x=((l1[0]*beta*l2[1])+(l1[1]*alfa*l2[0]))%mod
    print x,mod
    
    i=2
    while(i<len(l2)):
        alfa,beta=aee(mod,l2[i])
        print alfa,beta
        mod_ori=mod
        mod*=l2[i]
        x=((x*beta*l2[i])+(l1[i]*alfa*mod_ori))%mod
        print x,mod
        i+=1
    print '---'

def main():
    n_casos=input()
    for i in range(n_casos):
        b,e,m=input()
        l_fatores=aif(m)
        l_cong=[]
        for j in range(len(l_fatores)):
            if(b%l_fatores[j]==0):
                l_cong.append(0)
                print 0
            else:l_cong.append(apm_fermat(b,e,l_fatores[j]))
        acr(l_cong,l_fatores)

if __name__ == '__main__':
    main()
