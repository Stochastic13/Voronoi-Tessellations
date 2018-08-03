import tkinter as tk
from PIL.ImageTk import PhotoImage
from PIL import Image, ImageEnhance
import numpy as np
import sys

def labelupdate(which):
    if which==0:
        stat.set('Dot Mode')
    if which==1:
        stat.set('Gaussian Spray')

def saver(event=None):
    global finalarr
    finalarr = finalarr*fac
    finalarr[:,0],finalarr[:,1]=(np.array(finalarr[:,1],copy=False),np.array(finalarr[:,0],copy=True))
    with open(outfilename,'w',newline='') as f:
        f.write('\n'.join(list(map(lambda x: '\t'.join([str(x[0]),str(x[1])]),finalarr))))
    root.destroy()


def uniform(event=None):
    global finalarr
    n = int(scale2.get())
    px = np.random.rand(n)*img.size[0]
    py = np.random.rand(n)*img.size[1]
    if len(finalarr) == 0:
        finalarr = np.array(tuple(zip(px.tolist(), py.tolist())))
    else:
        finalarr = np.vstack((finalarr, np.array(tuple(zip(px.tolist(), py.tolist())))))
    draw_points()


def move_sprayer(event):
    if stat.get()=='Gaussian Spray':
        mainc.delete('pointer')
        sd = int(scale.get())
        mainc.create_oval((event.x-sd,event.y-sd,event.x+sd,event.y+sd),fill='',tags=('pointer',))

def draw_points():
    mainc.delete('points')
    if len(finalarr.shape)>1:
        for i in finalarr:
            valx,valy = i
            cx,cy = (int(valx),int(valy))
            mainc.create_oval((cx-1,cy-1,cx+1,cy+1),fill='red',outline='red',tag='points')
    else:
        valx,valy = finalarr
        cx, cy = (int(valx),int(valy))
        mainc.create_oval((cx - 1, cy - 1, cx + 1, cy + 1), fill='red', outline='red', tag='points')

def spray(event):
    global finalarr
    mode = {'Gaussian Spray':1,'Dot Mode':0}[stat.get()]
    if mode==0:
        px = mainc.canvasx(event.x)
        py = mainc.canvasy(event.y)
        if len(finalarr)==0:
            finalarr = np.array([float(px),float(py)])
        else:
            finalarr = np.vstack((finalarr,np.array([float(px),float(py)])))
        draw_points()
    elif mode==1:
        px = mainc.canvasx(event.x)
        py = mainc.canvasy(event.y)
        px = np.random.normal(float(px),float(scale.get()),int(nums.get()))
        py = np.random.normal(float(py),float(scale.get()),int(nums.get()))
        if len(finalarr)==0:
            finalarr = np.array(tuple(zip(px.tolist(),py.tolist())))
        else:
            finalarr = np.vstack((finalarr,np.array(tuple(zip(px.tolist(),py.tolist())))))
        draw_points()


def reset(event=None):
    global finalarr
    finalarr = np.array([])
    mainc.delete('points')


finalarr = np.array([])
filename = sys.argv[1]
outfilename = sys.argv[2]
root = tk.Tk()
img = Image.open(filename)
fac = 1
if img.size[0]>1200 or img.size[1]>900:
    fac = max((img.size[0]/1000),(img.size[1]/700))
img = img.resize((int(img.size[0]/fac),int(img.size[1]/fac)))
mainf = tk.Frame(root,width=img.size[0]+200,height=img.size[1])
mainf.pack()
mainc = tk.Canvas(mainf,width=img.size[0],height=img.size[1],bg='white')
mainc.grid(row=0,column=0,sticky='ns')
panel = tk.Frame(mainf,width=200,height=img.size[1],bg='white')
panel.grid(row=0,column=1,sticky='ns')
sharp = ImageEnhance.Sharpness(img)
img = sharp.enhance(0)
img.putalpha(210)
im = PhotoImage(img)
imc = mainc.create_image(0,0,image=im,anchor=tk.NW)
mainc.image=im
mainc.bind('<Motion>',move_sprayer)
mainc.bind('<Button-1>',spray)
stat = tk.StringVar(root)
stat.set('Select a mode')
l0 = tk.Label(panel,textvariable=stat,bg='black',fg='white',font=('lucida console',20))
l1 = tk.Button(panel,text='Dot Mode',command = lambda : labelupdate(0))
l2 = tk.Button(panel,text='Gaussian Spray mode',command = lambda : labelupdate(1))
nums = tk.Scale(panel,label='No. per click',from_=1,to=500,orient=tk.HORIZONTAL,resolution=1)
l0.grid(row=0,column=0,sticky='ew')
l1.grid(row=1,column=0,sticky='ew')
l2.grid(row=2,column=0,sticky='ew',pady=(20,0))
scale = tk.Scale(panel,from_=int(0.01*min(img.size)),to=max(img.size),label='SD for Spray',orient=tk.HORIZONTAL,resolution=0.1)
nums.grid(row=3,column=0,sticky='ew')
scale.grid(row=4,column=0,sticky='ew')
l3 = tk.Button(panel,text='add Uniform Random',command=uniform)
l3.grid(row=5,column=0,sticky='ew',pady=(20,0))
scale2 = tk.Scale(panel,from_=1,to=5000,label='No. of points to add',orient=tk.HORIZONTAL)
scale2.grid(row=6,column=0,sticky='ew')
l4 = tk.Button(panel,text='Reset',command=reset)
l4.grid(row=7,column=0,sticky='ew',pady=10)
l5 = tk.Button(panel,text='Save',command=saver)
l5.grid(row=8,column=0,sticky='ew')
root.mainloop()
