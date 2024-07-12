def registrar_ciudad(datosCiudad):
    datosCiudad = dict(datosCiudad)
    ciudad = {}
    ciudad["ciudad"] = input("Ingrese el nombre de la ciudad: ")
    ciudad["codigo_postal"] = input("Ingrese el codigo postal: ")
    ciudad["poblacion"] = input("Ingrese la poblacion de la ciudad: ")
    ciudad["Pais"] = input("Ingrese el pais en el que esta la poblacion: ")
    
    datosCiudad["ciudades"].append(ciudad)
    print("ciudad registrada exitosamente!")
        
    return datosCiudad

def editar_ciudad(datosCiudad):
    datosCiudad = dict(datosCiudad)
    ciudad = {}
    buscar_ciudad = input("Ingrese el nombre o el codigo postal de la ciudad: ")
    for ciudad in datosCiudad["ciudades"]:
        if ciudad["codigo_postal"] == buscar_ciudad:
                print("Ciudad encontrada!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_codigo = input("Nuevo codigo postal (Enter para dejar sin cambios): ")
                nuevo_poblacion = input("Nueva poblacion (Enter para dejar sin cambios): ")
                nuevo_pais = input("Nuevo pais (Enter para dejar sin cambios): ")
                if nuevo_nombre:
                    ciudad["ciudad"] = nuevo_nombre
                if nuevo_codigo:
                    ciudad["codigo_postal"] = nuevo_codigo
                if nuevo_poblacion:
                    ciudad["poblacion"] = nuevo_poblacion
                if nuevo_pais:
                    ciudad["Pais"] = nuevo_pais
                print("Ciudad editada con éxito!")
                break
        elif ciudad["ciudad"] == buscar_ciudad:
                print("Ciudad encontrada!")
                nuevo_nombre = input("Nuevo nombre (Enter para dejar sin cambios): ")
                nuevo_codigo = input("Nuevo codigo postal (Enter para dejar sin cambios): ")
                nuevo_poblacion = input("Nueva poblacion (Enter para dejar sin cambios): ")
                nuevo_pais = input("Nuevo pais (Enter para dejar sin cambios): ")
                if nuevo_nombre:
                    ciudad["ciudad"] = nuevo_nombre
                if nuevo_codigo:
                    ciudad["codigo_postal"] = nuevo_codigo
                if nuevo_poblacion:
                    ciudad["poblacion"] = nuevo_poblacion
                if nuevo_pais:
                    ciudad["Pais"] = nuevo_pais
                print("Ciudad editada con éxito!")
                break
        else:
            print("Ciudad no encontrada!")
        return datosCiudad
    
    return datosCiudad

def mostar_ciudades(datosCiudad):
    for i in datosCiudad["ciudades"]:
        print (i)