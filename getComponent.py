string = 'Objeto.getNombreFuncion("123").getAttribute("Nombre_Etiqueta") && Objeto.getNombreFuncion("Otra_Etiqueta").getAttribute("Nombre_Etiqueta")'
datos = string.split('"')
resultado = []

for i in range(1,len(datos),2):
	print(datos[i])