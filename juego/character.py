class character:

    def __init__(self,nombre,fuerza,inteligencia,defensa,vida):#constructor
        self.nombre = nombre #nombre: (str) Nombre del personaje.
        self.fuerza = fuerza #fuerza: (int) cantidad de fuerza.
        self.inteligencia = inteligencia  #inteligencia: (int) cantidad inteligencia.
        self.defensa = defensa  #defensa: (int) cantidad de defensa.
        self.vida = vida  #vida:(int) total vida.


    def atributos(self):#impresion de atributos
        print(f'{self.nombre}')
        print(f'Fuerza : {self.fuerza}')
        print(f'Inteligencia : {self.inteligencia}')
        print(f'Defensa : {self.defensa}')
        print(f'Vida : {self.vida}')

    def subir_nivel(self,fuerza,inteligencia,defensa,vida):
        #sube el nivel del personaje aumentando sus atributos.
        #los valores ingresados se sumaran a los valores actuales del personaje.
        self.fuerza += fuerza 
        self.inteligencia += inteligencia
        self.defensa += defensa
        self.vida += vida
        print(f'{self.nombre}')
        print('HA AVANZADO DE NIVEL')
        print('Nuevos atributos')
        self.atributos()

        

    def esta_vivo(self): #comprobar si el personaje esta vivo.
        return self.vida > 0 #True = vivo , False = Morraquiado
    
    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto!')

    def daño(self,enemigo):
        return max(0,self.fuerza - enemigo.defensa)
    
    def atacar(self,enemigo): # realiza un ataque al enemigo y muestra el resultado
        daño = self.daño(enemigo)
        enemigo.vida= enemigo.vida - daño
        print(f'el ataque de {self.nombre} ha sido de {daño} sobre {enemigo.nombre}')
        if enemigo.esta_vivo():
            print(f'la vida de {enemigo.nombre} es de {enemigo.vida} tras el ataque.')
        else:
            enemigo.morir()


class war(character):

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma


    def cambiar_arma(self):
        opcion= int(input('elige (1)para espada, (2) para dos-manos.'))
        if opcion == 1:
            self.arma = 2
        elif opcion == 2:
            self.arma = 3
        else:
            print('verifica tu respuesta')

    def atributos(self):
        super().atributos()
        print('arma',self.arma)

    def daño(self,enemigo):
        return self.fuerza + self.arma - enemigo.defensa
    

    
class mago(character):


    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def cambiar_arma(self):
        opcion= int(input('elige (1)para libro, (2) para baston.'))
        if opcion == 1:
            self.arma = 2
        elif opcion == 2:
            self.arma = 3
        else:
            print('verifica tu respuesta')

    def atributos(self):
        super().atributos()
        print('arma',self.arma)

    def daño(self,enemigo):
        return self.inteligencia + self.arma - enemigo.defensa
    

def combate(p1,p2):
    turno = 0
    while p1.esta_vivo() and p2.esta_vivo():
        print(f'\nTurno : {turno}')
        print(f'\nTurno de {p1.nombre} :')
        
        p1.atacar(p2)
        print(f'\nTurno de {p2.nombre} :')
        p2.atacar(p1)
        turno += 1
    if p1.vida > 0:
        print(f'\n{p1.nombre} ha vencido')
    elif p2.vida >0:
        print(f'\n{p2.nombre} ha vencido')
    else:
        print('\nEMPATE')

    
