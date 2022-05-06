from math import sqrt

l=[]

def p(primo):
    for i in range(2, primo+1):
            if i != primo:
                    i = primo % i
                    if i == 0:
                            
                            break
            else:
                    l.append(i)
                    break
    
def main():
    n=input()
    for i in range(n):
        p(i)
    print l

        
if __name__=='__main__':
    main()
