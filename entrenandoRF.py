import cv2
import os
import numpy as np

dataPath = 'C:/Users/carl2/Desktop/Reconocimiento/Datos' #Cambia a la ruta donde hayas almacenado Data
peopleList = os.listdir(dataPath)       #Lleva a la carpeta Datos
print('Lista de personas: ', peopleList)  #Imprime los nombres de las carpetas con los nombres

labels = []                             #Crea los strings globales
facesData = []
label = 0

for nameDir in peopleList:
	personPath = dataPath + '/' + nameDir     #Lée las imagenes a travez de un for con rutas
	print('Leyendo las imágenes')

	for fileName in os.listdir(personPath):
		print('Rostros: ', nameDir + '/' + fileName)     #Imprime la direccion de las imagenes
		labels.append(label)      #Agrega etiquetas al array 
		facesData.append(cv2.imread(personPath+'/'+fileName,0))    #Agrega y lee imagenes en el array
		#image = cv2.imread(personPath+'/'+fileName,0)
		#cv2.imshow('image',image)
		#cv2.waitKey(10)
	label = label + 1    #Aumenta el contador de las etiquetas

#print('labels= ',labels)   #Imprime el array de las atiquetas
print('Número de etiquetas 0: ',np.count_nonzero(np.array(labels)==0))   #Imprime el numero de etiquetas de cada numero 0,1,2....
print('Número de etiquetas 1: ',np.count_nonzero(np.array(labels)==1))

# Métodos para entrenar el reconocedor
#face_recognizer = cv2.face.EigenFaceRecognizer_create()
#face_recognizer = cv2.face.FisherFaceRecognizer_create()
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Entrenando el reconocedor de rostros
print("Entrenando...")
face_recognizer.train(facesData, np.array(labels))

# Almacenando el modelo obtenido
#face_recognizer.write('modeloEigenFace.xml')
#face_recognizer.write('modeloFisherFace.xml')
face_recognizer.write('modeloLBPHFace.xml')
print("Modelo almacenado...Listo")