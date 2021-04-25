from tkinter import *  #Si pones el asterisco, no tienes que poner un tkinte.algo, solo pones algo
from tkinter import filedialog #Libreria para poner explorador de archivos
import os,cv2,imutils,re   


#Window_1
'''def window_1():   

 Label(text="WELCOME", font=("Helvetica", 25), bg= "#40E0D0", fg= "#006400").pack(pady=10) #Configuración texto "Welcome"
 ButtonNew = Button(window_1, text="New Project", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[quit(window_1), window_2()]) #Configuración boton, New project
 ButtonNew.place(x=90,y=170)  #Posiciona los botones, no usar .pack
 ButtonContinue = Button(window_1, text="Continue Project", font=("Helvetica", 10), bg="yellow", width="20", height="8") #Configuración boton, Continue Project
 ButtonContinue.place(x=460,y=170)
'''

#Window_1
def window_1():
 welcome = Label(frame,text="WELCOME",font=("Helvetica", 25), bg= "#40E0D0", fg= "#006400")
 welcome.grid(row=0, column=0, sticky="n")  #Configuración texto "Welcome")
 ButtonNew = Button(frame, text="New Project", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), window_2()] ) #Configuración boton, New project
 ButtonNew.place(x=90,y=170)  #Posiciona los botones, no usar .pack
 ButtonContinue = Button(frame, text="Continue Project", font=("Helvetica", 10), bg="yellow", width="20", height="8") #Configuración boton, Continue Project
 ButtonContinue.place(x=460,y=170)
 #Button = Button(frame, text="clear frame", command=clearFrame)
 #Button.pack(fill=None, expand=False)

#Window_2
def window_2():
    
    #Label(window_1, width=100000000, height=100000000, bg="#40E0D0").pack()  #Color de fondo de pagina 1
    project = Label(frame, text="NEW PROJECT", font=("Helvetica", 25), bg= "#40E0D0", fg= "#006400") #Configuración texto "Welcome"
    project.grid(row=0, column=0, sticky="n")
    directory = Label(frame, text='Browse the directory for the "Data" folder', font=("Helvetica", 20), bg= "#40E0D0", fg= "blue")  #Configuracion texto "Browse the directory for the "Data" folder
    directory.grid(pady=65,row=0, column=0, sticky="n")
    browse_button= Button(frame, text="Browse..",command = browse, width=6, height=2, bg="blue", fg="yellow")
    browse_button.place(x=500,y=167)
    direction = Label(frame,width=50,textvariable = datapath, height = 2)
    direction.place(x=120,y=170)
    #direct = datapath.get()
    window3_button= Button(frame, text="Next ->",command =lambda:[clearFrame(), window_3()], width=10, height=3, bg="#006400", fg="yellow")
    window3_button.place(x=600,y=380)

#Window_3
def window_3():
    project = Label(frame, text="PERSON NAME", font=("Helvetica", 25), bg= "#40E0D0", fg= "#006400") #Configuración texto "persone name"
    project.grid(row=0, column=0, sticky="n")
    NameLabel= Label(frame, text = "Enter your name or the name of the person to register: ", font=("Helvetica", 15), bg ="#40E0D0" )
    NameLabel.place(x=120,y=105)
    namepath = Entry(width=50, textvariable = namepath_str)
    namepath.place(x=205,y=150)
    window4_button= Button(frame, text="Next ->",command =lambda:[clearFrame(), window_4(),Get_namepath(), namepath.destroy()], width=10, height=3, bg="#006400", fg="yellow")
    window4_button.place(x=600,y=380)

#Window_4
def window_4():
    project = Label(frame, text="PHOTO NUMBER", font=("Helvetica", 25), bg= "#40E0D0", fg= "#006400") #Configuración texto "persone name"
    project.grid(row=0, column=0, sticky="n")
    photonum = Entry(width=50, textvariable = photonum_str)
    photonum.place(x=205,y=150)
    photoLabel= Label(frame, text = "Enter the number of photos to take (If you take more is better): ", font=("Helvetica", 15), bg ="#40E0D0" )
    photoLabel.place(x=100,y=105)
    window5_button= Button(frame, text="Next ->",command =lambda:[clearFrame(), window_5(), photonum.destroy()], width=10, height=3, bg="#006400", fg="yellow")
    window5_button.place(x=600,y=380)

#window_5
def window_5():
    project = Label(frame, text="WHATS YOUR OPTION FOR PHOTO CAPTURE?: ", font=("Helvetica", 16), bg= "#40E0D0", fg= "#006400") #Configuración texto "persone name"
    project.grid(row=0, column=0, sticky="n")
    webcamb = Button(frame, text="Web Cam", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), webcam(), window_6()] ) #Configuración boton, New project
    webcamb.place(x=70,y=170)  #Posiciona los botones, no usar .pack
    ipcamerab = Button(frame, text="IP Camera", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), ipcamera()]) #Configuración boton, Continue Project
    ipcamerab.place(x=275,y=170)
    localvideob = Button(frame, text="Local Video", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), localvideo()]) #Configuración boton, Continue Project
    localvideob.place(x=480,y=170)

def window_6():
    project = Label(frame, text="WHAT WILL BE YOUR TRAINING METHOD:", font=("Helvetica", 16), bg= "#40E0D0", fg= "#006400") #Configuración texto "persone name"
    project.grid(row=0, column=0, sticky="n")
    EigenFace = Button(frame, text="Eigen Face", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), webcam(), window_6()] ) #Configuración boton, New project
    EigenFace.place(x=70,y=170)  #Posiciona los botones, no usar .pack
    FisherFace = Button(frame, text="Fisher Face", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), ipcamera()]) #Configuración boton, Continue Project
    FisherFace.place(x=275,y=170)
    LBPHFace = Button(frame, text="LBPH Face", font=("Helvetica", 10), bg="yellow", width="20", height="8", command =lambda:[clearFrame(), localvideo()]) #Configuración boton, Continue Project
    LBPHFace.place(x=480,y=170)


#Webcam
def webcam():
     
    #et_namepath(personPath)
    project = Label(frame, text="WEB CAM: ", font=("Helvetica", 16), bg= "#40E0D0", fg= "#006400") #Configuración texto "persone name"
    project.grid(row=0, column=0, sticky="n")
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  #Funcion para detectar objetos en video
    count = 0    #Contador en cero inicial

    while True:   #Mientras se ejecute se hace todo lo que está dentro

	    ret, frame1 = cap.read()   #Si está grabando
	    if ret == False: break    #Si no lo está haciendo, se sale del programa
	    frame1 =  imutils.resize(frame1, width=640)   #Corta imagenes del video en una medida de 650 pixeles de ancho frame=marco
	    gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)   #Cambia de color las imagenes de rgb a gris     cv2.cvtColor(se pone frame porque es lo que detecta el marco antes recortado, y la funcion del cambio de color que se hará)
	    auxFrame = frame1.copy()      #Crea una copia de la ultima imagen, la vdd no se para que, pero ok

	    faces = faceClassif.detectMultiScale(gray,1.3,5)   #Idk what is that

	    for (x,y,w,h) in faces:
		    cv2.rectangle(frame1, (x,y),(x+w,y+h),(125,255,0),2)      #Crea un rectangulo, sintaxis(image, start_point, end_point, color, thickness(grosor))
		    rostro = auxFrame[y:y+h,x:x+w]    #Idk what is that y tambien con esto  "Creo que es para el tamaño de la imagen actual"
		    rostro = cv2.resize(rostro,(150,150),interpolation=cv2.INTER_CUBIC) #Cambia el tamaño de las imagenes a 150x150 pixeles
		    cv2.imwrite(direct.get() + '/rostro_{}.jpg'.format(count),rostro)    #Funcion para guardar imagen sintaxis .imwrite(Nombre del archivo, imagen a guardar)  se guardará en el directorio que se esté usando
		    count = count + 1     #Count es la funcion para contar las imagenes tomadas, se eleva el numero para pasar a la siguiente
            
	    cv2.imshow('Detectando...',frame1)   #Crea una ventana para mostrar la camara en vivo

	    k =  cv2.waitKey(1)        #Funcion para esperar a que se presione una tecla
        
        #¡¡¡¡¡¡¡¡AGREGAR FUNCION DE WINDOW_6 PARA QUE CUANDO TERMINE DE TOMAR FOTOS, SE VAYA DIRECTO A LA 6
            
	    if k == ord("q") or count >= int(photonum_str.get()): 
		    break

    cap.release()              #Se acaba programa
    cv2.destroyAllWindows()



#IP Camera
def ipcamera():
 camera_url = input("Put your Ip for the local wifi camera: ")
 cap = cv2.VideoCapture(camera_url)       #Opcion para video desde ip local
 faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  #Funcion para detectar objetos en video
 count = 0    #Contador en cero inicial



#Localvideo
def localvideo():
 video_path = filedialog.askopenfilename(filetypes=[("mp4 files", "*.mp4")]) #abre el explorador de archivos y guarda la seleccion en la variable!
 cap = cv2.VideoCapture(video_path)      #Opcion para tomar imagenes de un video en carpeta creada
 faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')  #Funcion para detectar objetos en video
 count = 0    #Contador en cero inicial



#Funcion para concatenar la direccion
def Get_namepath():
    personPath = datapath.get() + '/Data/' + namepath_str.get()
    print(personPath)
    if not os.path.exists(personPath):     #Si no está creada la carpeta, se crea
	     print('Carpeta creada: ',personPath)
	     os.makedirs(personPath)
    direct.set(personPath)

#Funcion para buscar directorio
def browse():
    global datapath, items
    #datapath = Tk()
    #datapath = datapath.withdraw() #cierra ventana tkinter y abre explorador archivos 
    path = filedialog.askdirectory(title= 'Chosse the directory')
    datapath.set(path)

#Funcion para borrar el Frame actual
def clearFrame():
    # destroy all widgets from frame
    for widget in frame.winfo_children():
       widget.destroy()

#Funcion para salir de window_1
def quit(window_1):
    window_1.destroy()


#MAIN

root =Tk() #Creo la pestaña
#window.geometry("720x480")  #Pongo tamaño a la pestaña
root.title("Facial Recognition")   #Pongo titulo a la pestaña 1

frame = Frame(root, width=720, height=480, bg="#40E0D0")
frame.pack(fill='both', expand=True)
frame.grid_propagate(False)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)
#window_1.configure(bg="#40E0D0")  #Color de fondo de pagina 1
datapath = StringVar()
direct = StringVar()
namepath_str = StringVar()
photonum_str = StringVar()
items=['']
labels = []                             #Crea los strings globales
facesData = []
label = 0
window_1()



root.mainloop()
