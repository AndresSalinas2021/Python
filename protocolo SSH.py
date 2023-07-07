
import paramiko
import time
import os
from paramiko import SSHClient
import getpass

j=0
nombre_Archivo = ""

def realizar_solicitud(comando):
    # Inicia un cliente SSH
    ssh_client = SSHClient()
    # Establecer política por defecto para localizar la llave del host localmente
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Conectarse
    passwd = getpass.getpass('Password6767: ')
    ssh_client.connect(hostname='ip router' , username='usuario router' , password=passwd, look_for_keys=False)
    # Ejecutar un comando de forma remota capturando entrada, salida y error estándar
    stdin, stdout, stderr = ssh_client.exec_command(comando)
    # Mostrar la salida estándar en pantalla
    for line in stdout.readlines():
        print(line)
    # Cerrar la conexión
    ssh_client.close()
def Eliminar_solicitud(comando):
    os.remove(comando) #colocar la url donde esta el archivo a 
    
def Consultar_Archivo(comando):
    f = open(comando)   #aca se abre el archivo
    print(f.read()) 
    
def Guardar_solicitud(comando):
    # Inicia un cliente SSH
    ssh_client = SSHClient()
    # Establecer política por defecto para localizar la llave del host localmente
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Conectarse
    passwd = getpass.getpass('Password: ')
    ssh_client.connect(hostname='10.30.10.2' , username='Nivel1Soporte' , password=passwd, look_for_keys=False)
    # Ejecutar un comando de forma remota capturando entrada, salida y error estándar
    stdin, stdout, stderr = ssh_client.exec_command(comando)
    # Mostrar la salida estándar en pantalla
        
    line = stdout.readlines()
    f = open(nombre_Archivo +".txt", "a")     # a modo agregar  todo lo que tenemos 
    f.writelines(line)                    # agrega el contenido que esta aca lineas
    f.close() 
    # for line in stdout.readlines():
    #     # print(line)
    #     # f = open("archivo_nuevo.txt", "a") #abre archivo y lo prepara para agregar texto
    #     # f.write(line)            #lo que se agregara al archivo al final
    #     # f.close()                             # sin esta linea no se refleja  la agregacion
    #     f = open("archivo_nuevo.txt", "a")     # a modo agregar  todo lo que tenemos 
    #     f.writelines(line)                    # agrega el contenido que esta aca lineas
    #     f.close() 
    # Cerrar la conexión
    ssh_client.close()

while j==0:
    print("""\n=== Bienvenido a la plataforma ===\n
    Cual funcion desea realizar\n
    desea hacer una consulta o guardar consulta
    1) consulta
    2) guardar
    3) Eliminar
    4) Consultar Archivos
    5) salir""")
    selec_consult = input("\n>")
    if selec_consult == '1':
        j=1
    elif selec_consult == '2':
        j=2
        print("\nIngrese nombre del archivo: ")
        nombre_Archivo = input("\n>")
        f = open(nombre_Archivo +".txt", "x")  # se crea un nuevo archivo
    elif selec_consult == '3':
        j=0
        print("\nIngrese nombre del archivo a eliminar: ")
        nombre_Archivo = input("\n>")
        Eliminar_solicitud(nombre_Archivo)
    elif selec_consult == '4':
        j=0
        print("\nIngrese nombre del archivo a consultar: ")
        nombre_Archivo = input("\n>")
        Consultar_Archivo(nombre_Archivo)
    else:
        print("\nGracias por usar el programa ;)")
        time.sleep(2)
        quit()

while True:
    print("""\n=== Bienvenido a la plataforma ===\n
    Cual funcion desea realizar\n
    1) ping
    2) ip address
    3) ip router
    4) ip arp print
    5) salir""")
    seleccion = input("\n>")
    if seleccion == '1':
        comando = 'ping 8.8.8.8'
        if j==1:
            realizar_solicitud(comando)
        if j==2:
            Guardar_solicitud(comando)        
    elif seleccion == '2':
        comando = 'ip address/ p'
        if j==1:
            realizar_solicitud(comando)
        if j==2:
            Guardar_solicitud(comando)
    elif seleccion == '3':
        comando = 'ip route/ p'
        if j==1:
            realizar_solicitud(comando)
        if j==2:
            Guardar_solicitud(comando)
    elif seleccion == '4':
        comando = 'ip arp print'
        if j==1:
            realizar_solicitud(comando)
        if j==2:
            Guardar_solicitud(comando)
    else:
        print("\nGracias por usar el programa;)")
        time.sleep(2)
        quit()
    