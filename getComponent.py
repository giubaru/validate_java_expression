string = 'Objeto.getNombreFuncion("123").getAttribute("Nombre_Etiqueta") && Objeto.getNombreFuncion("Otra_Etiqueta").getAttribute("Nombre_Etiqueta")'
datos = string.split('"')[1::2]
resultado = []

for i in datos: #range(1,len(datos),2):
	print(i)#print(datos[i])
