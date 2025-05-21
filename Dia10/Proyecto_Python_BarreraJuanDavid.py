#########################
######## Dia 10 #########
#########################

#proyecto 1

from funciones import *
from tabulate import tabulate
import datetime
fecha_actual = datetime.date.today()

boleanito= True
while(boleanito):
    listaDeGastos = abrirJSON()
    listaDeGastos=hallarFecha()
    
    # Menú Principal del Simulador de Gasto Diario
    listaDeGastos=abrirJSON()
    print("=============================================")
    print("         Simulador de Gasto Diario           ")
    print("=============================================")
    print("eleccione una opción:")
    print("")
    print("1. Registrar nuevo gasto")
    print("2. Listar gastos")
    print("3. Calcular total de gastos")
    print("4. Generar reporte de gastos")
    print("5. Salir")
    print("=============================================")
    opcion=int(input("que desea hacer?: "))
    if (opcion==1):# 1. Registrar Nuevos Gastos  
        print(" ")
        print(" ")
        print("=============================================")
        print("        Registrar Nuevo Gasto               ")
        print("=============================================")
        print("Ingrese la información del gasto:")
        print(" ")
        fechaFormateada = fecha_actual.strftime("%Y-%m-%d %H:%M:%S") # %Y: año, %m: mes, %d: día, %H: hora, %M: minuto, %S: segund
        
        montoGasto=int(input("- Monto del gasto: "))
        categoriaGasto=str(input("- Categoría (ej. comida, transporte, entretenimiento, otros):"))
        descripcionGasto=str(input("- Descripción (opcional):"))
        nuevoGasto={
            "fecha":fechaFormateada,
            "monto del gasto":montoGasto,
            "categoria":categoriaGasto,
            "Descripción":descripcionGasto
        }
        
        print(" ")
        guardarGasto=str(input("Ingrese 'S' para guardar o 'C' para cancelar."))
        if (guardarGasto=="s"):
            listaDeGastos.append(nuevoGasto)
            guardarJSON(listaDeGastos)
            nuevoGasto={}
            print("")
            print("")

        elif (guardarGasto=="c"):
            print("=============================================")
            print("")
            print("")
        else:
            print("opcion no valida, vuelva a intentar")

              
    
    elif (opcion==2):# 2. Listar gastos
        print("")
        print("")
        print("=============================================")
        print("               Listar Gastos                 ")
        print("=============================================")
        print("Seleccione una opción para filtrar los gastos:")
        print(" ")
        print("1. Ver todos los gastos")
        print("2. Filtrar por categoría")
        print("3. Filtrar por rango de fechas")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionListarGastos=int(input("que desea hacer?"))
        
        if (opcionListarGastos==1):
           print(listaDeGastos)
        elif (opcionListarGastos==2):
            gastoCatComida=[]
            gastoCatTransporte=[]
            gastoCatEntretenimiento=[]
            gastoCatOtros=[]
            for i in range(len(listaDeGastos)):
                if (listaDeGastos[i]["categoria"]=="comida"):
                        gastoCatComida.append(listaDeGastos[i])
                elif (listaDeGastos[i]["categoria"]=="transporte"):
                        gastoCatTransporte.append(listaDeGastos[i])
                elif (listaDeGastos[i]["categoria"]=="entretenimiento"):
                        gastoCatEntretenimiento.append(listaDeGastos[i])
                elif (listaDeGastos[i]["categoria"]=="otros"):
                        gastoCatOtros.append(listaDeGastos[i])
            
            print("comida:")        
            print(gastoCatComida)
            print("")
            print("transporte:")
            print(gastoCatTransporte)
            print("")
            print("entretenimiento:")
            print(gastoCatEntretenimiento)
            print("")
            print("otros:")
            print(gastoCatOtros)
            
        elif (opcionListarGastos==3):
            listasPorFechas = sorted(listaDeGastos, key=lambda x: x["fecha"])
            print(listasPorFechas)
               
        elif (opcionListarGastos==4):
            print("")
    
    elif (opcion==3):# 3. Calcular total de gastos
        print("")
        print("")
        print("=============================================")
        print("        Calcular Total de Gastos             ")      
        print("=============================================")
        print("Seleccione el periodo de cálculo: ")  
        print(" ")  
        print("1. Calcular total diario")
        print("2. Calcular total semanal")
        print("3. Calcular total mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionCalcularGastos=int(input("que desea hacer?"))
        if (opcionCalcularGastos==1):
            print

        elif (opcionCalcularGastos==2):
            print####
        elif(opcionCalcularGastos==3):
            print###
        elif(opcionCalcularGastos==4):
            print("")
    
    elif (opcion==4):# 4. Generar reporte de gastos
        print("")
        print("")
        print("=============================================")
        print("       Generar Reporte de Gastos             ")
        print("=============================================")
        print("Seleccione el tipo de reporte: ")
        print(" ")
        print("1. Reporte diario")
        print("2. Reporte semanal")
        print("3. Reporte mensual")
        print("4. Regresar al menú principal")
        print("=============================================")
        opcionReporteGastos=int(input("que desea hacer?"))
        if (opcionReporteGastos==1):
             print####
        elif (opcionReporteGastos==2):
             print####
        elif(opcionReporteGastos==3):
             print###
        elif(opcionReporteGastos==4):
             print("")
    
    elif (opcion==5):# 5. Salir
            
            salirONo=str(input("¿Desea salir del programa? (S/N): \n"))
            if ((salirONo=="s") or (salirONo=="S")):
                boleanito= False
                print("hasta la proxima")
            elif ((salirONo=="n") or (salirONo=="N")):
                print(" ")
            else:
                print("opcion no valida, vuelva a intentar")
    else:
        print("vualeve a elegir una opcion")


# Desarrollado por Juan David Barrera Torres - T.I. 1.097.101.967
