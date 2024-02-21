def main():
    while(True):
        n = int(input())
        palabras = [0 for i in range(n)]
        maximo = -1
        for i in range(n):
            mayusculas = 0
            palabra = input()
            palabras[i] = palabra
            for letra in palabra:
                if letra.isupper():
                    mayusculas += 1
            if mayusculas == len(palabra):
                mayusculas = 0
            if mayusculas >= maximo:
                maximo = mayusculas
                indice_maximo = i
        for i in range(n):
            if (palabras[indice_maximo].lower() == palabras[i].lower()):
                print(palabras[indice_maximo])
            else:
                print(palabras[i])
        print("---")
if __name__ == "__main__":
    main()