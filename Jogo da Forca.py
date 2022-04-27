# Jogo da Forca

secreto = 'teste'
digitadas = []
chances = 3

while True:
    if chances <0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Te orienta! Digite apenas uma letra!')
        continue

    digitadas.append(letra) #acrescenta na lista
    if letra in secreto:
        print('A letra "{}" está dentro da palavra secreta!' .format(letra))
    else:
        print('A letra "{}" não existe na palavra secreta' .format(letra))
        digitadas.pop() #elimina a última na lista

    secreto_temporario = ''
    for letra_secreta in secreto: # Para letra secreta estiver em secreto
        if letra_secreta in digitadas: # se a letra está em digitadas
            secreto_temporario += letra_secreta # secreto temporario será a letra secreta que está conectada no secreto e digitadas
        else:
            secreto_temporario += '*' # Coloque * se estiver incorreta

    if secreto_temporario == secreto:
        print('A frase é "{}", parabéns!' .format(secreto_temporario))
        break
    else:
        print('Sua frase está assim: {}' .format(secreto_temporario))

    if letra not in secreto:
        chances -= 1
    print('Você ainda tem {} chances.' .format(chances))
