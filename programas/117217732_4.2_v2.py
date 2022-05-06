from math import sqrt

lista=[]
def main():
    n=input()

    for i in range(3,n):
        if(i%2!=0):
            lista.append(i)
    print lista,'\n',int(sqrt(n))

    k=int(sqrt(n))
    l=0
    while (k<lista[l]):
        if(lista[l]!=0):
            print lista[l],pow(lista[l],2),lista.index(pow(lista[l],2))
            r(lista[l])
            l+=1


def r(passo):
    p=passo
    lista_temp=[]
    lista_surv=[]
    while(passo<=len(lista)):
        lista_temp.append(lista[passo])
        lista[passo]=0
        passo+=p
    print lista_temp
    for j in range(len(lista)):
        if(lista[j]!=0):
            lista_surv.append(lista[j])
    print lista_surv


if __name__=='__main__':
    main()
