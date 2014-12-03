#-*- coding: utf-8-*-

print "	•••••••••••••••••••••••••••••"
print " 	•    •Número Factorial•     •"
print "	•••••••••••••••••••••••••••••"

def factorial(numero):  
	if numero == 0 or numero == 1:
		residuo = 1
	elif numero > 1:
		residuo = numero*factorial(numero-1)
	return residuo

num = True
while num == True:
	try:
		digitos=int(raw_input("Ingrese Un Número: "))
		print "Su Factorial es: %s"%factorial(digitos)
		re = True
		while re == True:
			reingreso = raw_input("Desea volver a ingresar otro valor Si/No: ")
			try:
				if reingreso.isalpha()==True:
					if reingreso.lower()=="si":
						re=False
					elif reingreso.lower()=="no":
						num = False
						print "Adios"
						break
			except:
				num = True
	except ValueError,NameError:
		print "No se aceptan datos Alfabeticos"