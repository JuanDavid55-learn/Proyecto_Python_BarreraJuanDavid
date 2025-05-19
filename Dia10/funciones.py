import json

def abrirJSON():
    listaDeGastos=[]
    with open("./datos.json",'r') as openFile:
        listaDeGastos=json.load(openFile)
    return listaDeGastos

def guardarJSON(dic):
    with open("./datos.json",'w') as outFile:
        json.dump(dic,outFile)