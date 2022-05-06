def main():
    n=input()
    for i in range(n):
        a,b=input()
        x1=y2=alfa=1 # Valores
        x2=y1=beta=0 # iniciais
        
        print a,'-',x1,y1,'\n',b,'-',x2,y2 #printa 2 primeiras linhas
        resto=a%b #
        div=a//b  # Calcula resto,divisao inteira e armazena b em temp
        temp=b    #
        while (resto!=0):
            alfa=x1-(x2*div) # Segue calculando alfa e beta
            beta=y1-(y2*div) 
            print resto,div,alfa,beta # printa linha
            
            a=temp
            b=resto
            resto=a%b
            div=a//b
            temp=b # atualiza todos os valores
            x1=x2
            y1=y2
            x2=alfa
            y2=beta
            
        print resto,div,'- -\n---' #encerra
if __name__=='__main__':
    main()
