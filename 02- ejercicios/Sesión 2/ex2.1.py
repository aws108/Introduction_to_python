def add(a,b):
	print "ADDING %d + %d" % (a,b)
	return a+b
	
def substract(a,b):
	print "SUBSTRACTING %d - %d" % (a,b)
	return a-b
	
def multiply(a,b):
	print "MULTIPLYNG %d * %d" % (a,b)
	return a*b
	
def divide(a,b):
	print "DIVIDING %d / %d" % (a,b)
	return a/b

print "Let's do some math with just functions!"

age1 = float(raw_input("Introduce una edad"))
age2 = float(raw_input("Introduce una segunda edad"))

height1=float(raw_input("Introduce una altura"))
height2=float(raw_input("Introduce una segunda altura"))

weight1=float(raw_input("Introduceun peso"))
weight2=float(raw_input("Introduce un segundo peso"))

iq1=float(raw_input("Introduce un valor para IQ"))
iq2=float(raw_input("Introduce un segundo palor para IQ"))

age= add(age1,age2)
height=substract(height1,height2)
weight = multiply(weight1,weight2)
iq = divide(iq1,iq2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight,iq)

#A puzzle for the extra credit, type it in anyway
print "Here is a puzzle"

what=add(age,substract(height,multiply(weight,divide(iq,2))))

print "That becomes: ", what, "Can you do it by hand?"
