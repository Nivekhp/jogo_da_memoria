import time
import random

def inicio():
    # Variaveis
    lista = ["Adriel", "Adriel", 'Daniel', 'Daniel', 'Endi', 'Endi', 'Karine', 'Karine', 'Kevin', 'Kevin', 'Kelmer',
             'Kelmer', 'Leandro', 'Leandro', 'Renan', 'Renan']
    mostra = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
    cont = 0
    tentativas = 0
    pontos = 0
    total = 0
    econt = 0
    erros = 0
    # Embaralhar lista
    random.shuffle(lista)
    nome = input("Digite seu nome: ")
    apresentacao(lista, econt)
    jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total, erros)

def apresentacao(lista, econt):
    print("\nMemorize os locais de cada nome por 15 segundos\n")
    for e in lista:
        print(e, end="\t")
        econt = econt + 1
        if econt == 4:
            print("\n")
            econt = 0
    time.sleep(15)

    print('\n' * 10)
    print('É hora de jogar\n')

def jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total, erros):
    # Loop para continuar no jogo até não haver opções
    while cont < 8:
        for e in mostra:
            print(e, end="\t")
            econt = econt + 1
            if econt == 4:
                print("\n")
                econt = 0
        try:
            n1 = int(input("Digite um número para abrir uma casa: "))
            if (n1 < 1) or (n1 > 16):
                print('\n' * 10)
                print('Atenção! Não é possível abrir uma casa que não existe\n')
                jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)
        except Exception:
            print('\n' * 10)
            print('Atenção! Não é possível abrir uma casa que não existe\n')
            jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)

        if (mostra[n1 - 1] != lista[n1 - 1]):
            print('Você abriu a casa = ', lista[n1 - 1])

            try:
                n2 = int(input("Digite outro número para abrir outra casa: "))
                if (n2 < 1) or (n2 > 16):
                    print('\n' * 10)
                    print('Atenção! Não é possível abrir uma casa que não existe\n')
                    jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)
            except Exception:
                print('\n' * 10)
                print('Atenção! Não é possível abrir uma casa que não existe\n')
                jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)

            if (mostra[n1 - 1] != lista[n1 - 1]):
                print('Você abriu a casa = ', lista[n2 - 1])
                time.sleep(1)
            else:
                print('\n' * 10)
                print("Você digitou uma casa já aberta!\n")
                jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)
        else:
            print('\n' * 10)
            print("Você digitou uma casa já aberta!\n")
            jogo(lista, mostra, cont, tentativas, pontos, econt, nome, total,erros)

        # Verificar se usuario acertou
        if lista[n1 - 1] == lista[n2 - 1]:
            if n1 != n2:
                print('\n' * 10)
                print("Você acertou!\n")
                cont = cont + 1
                mostra[n1 - 1] = lista[n1 - 1]
                mostra[n2 - 1] = lista[n2 - 1]
                tentativas = tentativas + 1
                pontos = pontos + 100
            else:
                print('\n' * 10)
                print("Você digitou a mesma opção!\n")
        else:
            print('\n' * 10)
            print("Você errou! Tente Novamente\n")
            tentativas = tentativas + 1
            erros = erros + 1
    total = pontos / tentativas
    final(nome, tentativas, pontos, total, erros)

def final(nome, tentativas, pontos, total, erros):
    # Contar pontuação e gravar em arquivo
    # print("Parabens ",nome,"!!!")
    # print("Tentativas")
    # print("Sua pontuação total foi = ", total)
    texto = []
    print("Parabéns {}\nForam {} erros\nVocê atingiu {:.2f} pontos".format(nome, erros, total))
    arquivo = open('pontuacao.txt', 'a')
    texto.append('Nome:{} \n'.format(nome))
    texto.append('Tentativas: {} \n'.format(tentativas))
    texto.append('Erros:  {}\n'.format(erros))
    texto.append('Pontos: {:.2f} \n'.format(total))
    texto.append('  \n')
    arquivo.writelines(texto)
    arquivo.close()

inicio()


