# Black_Hole is singly derived from Simulton, updating by finding+removing
#   any Prey whose center is contained within its radius
#  (returning a set of all eaten simultons), and
#   displays as a black circle with a radius of 10
#   (width/height 20).
# Calling get_dimension for the width/height (for
#   containment and displaying) will facilitate
#   inheritance in Pulsator and Hunter

from simulton import Simulton
from prey import Prey

class Black_Hole(Simulton):
    radiusc = 10
    def __init__(self,x,y):
        Simulton.__init__(self,x,y,Black_Hole.radiusc*2,Black_Hole.radiusc*2)
    
    def contains(self, xy):
        return self.distance(xy) < self._width/2
        
    def update(self,model):
        simseaten = set()
        simslist = list(model.find(lambda c : isinstance(c,Prey) and self.contains((c._x,c._y))))
        for s in simslist:
            model.remove(s)
            simseaten.add(s)
        return simseaten
        
    def display(self,canvas):
        canvas.create_oval(self._x-self._width/2, self._y-self._height/2,
                                self._x+self._width/2, self._y+self._height/2,
                                fill='black')
        