import json
import tabulate
def abrirJSON():
    listaDeGastos=[]
    with open("./datos/datos.json",'r') as openFile:
        listaDeGastos=json.load(openFile)
    return listaDeGastos

def guardarJSON(dic):
    with open("./datos/datos.json",'w') as outFile:
        json.dump(dic,outFile)

import datetime
import tabulate
def hallarFecha():
    hallarFecha=[]
    with open("./datos/datos.json",'r') as openFile:
        hallarFecha=json.load(openFile)
    return hallarFecha

def guardarJSON(dic):
    with open("./datos/datos.json",'w') as outFile:
        json.dump(dic,outFile)




