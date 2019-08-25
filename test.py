import tkinter as tk
import cv2
import PIL.Image, PIL.ImageTk
import time
from functools import partial
from cam import MyVideoCapture

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.frm = tk.Frame(self.window)
        self.frm.pack()
        self.lll=0
        x=["test2.mp4","test2.mp4",0,"test2.mp4","test2.mp4","test2.mp4","test2.mp4","test2.mp4","test2.mp4"]
        t=['Allocated:','Reserved:','Available:','Under maintenance:','Total:','']

        # open video source (by default this will try to open the computer webcam)
        self.vid = self.create_cams(x)
        self.l = self.create_cam_labels(len(x))
        self.photo = [None for i in range(len(x))]
        self.canvas = self.create_canvas(len(x))
        self.ll = self.create_data(t)
        self.btn = self.create_btn()

        self.General()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        self.window.mainloop()
    def create_canvas(self,size,w=256,h=192):
        return [tk.Canvas(self.frm, width = w, height = h) for i in range(size)]

    def create_cam_labels(self,size):
        return [tk.Label(self.frm,text="CAM"+str(i)) for i in range(1,size+1)]

    def create_cams(self,cams):
        return [MyVideoCapture(i) for i in cams]

    def create_data(self,t):
        return [tk.Label(self.frm,text=i) for i in t]

    def create_btn(self):
        x=[]
        x.append(tk.Button(self.frm,text="General",command=self.General))
        x.append(tk.Button(self.frm,text="Manual Booking",command=self.Manual_Booking))
        x.append(tk.Button(self.frm,text="ALL CAMERAS",command=self.all_cameras))
        x.append(tk.Button(self.frm,text="Settings",command=self.Settings))
        return x

    def General(self):
        for i in self.frm.winfo_children():
            i.grid_forget()
        self.l[0].grid(row=0,column=0)
        self.l[1].grid(row=0,column=1)
        self.l[2].grid(row=0,column=2)
        self.l[3].grid(row=2,column=0)
        self.l[4].grid(row=2,column=1)
        self.l[5].grid(row=2,column=2)
        self.canvas[0].grid(row=1,column=0)
        self.canvas[1].grid(row=1,column=1)
        self.canvas[2].grid(row=1,column=2)
        self.canvas[3].grid(row=3,column=0)
        self.canvas[4].grid(row=3,column=1)
        self.canvas[5].grid(row=3,column=2)
        self.ll[0].grid(row=4,column=0)
        self.ll[1].grid(row=4,column=1)
        self.ll[2].grid(row=4,column=2)
        self.ll[3].grid(row=5,column=0)
        self.ll[4].grid(row=5,column=1)
        self.ll[5].grid(row=5,column=2)
        self.btn[0].grid(row=6,column=0)
        self.btn[1].grid(row=6,column=1)
        self.btn[2].grid(row=6,column=2)
        self.btn[3].grid(row=7,column=1)

    def all_cameras(self):
        for i in self.frm.winfo_children():
            i.grid_forget()
        self.l[0].grid(row=0,column=0)
        self.l[1].grid(row=0,column=1)
        self.l[2].grid(row=0,column=2)
        self.l[3].grid(row=2,column=0)
        self.l[4].grid(row=2,column=1)
        self.l[5].grid(row=2,column=2)
        self.l[6].grid(row=4,column=0)
        self.l[7].grid(row=4,column=1)
        self.l[8].grid(row=4,column=2)
        self.canvas[0].grid(row=1,column=0)
        self.canvas[1].grid(row=1,column=1)
        self.canvas[2].grid(row=1,column=2)
        self.canvas[3].grid(row=3,column=0)
        self.canvas[4].grid(row=3,column=1)
        self.canvas[5].grid(row=3,column=2)
        self.canvas[6].grid(row=5,column=0)
        self.canvas[7].grid(row=5,column=1)
        self.canvas[8].grid(row=5,column=2)
        self.btn[0].grid(row=6,column=0)
        self.btn[1].grid(row=6,column=1)
        self.btn[2].grid(row=6,column=2)
        self.btn[3].grid(row=7,column=1)

    def Manual_Booking(self):
        for i in self.frm.winfo_children():
            i.grid_forget()
        self.z = tk.Label(self.frm,text="All Ok")
        self.z.grid(row=0,column=1)
        self.btn[0].grid(row=1,column=0)
        self.btn[1].grid(row=1,column=1)
        self.btn[2].grid(row=1,column=2)
        self.btn[3].grid(row=2,column=1)

    def Settings(self):
        for i in self.frm.winfo_children():
            i.grid_forget()
        self.z = tk.Label(self.frm,text="All Ok Settings")
        self.z.grid(row=0,column=1)
        self.btn[0].grid(row=1,column=0)
        self.btn[1].grid(row=1,column=1)
        self.btn[2].grid(row=1,column=2)
        self.btn[3].grid(row=2,column=1)

    def update(self):
        # Get a frame from the video source
        for i,n in enumerate(self.canvas):
        	self.create_photo(self.vid[i],i)

        self.window.after(self.delay, self.update)

    def create_photo(self,vid,i):
        ret, frame = vid.get_frame()
        if ret:
            self.photo[i] = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas[i].create_image(0, 0, image = self.photo[i], anchor = tk.NW)

 # Create a window and pass it to the Application object
App(tk.Tk(), "Yo MAMA is Great")
