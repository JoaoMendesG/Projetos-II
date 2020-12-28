# função fatorial
def fatorial(n):
    import numpy as np

    fatores = []
    
    while n > 0:
        fatores.append(n)
        n -= 1
    
    return np.prod(fatores)
        
#-----
n = int(input('Informe o número que deseja fatorar !: '))
print(f'O número {n} fatorado resulta em: {fatorial(3)} !')