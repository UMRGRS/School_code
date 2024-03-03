class PersonajeMortalKombat():
    def __init__(self, nombre, velocidad, fuerza, agilidad, resistencia, poderEspecial):
        self.nombre = nombre
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.resistencia = resistencia
        self.poderEspecial = poderEspecial
        self.next = None
    def __repr__(self):
        return(f'Nombre: {self.nombre}, Velocidad: {self.velocidad}, Fuerza: {self.fuerza}, Agilidad: {self.agilidad}, Resistencia: {self.resistencia}, Poder especial: {self.poderEspecial} \n')
    def __str__(self):
        return(f'Nombre: {self.nombre}, Velocidad: {self.velocidad}, Fuerza: {self.fuerza}, Agilidad: {self.agilidad}, Resistencia: {self.resistencia}, Poder especial: {self.poderEspecial} \n')

pr1 = PersonajeMortalKombat("Scorpion", 85, 55, 75, 45, "Spear Slam")
pr2 = PersonajeMortalKombat("Sub-Zero", 40, 85, 45, 85, "Frostbite Fury")
pr3 = PersonajeMortalKombat("Liu Kang", 75, 50, 80, 55, "Dragon Kick")
pr4 = PersonajeMortalKombat("Raiden", 90, 60, 70, 80, "Thunderstorm Asault")
pr5 = PersonajeMortalKombat("Sonya Blade", 60, 50, 75, 50, "Sonic Pulse")
pr6 = PersonajeMortalKombat("Johnny Cage", 80, 55, 80, 50, "Groin Stricke")
pr7 = PersonajeMortalKombat("Kitana", 85, 50, 75, 55, "Fan Blade Whirlwind")
pr8 = PersonajeMortalKombat("Kano", 55, 80, 75, 50, "Laser Eye Beam")
pr9 = PersonajeMortalKombat("Jax", 50, 85, 50, 80, "Sonic Wave Punch")
pr10 =PersonajeMortalKombat("Mileena", 90, 55, 80, 50, "Tarkatan Bite")
pr11 =PersonajeMortalKombat("Baraka", 50, 85, 50, 80, "Blade Barrage")
pr12 =PersonajeMortalKombat("Shang Tsung", 55, 55, 75, 55, "Shape-shifter's Gambit")
pr13 =PersonajeMortalKombat("Shao Khan", 25, 90, 25, 90, "Kahn's Wrath")
pr14 =PersonajeMortalKombat("Kung Lao", 80, 55, 80, 55, "Razor Hat Spin")
pr15 =PersonajeMortalKombat("Reptile", 90, 55, 80, 50, "Acid Spid")
pr16 =PersonajeMortalKombat("Goro", 20, 90, 20, 90, "Double Fist Smash")
pr17 =PersonajeMortalKombat("Quan Chi", 55, 30, 55, 50, "Dark Sorcery")
pr18 =PersonajeMortalKombat("Cyrax", 85, 50, 75, 50, "Net Boom")
pr19 =PersonajeMortalKombat("Smoke", 85, 50, 75, 50, "Teleportation Asault")
pr20 =PersonajeMortalKombat("Noob Saibot", 90, 85, 90, 30, "Shadow Clone Onslaught")
pr21 =PersonajeMortalKombat("Sindel", 80, 50, 75, 50, "Sonic Scream")
pr22 =PersonajeMortalKombat("Nightwolf", 90, 55, 80, 55, "Spirit Arrow Barrage")
pr23 =PersonajeMortalKombat("Kabal", 85, 55, 80, 50, "Rapid Blade Assault")
pr24 =PersonajeMortalKombat("Shinnok", 55, 90, 50, 85, "Soul Theft")
pr25 =PersonajeMortalKombat("Fujin", 90, 50, 75, 50, "Wind Blade Clone")
pr26 =PersonajeMortalKombat("Kotal Kahn", 25, 90, 25, 90, "Solar Beam")
pr27 =PersonajeMortalKombat("Cassie Cage", 90, 50, 75, 50, "Gatling Gun kick")
pr28 =PersonajeMortalKombat("D'Vorah", 90, 50, 75, 50, "Deadly Swaem Asault")
pr29 =PersonajeMortalKombat("Erron Black", 90, 90, 90, 55, "Precision Marksman")
pr30 =PersonajeMortalKombat("Jacqui Bringgs", 90, 50, 75, 50, "Bionic Power Slam")

pr1.next = pr2
pr2.next = pr3
pr3.next = pr4
pr4.next = pr5
pr5.next = pr6
pr6.next = pr7
pr7.next = pr8
pr8.next = pr9
pr9.next = pr10
pr10.next = pr11
pr11.next = pr12
pr12.next = pr13
pr13.next = pr14
pr14.next = pr15
pr15.next = pr16
pr16.next = pr17
pr17.next = pr18
pr18.next = pr19
pr19.next = pr20
pr20.next = pr21
pr21.next = pr22
pr22.next = pr23
pr23.next = pr24
pr24.next = pr25
pr25.next = pr26
pr26.next = pr27
pr27.next = pr28
pr28.next = pr29
pr29.next = pr30

def FindVel(start):
    minCV = []
    maxCV = []
    minVel = start.velocidad
    maxVel = start.velocidad
    while(start):
        if(start.velocidad > maxVel):
            maxVel = start.velocidad
            maxCV.clear()
            maxCV.append(start)
        elif(start.velocidad == maxVel):
            maxCV.append(start)
        if(start.velocidad < minVel):
            minVel = start.velocidad
            minCV.clear()
            minCV.append(start)
        elif(start.velocidad == minVel):
            minCV.append(start)
        start = start.next
    print("Personajes con mayor velocidad")
    print(maxCV)
    print("Personajes con menor velocidad")
    print(minCV)

def FindStr(start):
    minCF = []
    maxCF = []
    minStr = start.fuerza
    maxStr = start.fuerza
    while(start):
        if(start.fuerza > maxStr):
            maxStr = start.fuerza
            maxCF.clear()
            maxCF.append(start)
        elif(start.fuerza == maxStr):
            maxCF.append(start)
        if(start.fuerza < minStr):
            minStr = start.fuerza
            minCF.clear()
            minCF.append(start)
        elif(start.fuerza == minStr):
            minCF.append(start)
        start = start.next
    print("Personajes con mayor fuerza")
    print(maxCF)
    print("Personajes con menor fuerza")
    print(minCF)

def FindAgi(start):
    maxCA = []
    minCA = []
    maxAgi = start.agilidad
    minAgi = start.agilidad
    while(start):
        if(start.agilidad > maxAgi):
            maxAgi = start.agilidad
            maxCA.clear()
            maxCA.append(start)
        elif(start.agilidad == maxAgi):
            maxCA.append(start)
        if(start.agilidad < minAgi):
            minAgi = start.agilidad
            minCA.clear()
            minCA.append(start)
        elif(start.agilidad == minAgi):
            minCA.append(start)
        start = start.next
    print("Personajes con mayor agilidad")
    print(maxCA)
    print("Personajes con menor agilidad")
    print(minCA)

def FindRes(start):
    maxCR = []
    minCR = []
    maxRes = start.resistencia
    minRes = start.resistencia
    while(start):
        if(start.resistencia > maxRes):
            maxRes = start.resistencia
            maxCR.clear()
            maxCR.append(start)
        elif(start.resistencia == maxRes):
            maxCR.append(start)
        if(start.resistencia < minRes):
            minRes = start.resistencia
            minCR.clear()
            minCR.append(start)
        elif(start.resistencia == minRes):
            minCR.append(start)
        start = start.next
    print("Personajes con mayor resistencia")
    print(maxCR)
    print("Personajes con menor resistencia")
    print(minCR)

def CompleteList(start):
    print("Lista completa")
    while(start):
        print(start)
        start = start.next
        
def SortAlphabetically(start):
    lisToPrint = []
    while(start):
        lisToPrint.insert(0,{"Nombre":start.nombre, "Poder especial": start.poderEspecial})
        start = start.next
    lisToPrint.sort(key=lambda x: x["Poder especial"])
    print("Poderes ordenados alfabéticamente")
    for item in lisToPrint:
        print(item)

def FavoriteChar(start, character):
    while(start):
        if(start.nombre == character):
            print("Personaje favorito owo \n")
            return(start)
        start = start.next
    return("No se encontró tu personaje favorito :c")
    
FindVel(pr1)
print("----------------------------------")
FindStr(pr1)
print("----------------------------------")
FindAgi(pr1)
print("----------------------------------")
FindRes(pr1)
print("----------------------------------")
SortAlphabetically(pr1)
print("----------------------------------")
print(FavoriteChar(pr1, "Shinnok"))
print("----------------------------------")
CompleteList(pr1)