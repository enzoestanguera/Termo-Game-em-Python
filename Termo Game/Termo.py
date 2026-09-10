import random

def criar_tentativas():
    matriz = [
        [" _ ", " _ ", " _ ", " _ ", " _ "],
        [" _ ", " _ ", " _ ", " _ ", " _ "],
        [" _ ", " _ ", " _ ", " _ ", " _ "],
        [" _ ", " _ ", " _ ", " _ ", " _ "],
        [" _ ", " _ ", " _ ", " _ ", " _ "],
        [" _ ", " _ ", " _ ", " _ ", " _ "]
    ]
    return matriz

def mostrar_tabuleiro(matriz):
    print("\nsuas tentativas:")
    for linha in matriz:
        print(str(linha).upper())

def escolher_palavra():
    palavras = ["aguas","amora","amigo","banho","campo","carro","carta","festa","flora","grupo","livro","mente","mundo","noite","terra","peixe","porta","praia","rocha","tempo"]
    indice_palavra = random.randint(0,19)
    palavra_sorteada = palavras[indice_palavra].upper()
    return palavra_sorteada

def pegar_palpite():
    while True:
        try:
            palpite = input("Digite uma palavra de 5 letras: ")
            if len(palpite) != 5:
                raise ValueError("A palavra precisa ter exatamente 5 letras")
            return palpite.upper()
        except ValueError as erro:
            print(f"[erro] {erro}")

def jogar_termo():
    palavra_secreta = escolher_palavra()
    tentativas = criar_tentativas() 

    print("bem vindo ao nosso jogo Termo")
    print("dicas:\n[ ] = se não tiver na palavra\n( ) = existe na palavra, mas ta na posição errada\n letra = se estiver na posição correta")

    for rodada in range(6):
        mostrar_tabuleiro(tentativas)
        print(f"\ntentativa {rodada + 1} de 6")

        palpite = pegar_palpite() 
        for posicao in range(5):
            letra = palpite[posicao]
            if letra == palavra_secreta[posicao]:
                tentativas[rodada][posicao] = f"{letra}" 
            elif letra in palavra_secreta:
                tentativas[rodada][posicao] = f"({letra})"
            else:
                tentativas[rodada][posicao] = f" [{letra}] "

        if palpite == palavra_secreta:
            mostrar_tabuleiro(tentativas)
            print(f"\nparabens! Você acertou a palavra secreta: '{palavra_secreta}'")
            return

    mostrar_tabuleiro(tentativas)
    print(f"\nPerdeu o jogo! A palavra era: '{palavra_secreta}'")

#principal
jogar_termo()