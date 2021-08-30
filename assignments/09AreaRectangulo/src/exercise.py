
def main():
    #escribe tu código abajo de esta línea
    def area(base,altura):
        área=(base*altura)
        print('El área del rectángulo es: %0.2f' %área)

    b=float(input('Dame la base: '))
    a=float(input('Dame la altura: '))
    area(b,a)
    pass

if __name__=='__main__':
    main()
