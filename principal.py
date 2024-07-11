import funciones as fn
trabajadores=["Juan Perez", "Maria Garcia","Carlos Lopes", "Ana Martinez","Pedro Rodriguez", "Laura Hernandez", "Miguel Sanchez", "Isabel Gomez", "Francisco Diaz", "Elenas Fernandez"]
sueldos=[]

while True:

    print("---------Menu---------")
    print("**********************")
    print("1. asignar sueldos aleatorios")
    print("2. clasificar sueldos")
    print("3. ver estadisticas")
    print("4. reporte de sueldos ")
    print("5. salir del programa")

    opc=int(input("ingrese su opcion: "))

    if opc== 1:
        fn.asignar_sueldos(trabajadores,sueldos)         
    elif opc==2:
        fn.clasificar_sueldos(sueldos)
    elif opc==3:
        fn.estadisticas_sueldo(sueldos)
    elif opc==4:
        fn.reporte_sueldo (sueldos)
    elif opc==5:
        print("saliendo")
        print("programa creado por Maria Villarroel")
        break
    

    

    