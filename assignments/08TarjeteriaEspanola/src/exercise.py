
def main():
    #escribe tu código abajo de esta línea
    def Tarjetas(plumones,pliegos):
        tpp=(plumones*35)
        tppa=(pliegos*12)
        if tpp>tppa:
            print('El número de tarjetas que se puede hacer es: %i' %tppa)
        elif tppa>tpp:
            print('El número de tarjetas que se puede hacer es: %i' %tpp)

    pliegospapel=int(input('Dame la cantidad de pliegos de papel albanene: '))
    plumones=int(input('Dame la cantidad de plumones: '))

    Tarjetas(plumones,pliegospapel)
    pass

if __name__=='__main__':
    main()
