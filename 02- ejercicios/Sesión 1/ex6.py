x= "There are %d types of people." %10 
#Se le asigna a la variable "x" un string
#Además, a la vez se le está asignando un número a la string

binary= "binary" 
#Se le signa a la variable binary el texto "binary"

do_not= "don't" #Lo mismo de antes

y= "Those who know %s and those who %s." % (binary, do_not)
#Se le asigna a la variable "y" un string
#A la vez se le asignan dos variable dentro del string que irán colocadas donde se encuentran los "%s"

print x
print y #Se imprimen las variables x e y

print "I said: %r." %x 
print "I also said: %s" %y
#se imprime un string al que se le ha asignado una variable

hilarious= False #será una variable Boolean
