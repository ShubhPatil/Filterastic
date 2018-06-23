# Libraries
from Tkinter import *
from PIL import Image
from PIL import ImageTk
import cv2, threading, os, time
from threading import Thread

previous=0
smile=0

def get_sprite(num):
    global SPRITES
    SPRITES[num] = (1 - SPRITES[num])

def smile_Detection(current):
    global previous
    global smile
    global SPRITES

    if(current==0 and previous==1):
        smile=smile+1
        if smile==16:
            smile=0
        SPRITES[smile-1]= 1
        if smile>1:
            SPRITES[smile-2]= 0
        
    previous=current

# Applying filter
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape 
    rows, cols, _ = src.shape  
    y, x = pos[0], pos[1]

    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src

# Main Program
def cvloop(run_event):
    global panelA
    global SPRITES
    sc=0
    
    cap = cv2.VideoCapture(0)
    face_cascade = cv2.CascadeClassifier('Xml/haarcascade_frontalface_default.xml')
    noseCascade = cv2.CascadeClassifier('Xml/haarcascade_mcs_nose.xml')
    smile_cascade = cv2.CascadeClassifier('Xml/haarcascade_smile.xml')

    while run_event.is_set(): #while the thread is active we loop
        _, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img, 1.1, 5)
        for (x,y,w,h) in faces:

            # Crown1 Filter
            if SPRITES[0]:
                crown = cv2.imread('Pics/Crown/crown.png', -1)
                #crown = cv2.imread('s2.png', -1)
                crown_roi_color = img[y-20:y+h/3, x-5:x+w]
                crown = cv2.resize(crown, (w+20,int(h/2.2)),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(crown_roi_color,crown)

            # Crown2 Filter
            if SPRITES[1]:
                crown = cv2.imread('Pics/Crown/crown2.png', -1)
                crown_roi_color = img[y-20:y+h/3, x-5:x+w]
                crown = cv2.resize(crown, (w+20,int(h/2)),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(crown_roi_color,crown)

            # Crown3 Filter
            if SPRITES[2]:
                crown = cv2.imread('Pics/Crown/crown3.png', -1)
                crown_roi_color = img[y-40:y+h+35, x-25:x+w+25]
                crown = cv2.resize(crown, (w+50,int(h/2)),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(crown_roi_color,crown)

            # Glass 1 Filter
            if SPRITES[3]:
                specs_ori = cv2.imread('Pics/Glasses/glass.png', -1)
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax+30 - glass_symin
                face_glass_roi_color = img[glass_symin-10:glass_symax+20, x:x+w]
                specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Glass 2 Filter
            if SPRITES[4]:
                specs_ori = cv2.imread('Pics/Glasses/glass2.png', -1)
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax+30 - glass_symin
                face_glass_roi_color = img[glass_symin-10:glass_symax+20, x:x+w]
                specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Glass 3 Filter
            if SPRITES[5]:
                specs_ori = cv2.imread('Pics/Glasses/glass3.png', -1)
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax+30 - glass_symin
                face_glass_roi_color = img[glass_symin-10:glass_symax+20, x:x+w]
                specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Glass 4 Filter
            if SPRITES[6]:
                specs_ori = cv2.imread('Pics/Glasses/glass4.png', -1)
                glass_symin = int(y + 1.5 * h / 5)
                glass_symax = int(y + 2.5 * h / 5)
                sh_glass = glass_symax+30 - glass_symin
                face_glass_roi_color = img[glass_symin-10:glass_symax+20, x:x+w]
                specs = cv2.resize(specs_ori, (w, sh_glass),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)
                
            # Hat 1 Filter
            if SPRITES[7]:
                hat = cv2.imread('Pics/Hat/hat1.png', -1)
                face_glass_roi_color = img[y-110:y+10, x-45:x+w+60] 
                specs = cv2.resize(hat, (w+90 , 120),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Hat 2 Filter
            if SPRITES[8]:
                hat = cv2.imread('Pics/Hat/hat2.png', -1)
                face_glass_roi_color = img[y-150:y, x+8:x+w+10] 
                specs = cv2.resize(hat, (w , 150),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Hat 3 Filter
            if SPRITES[9]:
                hat = cv2.imread('Pics/Hat/hat3.png', -1)
                face_glass_roi_color = img[y-130:y+20, x-30:x+w+30] 
                specs = cv2.resize(hat, (w+50 , 150),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Hat 4 Filter
            if SPRITES[10]:
                hat = cv2.imread('Pics/Hat/hat4.png', -1)
                face_glass_roi_color = img[y-110:y+70, x-10:x+w+20] 
                specs = cv2.resize(hat, (w+30 , 180),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Hat 5 Filter
            if SPRITES[11]:
                hat = cv2.imread('Pics/Hat/hat5.png', -1)
                face_glass_roi_color = img[y-100:y+30, x-45:x+w+50] 
                specs = cv2.resize(hat, (w+80 , 130),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Mustache Filter
            if SPRITES[12]:
                imgMustache = cv2.imread('Pics/Mustache/mustache.png',-1)
                orig_mask = imgMustache[:,:,3]
                orig_mask_inv = cv2.bitwise_not(orig_mask)
                imgMustache = imgMustache[:,:,0:3]
                origMustacheHeight, origMustacheWidth = imgMustache.shape[:2]

                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]

                nose = noseCascade.detectMultiScale(roi_gray)
                for (nx,ny,nw,nh) in nose:
                    mustacheWidth =  2 * nw
                    mustacheHeight = mustacheWidth * origMustacheHeight / origMustacheWidth
                    x1 = nx - (mustacheWidth/4)
                    x2 = nx + nw + (mustacheWidth/4)
                    y1 = ny + nh - (mustacheHeight/2)
                    y2 = ny + nh + (mustacheHeight/2)
                    if x1 < 0:
                        x1 = 0
                    if y1 < 0:
                        y1 = 0
                    if x2 > w:
                        x2 = w
                    if y2 > h:
                        y2 = h
                    mustacheWidth = x2 - x1
                    mustacheHeight = y2 - y1
                    mustache = cv2.resize(imgMustache, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                    mask = cv2.resize(orig_mask, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                    mask_inv = cv2.resize(orig_mask_inv, (mustacheWidth,mustacheHeight), interpolation = cv2.INTER_AREA)
                    roi = roi_color[y1:y2, x1:x2]
                    roi_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
                    roi_fg = cv2.bitwise_and(mustache,mustache,mask = mask)
                    dst = cv2.add(roi_bg,roi_fg)
                    roi_color[y1:y2, x1:x2] = dst
                    break

            # Animal 1 Filter
            if SPRITES[13]:
                hat = cv2.imread('Pics/Animal/dog.png', -1)
                face_glass_roi_color = img[y-20:y+h, x-15:x+w+15] 
                specs = cv2.resize(hat, (w+15 , int(h/1.1)),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Animal 2 Filter
            if SPRITES[14]:
                hat = cv2.imread('Pics/Animal/cat.png', -1)
                face_glass_roi_color = img[y-20:y+h+15, x-5:x+w+15] 
                specs = cv2.resize(hat, (w+15 , h),interpolation=cv2.INTER_CUBIC)
                transparentOverlay(face_glass_roi_color,specs)

            # Screen Shot
            if SPRITES[15]:
                sc=sc+1
                cv2.imwrite('Screenshots/sc(%d).jpg'%sc,img)
                SPRITES[9] = 0

            # Smile I/O
            if SPRITES[16]:
                global previous
                global smile
                smiles = smile_cascade.detectMultiScale(
                    gray,
                    scaleFactor= 1.7,
                    minNeighbors=50,
                    minSize=(25, 25),
                    flags=cv2.CASCADE_SCALE_IMAGE
                    )
                
                for (x,y,w,h) in smiles:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
                    
                if len(smiles) == 0:
                    #print "No Smile Detected"
                    smile_Detection(0)
                else:
                    #print "SMILE : "+str(smiles.shape[0])
                    smile_Detection(1)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(img)
        panelA.configure(image=img)
        panelA.img = img
    cap.release()

#GUI
app = Tk()
app.title("SnapChat")

# Video Feed
panelA = Label(app)
panelA.pack()

# GUI Buttons
#######################################################################################
## Crown Drop Down
crown1=ImageTk.PhotoImage(file="icons/crown1.png")
crown2=ImageTk.PhotoImage(file="icons/crown2.png")
crown3=ImageTk.PhotoImage(file="icons/crown3.png")
mb=  Menubutton(app, text="Crowns", relief=RAISED)
mb.grid()
mb.menu =  Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mb.menu.add_checkbutton ( image=crown1,label="Crown 1", command = lambda: get_sprite(0))
mb.menu.add_checkbutton ( image=crown2,label="Crown 2", command = lambda: get_sprite(1))
mb.menu.add_checkbutton ( image=crown3,label="Crown 3", command = lambda: get_sprite(2))

mb.pack(side="left", expand="no", padx="5", pady="5")

#######################################################################################
## Glasses Drop Down
glass1=ImageTk.PhotoImage(file="icons/glass1.png")
glass2=ImageTk.PhotoImage(file="icons/glass2.png")
glass3=ImageTk.PhotoImage(file="icons/glass3.png")
glass4=ImageTk.PhotoImage(file="icons/glass4.png")
mb2=  Menubutton(app, text="Glasses", relief=RAISED)
mb2.grid()
mb2.menu =  Menu ( mb2, tearoff = 0 )
mb2["menu"] =  mb2.menu

mb2.menu.add_checkbutton ( image=glass1,label="Glass 1", command = lambda: get_sprite(3))
mb2.menu.add_checkbutton ( image=glass2,label="Glass 2", command = lambda: get_sprite(4))
mb2.menu.add_checkbutton ( image=glass3,label="Glass 3", command = lambda: get_sprite(5))
mb2.menu.add_checkbutton ( image=glass4,label="Glass 4", command = lambda: get_sprite(6))

mb2.pack(side="left", expand="no", padx="5", pady="5")

#######################################################################################
## Hats Drop Down
hat1=ImageTk.PhotoImage(file="icons/hat1.png")
hat2=ImageTk.PhotoImage(file="icons/hat2.png")
hat3=ImageTk.PhotoImage(file="icons/hat3.png")
hat4=ImageTk.PhotoImage(file="icons/hat4.png")
hat5=ImageTk.PhotoImage(file="icons/hat5.png")
mb3=  Menubutton(app, text="Hats", relief=RAISED)
mb3.grid()
mb3.menu =  Menu ( mb3, tearoff = 0 )
mb3["menu"] =  mb3.menu

mb3.menu.add_checkbutton ( image=hat1,label="Hat 1", command = lambda: get_sprite(7))
mb3.menu.add_checkbutton ( image=hat2,label="Hat 2", command = lambda: get_sprite(8))
mb3.menu.add_checkbutton ( image=hat3,label="Hat 3", command = lambda: get_sprite(9))
mb3.menu.add_checkbutton ( image=hat4,label="Hat 4", command = lambda: get_sprite(10))
mb3.menu.add_checkbutton ( image=hat5,label="Hat 5", command = lambda: get_sprite(11))

mb3.pack(side="left", expand="no", padx="5", pady="5")

#######################################################################################
## Mustache Drop Down
mustache1=ImageTk.PhotoImage(file="icons/mustache1.png")
mb4=  Menubutton(app, text="Mustache", relief=RAISED)
mb4.grid()
mb4.menu =  Menu ( mb4, tearoff = 0 )
mb4["menu"] =  mb4.menu

mb4.menu.add_checkbutton ( image=mustache1,label="Mustache 1", command = lambda: get_sprite(12))

mb4.pack(side="left", expand="no", padx="5", pady="5")
#######################################################################################
## Animal Drop Down
dog=ImageTk.PhotoImage(file="icons/dog.png")
cat=ImageTk.PhotoImage(file="icons/cat.png")
mb5=  Menubutton(app, text="Animal", relief=RAISED)
mb5.grid()
mb5.menu =  Menu ( mb5, tearoff = 0 )
mb5["menu"] =  mb5.menu

mb5.menu.add_checkbutton ( image=dog,label="Dog", command = lambda: get_sprite(13))
mb5.menu.add_checkbutton ( image=cat,label="Cat", command = lambda: get_sprite(14))

mb5.pack(side="left", expand="no", padx="5", pady="5")
#######################################################################################

# Variable to control which sprite you want to visualize
SPRITES = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Creates a thread where the magic ocurs
run_event = threading.Event()
run_event.set()
action = Thread(target=cvloop, args=(run_event,))
action.setDaemon(True)
action.start()

# Function to close all properly, aka threads and GUI
def terminate():
        global app, run_event, action
        run_event.clear()
        time.sleep(1)
        app.destroy()

btn5 = Button(app, text="Exit",fg="red", command =terminate )
btn5.pack(side="left", expand="no", padx="10", pady="10")

btn6 = Button(app, text="Screen Shot",fg="green", command =lambda: get_sprite(15))
btn6.pack(side="left", expand="no", padx="10", pady="10")

btn7 = Button(app, text="Smile I/O",fg="blue", command =lambda: get_sprite(16))
btn7.pack(side="left", expand="no", padx="10", pady="10")

# When the GUI is closed it actives the terminate function
app.protocol("WM_DELETE_WINDOW", terminate)
app.mainloop()

