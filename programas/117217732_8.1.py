def main():
    n=input()
    for i in range(n):
        e_carm=True
        n_int=input()
        n_ori=n_int
        lista_fatores=[] 
        for j in range(2,n_int): 
            while(n_int%j==0): 
                n_int/=j 
                lista_fatores.append(j) 
            if j in lista_fatores: 
                print j,lista_fatores.count(j)
                
        if(lista_fatores==[]):
            print n_int,'1\nNAO'
            e_carm='NaN'
        else:
            for k in range(len(lista_fatores)):
                if(n_ori%(lista_fatores[k]*lista_fatores[k])!=0 and (n_ori-1)%(lista_fatores[k]-1)==0):
                    e_carm=True
                else:
                    e_carm=False
        if(e_carm=='NaN'): print '---'
        elif(e_carm): print 'SIM\n---'
        else: print 'NAO\n---'
if __name__=='__main__':
    main()
            
