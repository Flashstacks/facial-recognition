import cv2
import os
import imutils
import tkinter, re                     #liberia para ventana de seleccion de archivo 
from tkinter import filedialog

root = tkinter.Tk() #esto se hace solo para eliminar la ventanita de Tkinter 
root.withdraw() #ahora se cierra 


personName = 'Christian'   #Aqui se pone el nombre de la persona o cosa a identificar 
dataPath = 'C:/Users/carl2/Desktop/Reconocimiento/Datos' #Cambia a la ruta donde hayas almacenado Data
personPath = dataPath + '/' + personName   #Se crea la string para crear la ruta de la carpeta para almacenar las fotos


if not os.path.exists(personPath):     #Si no está creada la carpeta, se crea
	print('Carpeta creada: ',personPath)
	os.makedirs(personPath)     #Crea el directorio y me lleva a el

print("Select a video option for the photo capture: ")
print("1: Local Camera ")
print("2: IP Camera")
print("3: Local Video")
video_option = input("Put your option here: ")

if video_option =='1':
	 cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Opcion para activar video en vivo
elif video_option =='2':
	camera_url = input("Put your Ip for the local wifi camera: ")
	cap = cv2.VideoCapture(camera_url)       #Opcion para video desde ip local
elif video_option =='3':
	video_path = filedialog.askopenfilename(filetypes=[("mp4 files", "*.mp4")]) #abre el explorador de archivos y guarda la seleccion en la variable!
	cap = cv2.VideoCapture(video_path)      #Opcion para tomar imagenes de un video en carpeta creada

faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  #Funcion para detectar objetos en video
count = 0    #Contador en cero inicial

while True:   #Mientras se ejecute se hace todo lo que está dentro

	ret, frame = cap.read()   #Si está grabando
	if ret == False: break    #Si no lo está haciendo, se sale del programa
	frame =  imutils.resize(frame, width=640)   #Corta imagenes del video en una medida de 650 pixeles de ancho frame=marco
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   #Cambia de color las imagenes de rgb a gris     cv2.cvtColor(se pone frame porque es lo que detecta el marco antes recortado, y la funcion del cambio de color que se hará)
	auxFrame = frame.copy()      #Crea una copia de la ultima imagen, la vdd no se para que, pero ok

	faces = faceClassif.detectMultiScale(gray,1.3,5)   #Idk what is that

	for (x,y,w,h) in faces:
		cv2.rectangle(frame, (x,y),(x+w,y+h),(125,255,0),2)      #Crea un rectangulo, sintaxis(image, start_point, end_point, color, thickness(grosor))
		rostro = auxFrame[y:y+h,x:x+w]    #Idk what is that y tambien con esto  "Creo que es para el tamaño de la imagen actual"
		rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC) #Cambia el tamaño de las imagenes a 150x150 pixeles
		cv2.imwrite(personPath + '/rostro_{}.jpg'.format(count),rostro)    #Funcion para guardar imagen sintaxis .imwrite(Nombre del archivo, imagen a guardar)  se guardará en el directorio que se esté usando
		count = count + 1     #Count es la funcion para contar las imagenes tomadas, se eleva el numero para pasar a la siguiente
	cv2.imshow('Detectando...',frame)   #Crea una ventana para mostrar la camara en vivo

	k =  cv2.waitKey(1)        #Funcion para esperar a que se presione una tecla
	if k == ord("q") or count >= 300:   #Funcion por si la tecla 27(ESC) es presionada se acabe o hasta que tome 300 fotos empezando en numero 0 hasta 299
		break

cap.release()              #Se acaba programa
cv2.destroyAllWindows()