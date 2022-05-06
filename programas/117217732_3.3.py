def main():
    n=input()
    for i in range(n):
        n_int=input()
        lista_fatores=[] #lista de fatores de n_int (sempre reseta com novo n_int)
        for j in range(2,n_int): #calcula j fatores, de 2 ate n_int
            while(n_int%j==0): #enquanto n_int for divisivel por j
                n_int/=j #atualiza n_int
                lista_fatores.append(j) #adiciona fator na lista
            if j in lista_fatores: #se for fator printa (se nao verificar entra em loop)
                print j,lista_fatores.count(j) #printa j e quantas vezes ele aparece na lista
        if(lista_fatores==[]):
            print n_int,'1' #se for primo printa ele proprio como fator
        print '---' #encerra
if __name__=='__main__':
    main()
            
