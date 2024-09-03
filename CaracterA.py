def caracter(texto):

    texto = texto.lower()
    
    quantidade = texto.count('a')

    existe = quantidade > 0
    
    if existe:
        print(f"A letra 'a' aparece {quantidade} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")


palavra = input("Digite uma string: ")

caracter(palavra)


    