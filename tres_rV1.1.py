import PySimpleGUI as pysg
from time import sleep
import random


TBOTON = (7,2)
JUGADOR1 = "X"
JUGADOR2 = "O"
GANAR = [["-1-","-2-","-3-"],["-1-","-5-","-9-"],
         ["-1-","-4-","-7-"],["-2-","-5-","-8-"],
         ["-3-","-6-","-9-"],["-3-","-5-","-7-"],
         ["-4-","-5-","-6-"],["-7-","-8-","-9-"]]
empate = ["-1-","-2-","-3-",
          "-4-","-5-","-6-",
          "-7-","-8-","-9-"]
contad1 = 0
contad2 = 0
contad3 = 0
contad4 = 0
contad5 = 0
contad6 = 0
contad7 = 0
contad8 = 0

contad1b = 0
contad2b = 0
contad3b = 0
contad4b = 0
contad5b = 0
contad6b = 0
contad7b = 0
contad8b = 0

tiempo = 25
jugador_actual = JUGADOR1
jj1 = []
jj2 = []
jndispo = []
jdispo = ["-1-","-2-","-3-",
          "-4-","-5-","-6-",
          "-7-","-8-","-9-"]
marcadorjj1 = 0
marcadorjj2 = 0
partidas = 10

def cuenta_atras():
    for n in reversed(range(1,16)):
        sleep(1)
        return n

layout = [
        [
        pysg.Button(0, size=(7,4),button_color="black" , key="MJ1"),
        pysg.Button(partidas,size=TBOTON, key="TIME"),
        pysg.Button(0, size=(7,4),button_color="black", key="MCPU")
        ],
        [pysg.Button("", size=TBOTON, button_color="black", key="-1-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-2-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-3-")
        ],
        [pysg.Button("", size=TBOTON, button_color="black", key="-4-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-5-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-6-")
        ],
        [pysg.Button("", size=TBOTON, button_color="black", key="-7-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-8-"),
        pysg.Button("", size=TBOTON, button_color="black", key="-9-")
        ],
        [pysg.Button("Salir", size=TBOTON, key="Salir"),
        pysg.Button("Reiniciar", size=TBOTON, key="Reiniciar")]]

ventana = pysg.Window("3-Raya BY M0rz4n", layout, margins=(70, 70))


def numero_random():
    numero = "-{}-".format(random.randrange(1,10))
    return numero


def bestmy(y):
    global contad1b
    global contad2b
    global contad3b
    global contad4b
    global contad5b
    global contad6b
    global contad7b
    global contad8b
    if y == "-1-":
        contad1b += 1
        contad2b += 1
        contad3b += 1
    elif y == "-2-":
        contad1b += 1
        contad3b += 1
    elif y == "-3-":
        contad1b += 1
        contad5b += 1
        contad6b += 1
    elif y == "-4-":
        contad3b += 1
        contad7b += 1
    elif y == "-5-":
        contad2b += 1
        contad4b += 1
        contad6b += 1
        contad7b += 1
    elif y == "-6-":
        contad5b += 1
        contad7b += 1
    elif y == "-7-":
        contad3b += 1
        contad6b += 1
        contad8b += 1
    elif y == "-8-":
        contad4b += 1
        contad8b += 1
    elif y == "-9-":
        contad2b += 1
        contad5b += 1
        contad8b += 1
    
def best2my():
    global contad1b
    global contad2b
    global contad3b
    global contad4b
    global contad5b
    global contad6b
    global contad7b
    global contad8b
    besta= []
    if contad1b == 2:
        besta.append(GANAR[0])
        contad1b = 3
    if contad2b == 2:
        besta.append(GANAR[1])
        contad2b = 3
    if contad3b == 2:
        besta.append(GANAR[2])
        contad3b = 3
    if contad4b == 2:
        besta.append(GANAR[3])
        contad4b = 3
    if contad5b == 2:
        besta.append(GANAR[4])
        contad5b = 3
    if contad6b == 2:
        besta.append(GANAR[5])
        contad6b = 3
    if contad7b == 2:
        besta.append(GANAR[6])
        contad7b = 3
    if contad8b == 2:
        besta.append(GANAR[7])
        contad8b = 3

    return besta


def best(y):
    global contad1
    global contad2
    global contad3
    global contad4
    global contad5
    global contad6
    global contad7
    global contad8
    if y == "-1-":
        contad1 += 1
        contad2 += 1
        contad3 += 1
    elif y == "-2-":
        contad1 += 1
        contad3 += 1
    elif y == "-3-":
        contad1 += 1
        contad5 += 1
        contad6 += 1
    elif y == "-4-":
        contad3 += 1
        contad7 += 1
    elif y == "-5-":
        contad2 += 1
        contad4 += 1
        contad6 += 1
        contad7 += 1
    elif y == "-6-":
        contad5 += 1
        contad7 += 1
    elif y == "-7-":
        contad3 += 1
        contad6 += 1
        contad8 += 1
    elif y == "-8-":
        contad4 += 1
        contad8 += 1
    elif y == "-9-":
        contad2 += 1
        contad5 += 1
        contad8 += 1
    
def best2():
    global contad1
    global contad2
    global contad3
    global contad4
    global contad5
    global contad6
    global contad7
    global contad8
    besta= []
    if contad1 == 2:
        besta.append(GANAR[0])
        contad1 = 3
    if contad2 == 2:
        besta.append(GANAR[1])
        contad2 = 3
    if contad3 == 2:
        besta.append(GANAR[2])
        contad3 = 3
    if contad4 == 2:
        besta.append(GANAR[3])
        contad4 = 3
    if contad5 == 2:
        besta.append(GANAR[4])
        contad5 = 3
    if contad6 == 2:
        besta.append(GANAR[5])
        contad6 = 3
    if contad7 == 2:
        besta.append(GANAR[6])
        contad7 = 3
    if contad8 == 2:
        besta.append(GANAR[7])
        contad8 = 3

    return besta


def mi_mejor(jou):
    global jj2
    global jdispo
    if len(jou) != 0:
        for fo in jou:
            for j in jj2:
                for f in fo:
                    if j != f:
                        for io in jdispo:
                            if f == io:
                                return f
    
    else:
        return None
    
    
def final():
    global jdispo
    global GANAR
    global jndispo
    global jj1
    global jj2
    ga = 0
    jugan = []
    nga = best2my()
    ghna = best2()
    
    prueba = mi_mejor(nga)
    if prueba != None:
        return prueba
    
    if ghna == [] and len(jdispo) == [] :
        reiniciar()
    
    if ghna != []:
        for uv in ghna:
            for iv in uv:
                jugan.append(iv)
            for g in jugan:
                for jsa in jdispo:
                    if g == jsa:
                        return g
    if ghna == [] and jdispo != []:
        return random.choice(jdispo)

    
    
def enemigo(jj1):
    global GANAR
    global jndispo
    global jj2
    global partidas
    global jdispo
    jndispo_contador = 0
    jugada = []
    jdispospo = jdispo.copy()
    ciclote = 0

    contador = 0
    contador2 = 0
    numero = numero_random()

        
        
    if len(jdispo) != 0 and len(jj1) < 2:
        if len(jj1 + jj2) == len(empate):
            reiniciar()
        elif len(jndispo) == 0:
            return random.choice(jdispo)
        for n in jj1:
            if numero != n:
                contador += 1
                if len(jj1) == contador:
                    contador = 0
                    if len(jj2) == 0:
                        jndispo.append(numero)
                        jndispo = sorted(jndispo)
                        return numero
                    for x in jj2:
                        if numero != x:
                            contador2 += 1                            
                            if contador2 == len(jj2):                           
                                jndispo.append(numero)
                                jndispo = sorted(jndispo)
                                return numero
                            elif len(jj2) == 0:
                                jndispo.append(numero)
                                jndispo = sorted(jndispo)
                                return numero
    
    return final()
    
                        
                        
        
        
                        

        



def estado(jj):
    global GANAR
    global jndispo
    global empate
    global contad1b
    global contad2b
    global contad3b
    global contad4b
    global contad5b
    global contad6b
    global contad7b
    global contad8b
    estat = 0
    marcador = False
    win = 3
    
    for x in GANAR:
        for x2 in x:
            for y in jj:
                if y == x2:
                    estat += 1
                    if estat == win:
                        marcador = True
                        estat = 0
                        return marcador
        estat = 0
    if sorted(empate) == sorted(jndispo):
        marcador = None
        return marcador
    elif contad1b == 3:
        marcador = True
    elif contad2b == 3:
        marcador = True
    elif contad3b == 3:
        marcador = True
    elif contad4b == 3:
        marcador = True
    elif contad5b == 3:
        marcador = True
    elif contad6b == 3:
        marcador = True
    elif contad7b == 3:
        marcador = True
    elif contad8b == 3:
        marcador = True
    else:
        return marcador
        


def ganador():
    global jugador_actual
    global JUGADOR1
    global JUGADOR2
    global GANAR
    global jj1
    global jj2
    contador = 0
    neutras = []
    if jugador_actual == JUGADOR1:
        for a in jj1:
            for b in jj2:
                if a != b:
                    for c in empate:
                        if b != c:
                            ventana.Element(key= c).Update(text= jugador_actual)
    elif jugador_actual == JUGADOR2:
        for a in jj2:
            for b in jj1:
                if a != b:
                    for c in empate:
                        if b != c:
                            ventana.Element(key= c).Update(text= jugador_actual)
    
#    ventana.Element(key="-2-").Update(text= jugador_actual)
#    ventana.Element(key="-3-").Update(text= jugador_actual)
#    ventana.Element(key="-4-").Update(text= jugador_actual)
#    ventana.Element(key="-5-").Update(text= jugador_actual)
#    ventana.Element(key="-6-").Update(text= jugador_actual)
#    ventana.Element(key="-7-").Update(text= jugador_actual)
#    ventana.Element(key="-8-").Update(text= jugador_actual)
#    ventana.Element(key="-9-").Update(text= jugador_actual)
#    return True

def subir_marcador(j):
    global jugador_actual
    if jugador_actual == JUGADOR1:
        jugador_actual = JUGADOR2
    else:
        jugador_actual = JUGADOR1
    j += 1
    return j

def cuenta_atras():
    global tiempo
    for n in reversed(range(tiempo)):
        sleep(1)
        tiempo -= 1
        return tiempo

def reiniciar():
    global JUGADOR1
    global contad1
    global contad2
    global contad3
    global contad4
    global contad5
    global contad6
    global contad7
    global contad8
    global contad1b
    global contad2b
    global contad3b
    global contad4b
    global contad5b
    global contad6b
    global contad7b
    global contad8b
    global jdispo
    global jj1
    global jj2
    global jndispo
    global jugador_actual
    #ventana.Element(key="MJ1").Update(text= ">")
    ventana.Element(key="TIME").Update(text= partidas)
    #ventana.Element(key="MCPU").Update(text= "<")
    ventana.Element(key="-1-").Update(text= "")
    ventana.Element(key="-2-").Update(text= "")
    ventana.Element(key="-3-").Update(text= "")
    ventana.Element(key="-4-").Update(text= "")
    ventana.Element(key="-5-").Update(text= "")
    ventana.Element(key="-6-").Update(text= "")
    ventana.Element(key="-7-").Update(text= "")
    ventana.Element(key="-8-").Update(text= "")
    ventana.Element(key="-9-").Update(text= "")
    jj1 = []
    jj2 = []
    jndispo = []
    contad1 = 0
    contad2 = 0
    contad3 = 0
    contad4 = 0
    contad5 = 0
    contad6 = 0
    contad7 = 0
    contad8 = 0
    contad1b = 0
    contad2b = 0
    contad3b = 0
    contad4b = 0
    contad5b = 0
    contad6b = 0
    contad7b = 0
    contad8b = 0
    tiempo = 25
    jdispo = ["-1-","-2-","-3-",
          "-4-","-5-","-6-",
          "-7-","-8-","-9-"]
def main():
    global JUGADOR1
    global JUGADOR2
    global jugador_actual
    global jj1
    global jj2
    global jndispo
    global marcadorjj1
    global marcadorjj2
    global partidas
    global jdispo
    game = True
    
    
    while True:
        eventos, valores = ventana.read()
        
        if eventos == pysg.WIN_CLOSED or eventos == "Salir" or partidas == 0:
            pysg.Popup("Adios Buda")
            break
        if ventana.Element(eventos).ButtonText == "" and game == True:
            if jugador_actual == JUGADOR1:
                ventana.Element(eventos).Update(text= jugador_actual)
                jj1.append(ventana.Element(eventos).Key)
                jndispo.append(eventos)
                best(eventos)
                jdispo.remove(eventos)
                jj1 = sorted(jj1)
                ronda = estado(jj1)
                jugador_actual = JUGADOR2
                
                if ronda == True:
                    jugador_actual = JUGADOR1    
                    ganador()
                    marcadorjj1 = subir_marcador(marcadorjj1)
                    partidas -= 1
                    jj1 = []
                    jj2 = []
                    jndispo = []
                    ventana.Element(key="MJ1").Update(marcadorjj1)
                    ventana.Element(key="MCPU").Update(marcadorjj2)
                    ventana.Element(key="TIME").Update(partidas)
                    sleep(1)
                    reiniciar()
                    jugador_actual = JUGADOR2
                
                    
        if jugador_actual == JUGADOR2:
            cpu = enemigo(jj1)
            if cpu == None:
                pass
            else:
                bestmy(cpu)
                ventana.Element(key=cpu).Update(text= JUGADOR2)
                jj2.append(ventana.Element(cpu).Key)


                jdispo.remove(cpu)
                jj2 = sorted(jj2)
                ronda2 = estado(jj2)
                jugador_actual = JUGADOR1
                if ronda2 == True:
                    jugador_actual = JUGADOR2
                    ganador()
                    marcadorjj2 = subir_marcador(marcadorjj2)
                    partidas -= 1
                    jj1 = []
                    jj2 = []
                    jndispo = []
                    jugador_actual = JUGADOR1
                    ventana.Element(key="MJ1").Update(marcadorjj1)
                    ventana.Element(key="MCPU").Update(marcadorjj2)
                    ventana.Element(key="TIME").Update(partidas)
                jugador_actual = JUGADOR1
                        

                
        if eventos == "Reiniciar":
            reiniciar()
        

if __name__ == "__main__":
    main()