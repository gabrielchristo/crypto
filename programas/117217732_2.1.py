def main():
    n=input() #numero de pares
    for i in range(n):
        a,b=input()
        r=a #resto igual ao valor a
        q=0 #quociente igual a 0
        print q,a
        while r>=b: #-----------------|
            q+=1    #algoritmo ingenuo|
            r-=b    #-----------------|
            print q,r
            if r<b:
                print '---' #se resto menor que b printa tres tracos
if __name__=='__main__':
    main()
