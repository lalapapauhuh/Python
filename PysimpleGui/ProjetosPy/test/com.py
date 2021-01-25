def conteInvertido(num):
    if num >= 0:
        print(num)
        conteInvertido(num - 1)
        return


if __name__ == "__main__":
    import sys
    conteInvertido(int(sys.argv[1]))