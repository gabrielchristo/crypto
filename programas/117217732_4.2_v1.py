from math import sqrt

lista=[]
novalista=[]
def main():
    n=input()
    for i in range(3,n):
        if(i%2!=0):
            lista.append(i)
    print lista,'\n',int(sqrt(n))
    for i in range(len(lista)):
        if(lista[i]!=0):
            if(pow(lista[i],2) in lista):
                print lista[i],pow(lista[i],2),lista.index(pow(lista[i],2))
                retira(lista[i])
            else:
                novalista.insert(0,2)
                break
    print novalista+lista
def retira(passo):
    lista_temp=[]
    lista_surv=[]   #nao tive tempo de arrumar o bug quando i>lista[0]
    p=passo         #nem de fazer o trabalho com calma
    while(passo<=len(lista)): #nem de comentar
        lista_temp.append(lista[passo])
        lista[passo]=0
        passo+=p
    print lista_temp
    for i in range(len(lista)):
        if(lista[i]!=0):
            lista_surv.append(lista[i])
    print lista_surv
    novalista=lista_surv
if __name__=='__main__':
    main()
