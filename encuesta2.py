class Encuesta:
    def leeEncuesta():
        print('¿Cuantos alumnos desea registrar?')
        cantidadAlumnos = int(input())
        i = 0
        diccionario = dict()
        while i < cantidadAlumnos:

            print('Encuesta a alumnos')
            ide = input('Matricula:')
            sex = input('Sexo (M o F): ')
            carrer = input('Carrera: (‘IE’, ‘ISW’, ‘IC’, LAE’, ‘LPS’, etc.))')
            diccionario.fromkeys('sexo', [sex])
            diccionario.fromkeys('id', [ide])
            diccionario.fromkeys('carrera', [carrer])
            diccionario.fromkeys('carrera', [carrer])
            i = i+1
        return diccionario

    def despEncuesta(dicc):
        print('***************')
        print('      ID      |      Sexo      |     Carrera')
        print(dicc.items())

    def clasificaAlumnosCategoria(dicc):
        # se instancia cel como arreglo
        alumno = list(dicc.values())
        # se define el tamaño de la lista
        i = 0
        hombre = 0
        mujer = 0
        ie = 0
        isw = 0
        ic = 0
        lae = 0
        otros = 0

        for i in alumno:
            if alumno.get(i) == 'M':
                hombre = hombre+1
            elif alumno.get(i) == 'F':
                mujer = mujer+1
            else:
                if alumno.get(i) == 'IE':
                    ie = ie+1
                elif alumno.get(i) == 'ISW':
                    isw = isw+1
                elif alumno.get(i) == 'IC':
                    ic = ic+1
                elif alumno.get(i) == 'LAE':
                    lae = lae+1
                else:
                    otros = otros+1

        print('Hombres:', hombre)
        print('Mujeres:', mujer)
        print('IE:', ie)
        print('ISW:', isw)
        print('IC:', ic)
        print('LAE:', lae)
        print('Otros:', otros)

    def despCatAlumno(dicc):
        i = 0
        ide = input('Matricula: ID')
        print(dicc[ide])

    def clasificaAlumnosCategoria(alumnos):
        # se instancia cel como arreglo
        alumno = alumnos
        # se define el tamaño de la lista
        tamañoLista = len(alumno)
        i = 0
        calificaciones = {}
        for i in alumno:
            ide = input('Calificar alumno: ')
            dicc = dict.fromkeys(llaves, 5)

        return calificaciones


clase = Encuesta
alumnos = clase.leeEncuesta()

while True:
    print('********************************')
    print('Seleccione lo que desee hacer: \n')
    print('1) Desplegar Encuesta\n')
    print('2) Imprimir alumnos por categoria\n')
    print('3) Filtrar Alumnos\n')
    print('4) Calificar Alumnos\n')
    print('5) Salir\n')
    print('********************************')

    comando = int(input())

    # si se selecciona 1
    if comando == 1:
        clase.despEncuesta(alumnos)
    if comando == 2:
        clase.clasificaAlumnosCategoria(alumnos)
    if comando == 3:
        clase.despCatAlumno(alumnos)
    if comando == 4:
        clase.clasificaAlumnosCategoria(alumnos)
    if comando == 5:
        exit()
