# f = open("leerarchivos txt/archivo.txt")   #aca se abre el archivo
# print(f.read())                            #aca solo se puede leer

# f = open("leerarchivos txt/archivo_nuevo.txt", "x")  # se crea un nuevo archivo

# f = open("leerarchivos txt/archivo.txt", "a") #abre archivo y lo prepara para agregar texto
# f.write("\nLínea Nueva")            #lo que se agregara al archivo al final
# f.close()                             # sin esta linea no se refleja  la agregacion

# f = open("leerarchivos txt/archivo.txt", "w")     # w modo write elimina todo lo que tenemos 
# f.write("Contenido nuevo")                         # agrega el contenido que esta aca
# f.close()                                       #se debe cerrar el archivo para que los cambios se reflejen

# f = open("leerarchivos txt/archivo.txt", "a")     # a modo agregar  todo lo que tenemos 
# f.writelines(["\n este archivo es de prueba","\n", "\n",
# "\nasi que ","\n","\n", "\nvamos a hacer que funcione"])                    # agrega el contenido que esta aca lineas
# f.close()                                       #se debe cerrar el archivo para que los cambios se reflejen

# f = open("leerarchivos txt/archivo_nuevo.txt", "x")  # se crea un nuevo archivo
# import os               #para eliminar el archivo 
# os.remove("leerarchivos txt/archivo_nuevo.txt") #colocar la url donde esta el archivo a eliminar

with open("leerarchivos txt/archivo.txt", "r+") as f:  # se abre el archivo para la lectura 
    print(f.readlines())    #se cierra el arrchivo automaticamente recordar identar

