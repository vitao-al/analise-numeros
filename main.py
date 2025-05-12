def analiseDeListaDeNumeros(numeros):
    soma = 0
    maiorNum = max(numeros)
    menorNum = min(numeros)
    qtdNumPar = 0

    for numero in numeros:
        soma += numero
        if numero % 2 == 0:
            qtdNumPar += 1

    media = soma / len(numeros)

    return print(f"Média: {media:.2f}\nMaior número: {maiorNum}\nMenor número: {menorNum}\nQuantidade de números pares: {qtdNumPar}")