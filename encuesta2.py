class Encuesta:
    def leeEncuesta():
        print('¿Cuantos alumnos desea registrar?')
        cantidadAlumnos = int(input())
        i = 0
        my_dict = {"Sexo": [], "ID": [], "Carrera": []}
        while i < cantidadAlumnos:
            print('Encuesta a alumnos')
            ide = input('Matricula:')
            sex = input('Sexo (M o F): ')
            carrer = input('Carrera: (‘IE’, ‘ISW’, ‘IC’, LAE’, ‘LPS’, etc.): ')
            my_dict["Sexo"].append(sex)
            my_dict["Carrera"].append(carrer)
            my_dict["ID"].append(ide)
            i = i+1
        return my_dict

    def clasificaAlumnosCategoria(carrera, sexo):
        print("******************")
        print("ie, isw, ic, lae, otros")
        print(carrera)
        print("Mujeres, Hombres")
        print("******************")
        print(sexo)
        print("******************")
        return alumnos

    def despEncuesta(listaAlumnos):
        print('***************')
        print("ID :", listaAlumnos['ID'])
        print("Carrera :", listaAlumnos['Carrera'])
        print("Sexo :", listaAlumnos['Sexo'])

    def clasificaAlumnosCarrera(dicc):
        # se instancia cel como arreglo
        # se define el tamaño de la lista
        ie = 0
        isw = 0
        ic = 0
        lae = 0
        otros = 0

        for val in dicc.values():
            if val.__eq__("IE".upper().lower()):
                ie = ie + 1
            elif val.__eq__("ISW".upper().lower()):
                isw = isw+1
            elif val.__eq__("IC".upper().lower()):
                ic = ic+1
            elif val.__eq__("LAE".upper().lower()):
                lae = lae + 1
            else:
                otros += 1

        listaDatos = [ie, isw, ic, lae, otros]
        return listaDatos

    def despAlumnosCarrera(listaDatos):
        print('IE:', listaDatos[0])
        print('ISW:', listaDatos[1])
        print('IC:', listaDatos[2])
        print('LAE:', listaDatos[3])
        print('Otros:', listaDatos[4])

    def clasificaAlumnosSexo(dicc):
        hombre = 0
        mujer = 0
        for val in dicc.values():
            if val.__eq__('M'.upper().lower()):
                hombre = hombre+1
            elif val.__eq__('F'.upper().lower()):
                mujer = mujer+1
        listaDatos = [hombre, mujer]
        return listaDatos

    def despAlumnosSexo(lista):
        print('Mujeres:', lista[0])
        print('Hombres:', lista[1])


clase = Encuesta
alumnos = clase.leeEncuesta()
sexo = clase.clasificaAlumnosSexo(alumnos)
carrera = clase.clasificaAlumnosCarrera(alumnos)

while True:
    print('********************************')
    print('Seleccione lo que desee hacer: \n')
    print('1) Desplegar Encuesta\n')
    print('2) Imprimir alumnos en general\n')
    print('3) Imprimir alumnos por sexo\n')
    print('4) Imprimir alumnos por carrera\n')
    print('5) Salir\n')
    print('********************************')

    comando = int(input())

    # si se selecciona 1
    if comando == 1:
        clase.despEncuesta(alumnos)
    if comando == 2:
        clase.clasificaAlumnosCategoria(carrera, sexo)
    if comando == 3:
        clase.despAlumnosSexo(sexo)
    if comando == 4:
        clase.despAlumnosCarrera(carrera)
    if comando == 5:
        exit()
