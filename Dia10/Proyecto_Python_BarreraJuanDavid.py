#########################
######## Dia 10 #########
#########################

#proyecto 1

# Menú Principal del Simulador de Gasto Diario
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

boleanito= True
while(boleanito):
    if (opcion==1):
        print("=============================================")
        print("        Registrar Nuevo Gasto                ")
        print("=============================================")
        print("Ingrese la información del gasto:")
        montoGasto=float(input("- Monto del gasto: "))
        print("- Categoría (ej. comida, transporte, entretenimiento, otros):")
        categoriaGasto= comida
        print(type(categoriaGasto))
- Descripción (opcional):

Ingrese 'S' para guardar o 'C' para cancelar.
=============================================

