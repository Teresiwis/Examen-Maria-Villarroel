import statistics
import random
import csv

def asignar_sueldos(trabajadores, sueldos):
    for i in trabajadores:
        sueldo=random.randint(300000,2500000)
        sueldos.append({
            i:sueldo
        })
    print(sueldos)
    return
def clasificar_sueldos(sueldos):
    if not sueldos:
        print("debe asignar sueldos")
    else:
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                if sueldo <800000:
                    print(f"el trabajador{trabajador} tiene como sueldo{sueldo}, el cual es menor a 800000")
                if sueldo>800000 and sueldo <2000000:
                    print(f"el trabajador {trabajador} tiene como sueldo {sueldo}, el cual esta entre el rango mayor a 800000 y menor a 2000000")
                if sueldo <2000000:
                    print(f"el trabajador{trabajador}, tiene un sueldo{sueldo}, el cual es mayor a 2000000")
    return
def estadisticas_sueldo(sueldos):
    if not sueldos:
        print("primero debe entregar sueldos")
        return
    else:
        lista=[]
        for diccionario in sueldos:
            for trabajador, sueldo in diccionario.items():
                lista.append(sueldo)
            menor=min(lista)
            mayor=max(lista)
            promedio=sum(lista)/ len(lista)
            media_geometrica=statistics.geometric_mean(lista)

            print("menor sueldo", menor)
            print("mayor sueldo", mayor)
            print("promedio sueldo", promedio)
            print("media geometrica", media_geometrica)
            return
def reporte_sueldo(sueldos):
    if not sueldos:
        print("primero debe entregar sueldos")
        return
    else:
        with open ("reporte_sueldos.csv","w",newline="") as archivo:
            escritor=csv.writer(archivo)
            escritor.writerow(["Nombre empleado", "sueldo base", "descuento salud", "descuento afp", "sueldo liquido"])
            for diccionario in sueldos:
                for trabajador, sueldo in diccionario.items():
                    descuento_salud=sueldo*0.07
                    descuento_afp=sueldo*0.12
                    liquido=sueldo-descuento_salud-descuento_afp
                    escritor.writerow([trabajador, sueldo, descuento_afp, descuento_salud, liquido, ""])
        print("los sueldos se han impreso satisfactoriamente")
        return
