"""
@author: Gustavo Asaph Dilay de Paula
-Jogo da Forca automatizado, propõe palavras aleatórias, aceita tentativas e testa respostas
-Não maximizado
"""
import random

def Inicial(B):
	Agora = []
	Format = '_'
	for X in B:
		Agora.append(Format)
	return Agora


def TiraInicial(Letra,Palavra,ListaEsta):
    u = -1
    for h in Palavra:
        u += 1
        if h == Letra:
            ListaEsta[u] = Letra
    return ListaEsta

def PROPT(Comp):
        lil = []
        tup = ''
        for x in range(Comp):
                lil.append('{%s} '%(x))
        lona = tup.join(lil)
        return lona

Dif = True

while Dif == True:
    Dificuldade = input('\nDeseja jogar na dificuldade 1 ou 2? ')
    if Dificuldade == '1' or Dificuldade == '2':
        Dif = False
    else:
        print('===Responda com 1 ou 2 apenas===')

while Dif == False:
    Vida = input('Jogar com tentativas limitadas?[S/N] ')
    if Vida == 'S' or Vida == 's' or Vida =='n' or Vida == 'N':
        Dif = True
    else:
        print("===Responda apenas com 'S' ou 'N'===")

if Dificuldade == '1':
    Aberto = open('facil.txt')
    Linha = random.randrange(1,39)
if Dificuldade == '2':
    Aberto = open('palavras.txt')
    Linha = random.randrange(1,320100)

while Linha != 0:
    Aberto.readline()
    Linha = Linha - 1
    

Resposta = Aberto.readline()
Resposta = Resposta.replace(Resposta[-1],'')
Resposta = Resposta.lower()

Comprimento = len(Resposta)

Atua = ('_ '*Comprimento)
print('Sua palavra é: ',Atua)

Resposta1 = Resposta
Acertou = 'nao'
Chave = True
Foi = []
ATUAL = Inicial(Resposta)
asdf = len(Resposta)
prop = PROPT(asdf)





if Vida == 'S' or Vida == 's':
    chance = 10

while Acertou == 'nao':
    while Chave == True:
        tr = 1
        Tenta = input('\nDigite uma Letra: ')
        if len(Tenta) > 1:
            print('===Digite apenas uma letra===')
            tr = 2
        if Tenta in Foi:
            print('Essa Letra já foi ultilizada')
        if tr == 1:
            Chave = False
    Foi.append(Tenta)
    if Tenta not in Resposta:
        print('\nA letra ultilizada não está na palavra')
    
     

    if Tenta in Resposta:
        ATUAL = TiraInicial(Tenta,Resposta,ATUAL)
        
    print('\nLetras já ultilizadas:',Foi)
    print(prop.format(*ATUAL))
    




    
    Tentou = input('\nQual é a palavra? ')
    if Tentou == Resposta1:
        Acertou = 'Sim'
        print('\n Parábens!!!Você acertou')
    else:
        print('===Você errou===')
    if Vida == 'S' or Vida == 's':
        chance -= 1
        print('\nVocê tem mais {} tentativas'.format(chance))
        if chance == 0:
            print('\n Você errou demais e perdeu')
            break

    Chave = True
    
        
