"""
@author: Gustavo Asaph Dilay de Paula
-Resolve jogo da forca (encontra palavras correspondentes ao tamanho e letras usadas)
-Não maximizado (projetar busca para separação da 1 letra se a tiver)
"""

from itertools import product

def Existe(ty):
        x = open('palavras.txt')
        for linha in x:
                if ty in linha:
                        if len(ty) == len(linha) - 1:
                                er = True
                                break
                else:
                        er = False
        return er

def Fazer(p,Alft):
        print('')
        y = product(Alft,repeat = under)
        o = []
        for i in list(y):
                o.append(i)

        for x in o:
                a = (p.format(*x))
                if Existe(a)== True:
                        print('-',a)



Alf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','ç']
Alft = Alf
ui = True
while ui == True:
    ui = False
    Frase = input('Digite seu jogo até agora(ex:_v_): ')
    if Frase.find('_') == -1:
        print('--Não foi digitado os espaços vazios--')
        ui = True

under = Frase.count('_')
FraseL = Frase.split('_')



pru = ''
po = []
print ('\nAgora digite as letras já tentadas que não estão na palavra')
while pru  is not int:
    t = True
    pru = input('\nDigite a proxima letra (para encerrar digite um número): ')
    pru = pru.lower()
    if len(pru) != 1:
        print('---Digite uma letra,sozinha e sem espaços---')
        t = False
        
    try:
        int(pru)
        break
    except ValueError:
        if t == True:
            po.append(pru)


        
for i in po:
    if i in Alft:
        Alft.remove(i)
for i in range(len(FraseL)):
        if FraseL[i] in Alft:
                Alft.remove(FraseL[i])
        
print(Alft)

vezes = len(Alft)**under


p = Frase.replace('_','{}')


Fazer(p,Alft)




