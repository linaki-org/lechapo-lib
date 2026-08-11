"""Le_chapo_lib is a free/open-source module for create a litles cutes games"""
import tkinter as TK #On importe tkinter
from time import sleep
from subprocess import run, PIPE
import tkinter.messagebox as TKBOX
from math import sqrt
import threading as THR
stamps=[]
imgs=[]
virtuals=[]

def _verify():
    """System function, verify if window exists"""
    try:
        root_tk
    except NameError:
        raise ChapoError("Window not exists")
    
def _distance(sp1, sp2):
    x1, y1=_xy(sp1)
    x2, y2=_xy(sp2)
    return round(sqrt((x2-x1)**2 + (y2-y1)**2))

def _xy(sp):
    pos=c.coords(sp.id)
    if sp.nature=="img":
        x=pos[0]
        y=pos[1]
        x+=sp.brut.width()
        y=sp.brut.height()
        return x, y
    x=(pos[0] + pos[2])/2
    y=(pos[1] + pos[3])/2
    return x, y

def _collide(sp1, sp2):
    return _distance(sp1, sp2) < ((sp1.brut.height()/2) + (sp2.brut.height()/2))

class Sprite:
    """Create a sprite"""
    def __init__(self, id, brut, nature):
        """Create the sprite"""
        _verify()
        self.id=id
        self.brut=brut
        self.nature=nature
        if self.id in (chapi_body, chapi_eye, chapi_pupil, chapi_mouth, chapi_neck, chapi_chapo, words_zone):
            raise ChapoError("'%s' id reserved to system"%self.id)
    def move(self, x, y):
        """Move the sprite"""
        _verify()
        c.move(self.id, x, y)
    def _change_state(self, spstate):
        """System function, change state of sprite (hidden or normal)"""
        _verify()
        if spstate in ("hidden", "normal"):
            pass
        else:
            raise ChapoError("Invalid option '%s'"%spstate)
        c.itemconfig(self.id, state=spstate)
    def hide(self):
        """Hide the Sprite"""
        self._change_state("hidden")
    def show(self):
        """Show the sprite"""
        self._change_state("normal")
    def is_on_collide(self, sprite):
        """Verify collide"""
        return _collide(self, sprite)
    def bind(self, event, command):
        """Link event to sprite"""
        c.tag_bind(self.id, event, command)

class _Virtual:
    """System class"""
    def __init__(self, id, brut, nature):
        """Init"""
        _verify()
        self.id=id
        self.brut=brut
        self.nature=nature

class _Brut:
    """System class"""
    def __init__(self, height, width):
        """Init"""
        self.Vwidth=width
        self.Vheight=height
    def height(self):
        """Height"""
        return self.Vheight
    def width(self):
        """Width"""
        return self.Vwidth

def img(file, x, y):
    global imgs
    imgs.append(TK.PhotoImage(file=file))
    id=c.create_image(x, y, anchor="nw", image=imgs[-1])
    obj=Sprite(id, imgs[-1], "img")
    update()
    return obj

class ChapoError(Exception):
    pass

class Music(THR.Thread):
    """This class play background music."""
    def __init__(self, file):
        """Init the instance"""
        THR.Thread.__init__(self)
        self.file=file
    def play(self):
        """Play music"""
        self.start()
    def run(self):
        """Thread function run"""
        music(self.file)

def init(height=300, width=400):
    """Create le_chapo_lib window and draw the character"""
    global root_tk
    try:
        root_tk
    except:
        pass
    else:
        raise ChapoError("Use one window only")
    
    global c
    global chapi_body
    global chapi_eye
    global chapi_pupil
    global chapi_mouth
    global chapi_neck
    global chapi_chapo
    global words_zone
    root_tk=TK.Tk()
    root_tk.title("Chap0")
    c=TK.Canvas(root_tk, height=height, width=width)
    c.pack()

    # Let's draw Chapi !
    chapi_body, chapi_eye, chapi_pupil, chapi_mouth, chapi_neck, chapi_chapo=stamp(False, True)
    words_zone=c.create_text(200, 280, text="")

def character_1():
    global chapi_body
    global chapi_eye
    global chapi_pupil
    global chapi_mouth
    global chapi_neck
    global chapi_chapo

def set_hat_color(color):
    """Change color of the hat"""
    _verify()
    c.itemconfig(chapi_chapo, fill=color)#Changement de chapo !
        

def open_mouth():
    """Open mouth of character"""
    _verify()
    c.itemconfig(chapi_mouth, fill="black")#HAAAAAAAAAAAAAAAAAAAAAAAAAAA

def close_mouth():
    """Close mouth of character"""
    _verify()
    c.itemconfig(chapi_mouth, fill="green")#MMMMMMMMMMMMMMMMMMMMMMMMMMMH

def giveback_hat():
    """Show the hat"""
    _verify()
    c.itemconfig(chapi_chapo, state="normal")#J'ai mon chapo à moi !

def take_hat():
    """Hide the hat"""
    _verify()
    c.itemconfig(chapi_chapo, state="hidden")#Rends moi mon chapo !
    
def message(message):
    """Show a message"""
    _verify()
    c.itemconfig(words_zone, text=message)#Crache le morceau !
    update()

def button(text, command):
    """Create a button, bind click to [command] and return an object of this button """
    _verify()
    btn=TK.Button(root_tk, text=text, command=command)
    btn.pack()
    return btn

def blink():
    """Blink the eye"""
    _verify()
    close_eye()
    update()
    sleep(0.1)
    open_eye()
    update()
    sleep(0.1)

def move(x, y):
    """Move the character by [x, y]"""
    _verify()
    c.move(chapi_body, x, y)
    c.move(chapi_eye, x, y)
    c.move(chapi_pupil, x, y)
    c.move(chapi_mouth, x, y)
    c.move(chapi_neck, x, y)
    c.move(chapi_chapo, x, y)

def move_message(x, y):
    """Move the message zone by [x, y]"""
    _verify()
    c.move(words_zone, x, y)

def bind(key, command):
    """Bind (key) to (command)"""
    _verify()
    try:
        c.bind_all(key, command)
    except:
        raise ChapoError("Invalid event '%s'"%key)

    

def music(file):
    """Play music"""
    out=run(["play", file], stdout=PIPE)
    return out
    
def set_fullscreen(value=True):
    """if (value)=True, put your window on fullscreen;Else, put your window in normal (not on fullscreen)"""
    _verify()
    root_tk.attributes('-fullscreen', value)

def mouse_coords():
    """Return mouse coordinates"""
    _verify()
    return root_tk.winfo_pointerxy()

def set_background(color):
    """Change colour of background"""
    _verify()
    try:
        root_tk["bg"]=color
        c.configure(bg=color)
    except:
        raise ChapoError("Invalid color '%s'"%color)

def destroy():
    """Destroy your window"""
    _verify()
    global root_tk
    root_tk.destroy()
    del root_tk

def update():
    """Update window"""
    _verify()
    root_tk.update()

def reset():
    """Reset window"""
    kill_window()
    init()

def demo():
    """Lechapo-lib demo"""
    kill_window()
    init()
    set_background("light pink")
    message("Hello !")
    deroule("My name is Chapi!", 0.1)
    sleep(1)
    message("Look what I can do !")
    sleep(0.5)
    for i in range(5):
        blink()
        sleep(0.2)
    message("")
    for x in range(3):
        update()
        sleep(1)
        set_hat_color("red")
        update()
        sleep(1)
        set_hat_color("blue")
    for x in range(100):
        move(5, 0)
        update()
        sleep(0.1)

def kill_window():
    """Kill window if it was destroyed by "X" button"""
    global root_tk
    try:
        root_tk.destroy()
    except:
        raise ChapoError("Window is destroyed")
    del root_tk

def stamp(addtostamps=True, makeVirtuals=False):
    """Stamp character and return the stamp.If addtostamps=True, the stamp is add to "le_chapo_lib.stamps\""""
    _verify()
    global stamps
    chapi_body=c.create_oval(100, 150, 300, 250, fill="green") #chapi_body
    chapi_eye=c.create_oval(170, 70, 230, 130, fill="white")#chapi_eye
    chapi_pupil=c.create_oval(190, 90, 210, 110, fill="black")#chapi_pupil
    chapi_mouth=c.create_oval(150, 220, 250, 240, fill="red")#chapi_mouth
    chapi_neck=c.create_line(200, 150, 200, 130) #chapi_neck
    chapi_chapo=c.create_polygon(180, 75, 220, 75, 200, 20, fill="blue")#chapi_chapo
    thisstamp=chapi_body, chapi_eye, chapi_pupil, chapi_mouth, chapi_neck, chapi_chapo
    if makeVirtuals:
        tomake_virtuals=[(chapi_body, 100, 200), (chapi_eye, 60, 60), (chapi_chapo, 55, 40)]
        virtuals=make_virtuals(tomake_virtuals)
    #Fin du dessin
    if addtostamps:
        stamps.append(thisstamp)
    return thisstamp

def clearstamps():
    """Clear all stamps"""
    global stamps
    for x in stamps:
        for y in x:
            c.delete(y)
    update()
    stamps=[]

def _change_state(spstate):
    """System function. Change the "state" attribute of the character"""
    _verify()
    c.itemconfig(chapi_body , state=spstate)
    c.itemconfig(chapi_neck , state=spstate)
    c.itemconfig(chapi_chapo , state=spstate)
    c.itemconfig(chapi_eye , state=spstate)
    c.itemconfig(chapi_pupil , state=spstate)
    c.itemconfig(chapi_mouth , state=spstate)

def hide():
    """Hide the character"""
    _verify()
    _change_state("hidden")

def show():
    """Show the character"""
    _verify()
    _change_state("normal")

def set_title(title):
    """Set window title"""
    _verify()
    root_tk.title(title)

def popup_yesno(a, b):
    """Show a popup window (yes or no)"""
    _verify()
    return TKBOX.askyesno(a, b)

def popup(a, b):
    """Show a popup window (info)"""
    _verify()
    TKBOX.showinfo(a, b)

def popup_okcancel(a, b):
    """Show a popup window (OK or Cancel)"""
    _verify()
    return TKBOX.askokcancel(a, b)

def popup_yesynocancel(a, b):
    """Show a popup window (OK or Cancel)"""
    _verify()
    return TKBOX.askyesnocancel(a, b)

def nothing():
    """This function do...nothing !!! It's very useful in default function assignements !!"""
    pass

def deroule(text, timeS, call1=nothing, call2=nothing):
    """Show text progressively"""
    _verify()
    m1=""
    tocall=True
    for x in text:
        if tocall:
            call1()
        else:
            call2()
        m1+=x
        message(m1)
        update()
        sleep(timeS)
        tocall=not tocall

def close_eye():
    """Close Chapi's eye"""
    _verify()
    c.itemconfig(chapi_eye, fill="green")
    c.itemconfig(chapi_pupil, state=TK.HIDDEN)

def open_eye():
    """Open Chapi's eye"""
    _verify()
    c.itemconfig(chapi_eye, fill="white")
    c.itemconfig(chapi_pupil, state=TK.NORMAL)

def is_on_collide(sp, sprites=virtuals):
    for sprite in sprites:
        if _collide(sprite, sp):
            return True
    return False

def make_virtuals(virtuals):
    sprites=[]
    for id, height, width in virtuals:
        brut=_Brut(height, width)
        sprite=_Virtual(id, brut, "polygon")
        sprites.append(sprite)
    return sprites

def mainloop():
    """Run the game's mainloop"""
    _verify()
    root_tk.mainloop()