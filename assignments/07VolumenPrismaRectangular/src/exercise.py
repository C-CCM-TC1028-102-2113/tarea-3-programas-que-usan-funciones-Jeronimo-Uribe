def volumen(área,profundidad):
        v=área*profundidad
        print('El volumen del prisma es: %0.2f' %v)

def área(b,a):
        a=(b*a)
        volumen(a,p) ##Estás utilizando una variable que no existe en este contexto.
def main():
    #escribe tu código abajo de esta línea
    
    base=float(input('Dame la base: '))
    altura=float(input('Dame la altura: '))
    p=float(input('Dame la profundidad: ')) #p solo existe en el contexto de la función main

    área(base,altura)
    pass

if __name__=='__main__':
    main()
