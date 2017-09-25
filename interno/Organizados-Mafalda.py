import shutil, os
import time
import random
from PIL import Image

#prev:crear una carpeta que se llame Historial dónde están todas las imagenes.
#Aclaración, por ahora solo abre la imagen seleccionada al terminar el programa, vemos bien q hacemos con eso, se cambia al toque igual.

def fotos_a_lista():
    archivos= os.listdir()
    new_list=[]
    for file in archivos:
        if 'jpg' in file.lower() or 'png' in file.lower():
            new_list.append(file)
    return new_list


def devolver_imagen():
    """Devuelve una nueva imagen"""
    lista=fotos_a_lista()
    img = random.choice(lista)
    guardar_en_historial(img)
    mover_carpeta_historial(img)



def guardar_en_historial(imagen):
    """ Guarda en historial.txt el nombre del mafalda agregado y en la fecha que sucedió """
    arch = open("historial.txt",'a')
    fecha = time.strftime("%d/%m/%y")
    cadena = imagen + " - " + fecha + "\n"
    arch.write(cadena)
    arch.close()

def mover_carpeta_historial(imagen):
    """Mueve la imagen a la carpeta de las imagenes ya usadas"""
    prev_name = imagen
    new_name = 'Historial/' + imagen
    os.rename(prev_name,new_name)
    mafalda = Image.open(new_name)
    mafalda.show()


    

devolver_imagen()