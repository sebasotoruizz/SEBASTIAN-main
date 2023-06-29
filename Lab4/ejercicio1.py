#Ejercicio 1

Trabajadores = [["Juan",[700000,650000,690000],["María",[681000,710000,590000]],["Pedro",[590000,635000,705000]]]]

#A) 
def prom_sueldo(sueldos):
    cant_sueldos = sum(sueldos)
    resultado = cant_sueldos/len(sueldos)
    return round(resultado)
#B)
def sueldo_alto()