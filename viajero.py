class Viajero:
    __numv=""
    __dni=""
    __nombre=""
    __apellido=""
    __millasa=""
    
    def __init__(self, num, dni, nombre, apellido, millas):
        self.__numv = num
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasa = millas
        
    def __gt__(self, otro):
       return self.__millasa > otro.__millasa
       
    def __add__(self, otro):
        self.__millasa + otro
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa+otro)
    
    def __radd__(self, otro):
        self.__millasa + otro
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa+otro)

    def __sub__(self, otro):
        self.__millasa - otro
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa-otro)
    
    def __rsub__(self, otro):
        self.__millasa - otro
        return Viajero(self.__numv, self.__dni, self.__nombre, self.__apellido, self.__millasa-otro)
    
    def mostrar(self):
        print('-'*50)
        print('numero de viajero: {}'.format(self.__numv))
        print("dni del viajero: {}".format(self.__dni))
        print("nombre: {}".format(self.__nombre))
        print("apellido: {}".format(self.__apellido))
        print('millas acumaldas del viajero: {}'.format(self.__millasa))
        print('-'*50)
