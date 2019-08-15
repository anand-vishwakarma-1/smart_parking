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
        self.vid = [MyVideoCapture(i) for i in x]
        self.photo = ["" for i in range(len(x))]
        self.l=[tk.Label(self.frm,text="CAM"+str(i)) for i in range(1,len(x)+1)]
        self.l[0].grid(row=0,column=0)
        self.l[1].grid(row=0,column=1)
        self.l[2].grid(row=0,column=2)
        self.l[3].grid(row=2,column=0)
        self.l[4].grid(row=2,column=1)
        self.l[5].grid(row=2,column=2)
        #self.l[6].grid(row=4,column=0)
        #self.l[7].grid(row=4,column=1)
        #self.l[8].grid(row=4,column=2)

        # Create a canvas that can fit the above video source size
        #self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
        self.canvas = [tk.Canvas(self.frm, width = 320, height = 240) for i in range(len(x))]
        self.canvas[0].grid(row=1,column=0)
        self.canvas[1].grid(row=1,column=1)
        self.canvas[2].grid(row=1,column=2)
        self.canvas[3].grid(row=3,column=0)
        self.canvas[4].grid(row=3,column=1)
        self.canvas[5].grid(row=3,column=2)
    	#self.canvas[6].grid(row=5,column=0)
    	#self.canvas[7].grid(row=5,column=1)
    	#self.canvas[8].grid(row=5,column=2)

        self.ll = [tk.Label(self.frm,text=i) for i in t]
        self.ll[0].grid(row=4,column=0)
        self.ll[1].grid(row=4,column=1)
        self.ll[2].grid(row=4,column=2)
        self.ll[3].grid(row=5,column=0)
        self.ll[4].grid(row=5,column=1)
        self.ll[5].grid(row=5,column=2)

        self.btn = tk.Button(self.frm,text="ALL CAMERAS",command=self.all_cameras)
        self.btn.grid(row=6,column=1)

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 1
        self.update()

        self.window.mainloop()

    #def single_cam(self,i):
    #	self.xx=tk.Toplevel()
    #	self.lll=1

    def all_cameras(self):
    	for i in range(len(self.ll)):
    		self.ll[i].grid_forget()
    	self.l[6].grid(row=4,column=0)
    	self.l[7].grid(row=0,column=3)
    	self.l[8].grid(row=2,column=3)

    	self.canvas[6].grid(row=5,column=0)
    	self.canvas[7].grid(row=1,column=3)
    	self.canvas[8].grid(row=3,column=3)
    	

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