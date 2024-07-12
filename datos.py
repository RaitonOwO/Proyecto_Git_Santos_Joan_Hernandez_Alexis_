import json

def bajar_datos(archivo):
    datos = {}
    with open (archivo,"r") as file:
        datos = json.load(file)
        return datos
    
def subir_datos(datos,archivo):
    datos = dict(datos)
    base_datos = json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(base_datos)
    file.close