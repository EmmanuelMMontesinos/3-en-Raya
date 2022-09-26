
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
jugador_actual = JUGADOR1
jj1 = []
jj2 = ["w"]
jndispo = []


layout = [[pysg.Button("", size=TBOTON, key="-1-"),
           pysg.Button("", size=TBOTON, key="-2-"),
           pysg.Button("", size=TBOTON, key="-3-")
           ],
          [pysg.Button("", size=TBOTON, key="-4-"),
           pysg.Button("", size=TBOTON, key="-5-"),
           pysg.Button("", size=TBOTON, key="-6-")
           ],
          [pysg.Button("", size=TBOTON, key="-7-"),
           pysg.Button("", size=TBOTON, key="-8-"),
           pysg.Button("", size=TBOTON, key="-9-")
           ],
          [pysg.Button("Salir", size=TBOTON, key="Salir"),
           pysg.Button("Reiniciar", size=TBOTON, key="Reiniciar")]]

ventana = pysg.Window("Demo", layout, margins=(100, 100))

def numero_random():
    numero = "-{}-".format(random.randrange(1,10))
    return numero


def enemigo(jj1):
    global GANAR
    global jndispo
    global jj2
    jndispo_contador = 0
    jugada = ""
    
    while True:
        contador = 0
        contador2 = 0
        numero = numero_random()
        for n in jj1:
            if numero != n:
                contador += 1
                if len(jj1) == contador:
                    contador = 0
                    for x in jj2:
                        if numero != x:
                            contador2 += 1                            
                            if contador2 == len(jj2):                           
                                jndispo.append(numero)
                                jndispo = sorted(jndispo)
                                return numero
                
            
    


def estado(jj):
    global GANAR
    global jndispo
    global empate
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
    if empate == jndispo:
        marcador = None
        return marcador
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
    elif jugador_actual == JUGADOR1:
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


def reiniciar():
    global JUGADOR1
    global jj1
    global jj2
    global jndispo
    global jugador_actual
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
    jj2 = ["W"]
    jndispo = []
    jugador_actual = JUGADOR1
    

def main():
    global JUGADOR1
    global JUGADOR2
    global jugador_actual
    global jj1
    global jj2
    global jndispo
    game = True
    
    
    while True:
        eventos, valores = ventana.read()
        if eventos == pysg.WIN_CLOSED or eventos == "Salir":
            break
        if ventana.Element(eventos).ButtonText == "" and game == True:
            if jugador_actual == JUGADOR1:
                ventana.Element(eventos).Update(text= jugador_actual)
                jj1.append(ventana.Element(eventos).Key)
                jndispo.append(eventos)
                jj1 = sorted(jj1)
                ronda = estado(jj1)
                jugador_actual = JUGADOR2
                if ronda == True:
                    jugador_actual = JUGADOR1
                    ganador()
                    jj1 = []
                    jj2 = ["w"]
                    jndispo = []
                elif ronda == None:
                    ventana.refresh()
                    jj1 = []
                    jj2 = []
                    jndispo = []
                elif jugador_actual == JUGADOR2:
                    cpu = enemigo(jj1)
                    ventana.Element(key=cpu).Update(text= JUGADOR2)
                    jj2.append(ventana.Element(cpu).Key)
                    jj2 = sorted(jj2)
                    ronda2 = estado(jj2)
                    jugador_actual = JUGADOR1
                    if ronda2 == True:
                        jugador_actual = JUGADOR2
                        ganador()
                        jj1 = []
                        jj2 = ["w"]
                        jugador_actual = "$"

                
        if eventos == "Reiniciar":
            reiniciar()

if __name__ == "__main__":
    main()