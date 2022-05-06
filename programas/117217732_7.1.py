def main():
    n=input()
    for i in range(n):
        mdc=0
        a,b=input()
        b_ori=b
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
            if(resto>0):
                mdc=resto
            resto=a%b
            div=a//b
            temp=b 
            x1=x2
            y1=y2
            x2=alfa
            y2=beta
        print resto,div,'- -'
        if(mdc==1):print alfa%b_ori,'\n---'
        else:print '0\n---'
if __name__=='__main__':
    main()
