# A Floater is Prey; it updates by moving mostly in
#   a straight line, but with random changes to its
#   angle and speed, and displays as ufo.gif (whose
#   dimensions (width and height) are computed by
#   calling .width()/.height() on the PhotoImage


from PIL.ImageTk import PhotoImage
from prey import Prey
from random import random
from random import randrange

class Floater(Prey):
    radiusc = 5
    def __init__(self,x,y):
        self.randomize_angle()
        self.pic = PhotoImage(file = 'ufo.gif')
        Prey.__init__(self,x,y,self.pic.width(),self.pic.height(),self._angle,5)
                
    def update(self,model):
        con = randrange(1,100)
        if con <= 30:
            change = randrange(-500,500)/1000 + self._speed
            if 3 < change < 7:
                self._speed = change
            change = randrange(-500,500)/1000
            self._angle += change
        else:
            pass        
        self.move()
    
    def display(self,the_canvas):
        the_canvas.create_image(*self.get_location(),image=self.pic) 