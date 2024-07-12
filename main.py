#imports

from modulo_menu import*
from modulo_ciudades import *
from datos import *
#constantes
RUTA_CIUDADES = "ciudades.json"


# cargar datos
datosCiudad = bajar_datos(RUTA_CIUDADES)


opc = 0

while True:
    menu_principal()
    opc = int(input("Ingrese su opcion: "))
    if opc == 1:
        datos = registrar_ciudad(datosCiudad)
    elif opc == 2:
        datos = editar_ciudad(datosCiudad)
    #elif opc == 3:
        #datos = mostrar_ciudad(datosCiudad)
    elif opc == 4:
        mostar_ciudades(datosCiudad)
    elif opc == 5:
        break
    subir_datos(datosCiudad,RUTA_CIUDADES)
    break

    
