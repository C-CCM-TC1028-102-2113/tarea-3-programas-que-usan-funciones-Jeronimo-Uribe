def es_bisiesto(a):
    if a % 4 == 0:
        print('True')
    elif a % 400 == 0:
        print('True')
    elif a % 100 == 0:
        print('False')
    else:
        print('False')

def main():
    #escribe tu código abajo de esta línea
    
    año=2020

    es_bisiesto(año) 
    pass

if __name__=='__main__':
    main()
