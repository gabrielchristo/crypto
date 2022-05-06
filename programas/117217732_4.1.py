from math import sqrt

def main():
    n=input()
    for i in range(n):
        n_int=input()
        x=int(sqrt(n_int))
        y=0
        if(n_int==pow(x,2)-pow(y,2)):
            print x,y,'S\n',x-y,x+y,'\n---'
        while (n_int!=((x*x)-(y*y))):
            print x,y,'N'
            x+=1
            y=int(sqrt(pow(x,2)-n_int))
            if (x==(n_int+1)/2):
                print 1,n_int,'\n---'
                break
            if(n_int==pow(x,2)-pow(y,2)):
                print x,y,'S\n',x-y,x+y,'\n---'
                break
if __name__=='__main__':
    main()
