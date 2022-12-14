import random

palavras = ['galinha']

palavra = random.choice(palavras)

tentativas = 0

chances = 6

letras_escolhidas = []

estado_atual = ['___'] * len(palavra)

erro1 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||                     
        | ||                     
        |O||               
        | ||
        | ||
        | ||        
        | ||        
        | ||        
        |O||
        | ||
  _=============_
===================
 ''')

erro2 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||                |      
        | ||                     
        |O||               
        | ||
        | ||
        | ||        
        | ||        
        | ||        
        |O||
        | ||
  _=============_
===================
 ''')
erro3 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||               /|      
        | ||                    
        |O||               
        | ||
        | ||
        | ||        
        | ||        
        | ||        
        |O||
        | ||
  _=============_
===================
 ''')

erro4 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||               /|\      
        | ||                   
        |O||               
        | ||
        | ||
        | ||        
        | ||        
        | ||        
        |O||
        | ||
  _=============_
===================
 ''')

erro5 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||               /|\      
        | ||               /      
        |O||               
        | ||
        | ||
        | ||        
        | ||        
        | ||        
        |O||
        | ||
  _=============_
===================
 ''')

erro6 = ('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||               /|\      
        | ||               / \      
        |O||               
        | ||
        | ||
        | ||        ===================================
        | ||        ||          VOC?? PERDEU!         ||
        | ||        ===================================
        |O||
        | ||
  _=============_
===================
 ''')

print('''
        ______________________
        | ===================
        |O||                |
        | ||                |
        | ||                |
        | ||                0
        | ||               /|\      
        | ||               / \      
        |O||               
        | ||
        | ||
        | ||        ===================================
        | ||        || BEM VINDO AO JOGO DA FORCA!!! ||
        | ||        ===================================
        |O||
        | ||
  _=============_
===================
 ''')

print('___ ' * len(palavra))

while tentativas < chances and ''.join(estado_atual) != palavra:

    letra = input("\n\nQual letra voc?? quer tentar? ").lower()

    while letra in letras_escolhidas:
        print("Voc?? escolheu uma letra que j?? tinha tentado, escolha outra")
        letra = input("\nQual letra voc?? quer tentar? ")

    letras_escolhidas.append(letra)

    if letra in palavra:
        print("Parab??ns, voc?? acertou a letra!")
        for i in range(len(palavra)):
            if letra == palavra[i]:
                estado_atual[i] = letra
    else:
        tentativas = tentativas + 1
        if tentativas == 1:
          print(erro1)
        if tentativas == 2:
          print(erro2)
        if tentativas == 3:
          print(erro3)
        if tentativas == 4:
          print(erro4)
        if tentativas == 5:
          print(erro5)
        if tentativas == 6:
          print(erro6)
        

    print("Voc?? j?? fez", tentativas, "tentativas erradas e ainda tem",
          chances - tentativas, "tentativas")

    print("Esse ?? o estado atual:")
    print(estado_atual)

    print("As letras que voc?? j?? tentou s??o:")
    for item in letras_escolhidas:
        print(item, end=" ")

if tentativas == chances:
    print("Acabaram suas tentativas")
else:
    print("\n\nVoc?? ganhou, parab??ns")

print("A palavra era", palavra)
