def main():
    n=input()
    for i in range(n):
        a,b=input()
        x1=y2=alfa=1
        x2=y1=beta=0
        print a,'-',x1,y1,'\n',b,'-',x2,y2
        div=a//b
        resto=a%b
        temp=b
        while(resto!=0):
            alfa=x1-(div*x2)
            beta=y1-(div*y2)
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
        print resto,div,'- -\n---'
if __name__=='__main__':
    main()
