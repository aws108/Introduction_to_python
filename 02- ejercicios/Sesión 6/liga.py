#!/usr/bin/python
# -*- coding: utf-8 -*-

resultats_lliga = {}
resultats_lliga3 = {} 
equiposPuntos={}


def obtenerNumClub(num):

	num = int(num)-1
	numero = 0

	for club in resultats_lliga:
		if numero == num:
			return club
		numero = numero + 1
		
              
def insertarEquiposPuntos(golesLocal,golesContra,local,contrario):
       if golesLocal < golesContra:
              equiposPuntos[contrario] += 3
       elif golesLocal > golesContra:
              equiposPuntos[local] += 3
       elif golesLocal == golesContra:
              equiposPuntos[local] += 1
              equiposPuntos[contrario] += 1

e = 1
while e <= 3:
      #Menú
      print "\t MENU LIGA: \n "
      print "1 - Registrar Equipos para nueva Temporada \n"
      print "2 - Crear nueva liga\n"
      print "3 - Introducir datos de un partido\n"
      print "4 - Descartar la entrada de datos de un partido \n"
      print "5 - Guardar los datos obtenidos en un txt \n"
      print "6 - Cargar los datos de la liga desde archivo \n"
      print "7 - Mostrar los resultados de todos los partidos \n"
      print "8 - Calcular y mostrar la clasificación\n"
      print "9 - Salir" 
      op = raw_input() 

      if op == '5':
              fichero = open("liga.txt","w")

              for clubLocal in resultats_lliga:
                    for clubContra in resultats_lliga:
                        try:
                            muestra = resultats_lliga[clubLocal][clubContra]
                            mu = str(muestra)
                            numero = mu.partition(",")
                            num1 = numero[0].split('(') #Split corta las palabras
                            num2 = numero[2].split(')') 
                            fin = num2[0].strip() 
                      
                            fichero.write("%s*%s*%s*%s\n" % (clubLocal,clubContra,num1[1],fin))
                        except:
                            print "" #Sino, printo la cadena vacía    
              
              fichero.close()

      elif op == '1':
        fixero = open("equips.cfg","w")
        print "Introduce los nombres de los equipos de la liga"
        o = 1
        while o <= 3:
          print "Introduce otro. Para salir escribe 'sal' "
          intro = raw_input()
          
          if intro == 'sal':
            o = 4
          else:
            fixero.write(intro + "\n")
        fixero.close()
              
      elif op == '2':
       	fixe = open("equips.cfg","r")
       	fixo = open("equips.cfg","r")

       	for line in fixe:
          for linea in fixo:
            try:
              resultats_lliga3[linea.rstrip('\n')] = (None,None)
            except:
              print ""

          try:
				resultats_lliga[line.rstrip('\n')] = resultats_lliga3
				equiposPuntos[line.rstrip('\n')] = 0
          except:
				    print ""


      elif op == "3":

        print "Introducir resultados"

        d = 1
           
        print "Seleciona el club local"

        for clubLocal in resultats_lliga:
          print "%d - %s" % (d,clubLocal)
          d= d+ 1

          local = raw_input()
          
          z = 1
          print "Selecciona el club contrario\n"
          
          for clubLocal in resultats_lliga:
            print "%d - %s" % (y,clublocal)
            z= z+ 1
              
            contrario = raw_input()

            local = obtenerNumClub(local)
            contrario = obtenerNumClub(contrario)

            print "Introduce los goles marcados por %s" % (local),
            golesLocal = raw_input()

            print "Introduce los goles marcados por %s" % (contrario),
            golesContra = raw_input()

            try:
              insertarEquiposPuntos(golesLocal,golesContra,local,contrario) 
            except:
              print ""

            try:
              resultats_lliga[local][contrario] = (int(golesLocal),int(golesContra.strip()))
            except:
              print ""


      elif op == "4":
        
        print "Eliminar resultados\n"
        print "Selecciona el club local:\n"
          
        for clublocal in resultats_lliga:
          print "%d - %s" % (i,clubLocal)
          i += 1

          local = raw_input()
          y = 1
            
          print "Selecciona el club contrario:"
            
          for clublocal in resultats_lliga:
            print "%d - %s" % (y,clubLocal)
            y += 1
              
            contrario = raw_input()

            local = pasarnumclub(local)
            contrario = pasarnumclub(contrario)

            try:
              resultats_lliga[local][contrario] = (None,None)
            except:
              print ""

      elif op == '6':
        try:
          fifi = open("liga.txt","r")
          
          for lineas in fifi:
            cortar = lineas.split('*')
                  
            if cortar[2] == 'None':
              try:
                resultats_lliga[cortar[0]][cortar[1]] = (cortar[2],cortar[3].rstrip('\n'))
              except:
                print ""
            elif cortar[2] != 'None':
              try:
                resultats_lliga[cortar[0]][cortar[1]] = (int(cortar[2]),int(cortar[3].rstrip('\n')))
              except:
                print ""

          fifi.close()
        except:
          print ""

      elif op == "7":

        print "\nResultados de los partidos:\n"

        try:
          for clubLocal in resultats_lliga: 

            for clubContra in resultats_lliga:
              muestra = resultats_lliga[clubLocal][clubContra]
              mu = str(muestra)
              numero = mu.partition(",")
              num1 = numero[0].split('(')
              num2 = numero[2].split(')')
              fin = num2[0].strip()
              if fin == 'None':
                print "Partido contra %s y %s no disputado." % (clublocal,clubContra)
              elif fin != 'None':
                print "%s contra %s y quedaron %s a %s" % (clublocal,clubContra,num1[1],fin)

        except:
          print ""

      elif op == "8":
        
        print "\nClasificación:\n"
        
        import operator
        
        diccionario={"a":2, "b":3, "d":1, "c":1}
        resul = sorted(equiposPuntos.items(), key=operator.itemgetter(1))
        resul.reverse()

        for dia in resultado:
          mu = str(dia)
          print(te)
          numero = mu.partition(",")
          num1 = numero[0].split('(')
          num2 = numero[2].split(')')
          fin = num2[0].strip()

          print "Puntos del %s %s"% (num1,fin)

           
      elif op == '9':
        print "Pulsa 's' para salir"
        letra = raw_input()

        if letra == 's' or letra == 'S':
          i = 4
