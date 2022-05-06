def aee(a,b):
    x1=y2=alfa=1 
    x2=y1=beta=0 
    print a,'-',x1,y1,'\n',b,'-',x2,y2
    resto=a%b 
    div=a//b  
    temp=b    
    while (resto!=0):
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
def main():
    n_duplas=input()
    for i in range(n_duplas):
        #for j in range(len(l2)-1):nao tive tempo para fazer >3 congruencias
        l1,l2=input()
        alfa,beta=aee(l2[0],l2[1])
        print alfa,beta
        mod=l2[0]*l2[1]
        x=((l1[0]*beta*l2[1])+(l1[1]*alfa*l2[0]))%mod
        print x,mod
        alfa,beta=aee(mod,l2[2])
        print alfa,beta
        mod_ori=mod
        mod*=l2[2]
        x=((x*beta*l2[2])+(l1[2]*alfa*mod_ori))%mod
        print x,mod,'\n---'
if __name__=='__main__':
    main()
