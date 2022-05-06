def main():
    n=input()
    for i in range(n):
        mdc=0
        c_linha=0
        a,b,c=input() # pega a,b e c
        x1=y2=alfa=1 # valores iniciais
        x2=y1=beta=0
        print a,'-',x1,y1,'\n',b,'-',x2,y2 #printa 2 primeiras linhas
        resto=a%b
        div=a//b #resto,divisao inteira e armazena b em temp
        temp=b
        
        while (resto!=0):
            alfa=x1-(x2*div) #segue calculando alfa e beta
            beta=y1-(y2*div)
            print resto,div,alfa,beta
            a=temp
            b=resto
            if(resto>0):
                mdc=resto #pega o mdc
            resto=a%b
            div=a//b
            temp=b #atualiza valores
            x1=x2
            y1=y2
            x2=alfa
            y2=beta
        if (c%mdc==0):
            c_linha=c/mdc # verifica se mdc divide c e calcula c linha
            
        x_solucao=alfa*c_linha #solucoes equacao
        y_solucao=beta*c_linha
        print resto,div,'- -\n',x_solucao,y_solucao,'\n---' #printa resultado e encerra
if __name__=='__main__':
    main()
