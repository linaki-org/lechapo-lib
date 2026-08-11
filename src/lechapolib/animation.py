"""Le_chapo_lib.animation module can read and create THA animations files."""
import tkinter as TK
import pickle
class HatError(Exception):
    pass
class Tha:
    def __init__(self, tha):
        try:
            file=open(tha, 'rb')
            thaCTN=pickle.load(file)
            file.close()
        except:
            raise HatError("No such file or directory %s"%tha)
        self.IMGlist=[]
        for x in thaCTN:
             template=open("template.gif", 'wb')
             template.write(x)
             template.close()
             img=TK.PhotoImage(file="template.gif")
             self.IMGlist.append(img)
    def read(self, le_chapo_lib, x, y):
        img=le_chapo_lib.c.create_image(x, y, anchor="nw", image=self.IMGlist[0])
        le_chapo_lib.update()

        for x in self.IMGlist:
            le_chapo_lib.c.itemconfig(img, image=x)
            le_chapo_lib.update()
            le_chapo_lib.sleep(0.1)
        le_chapo_lib.c.delete(img)
        
