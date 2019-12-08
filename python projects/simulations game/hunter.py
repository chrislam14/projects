# Hunter is doubly-derived from the Mobile_Simulton and Pulsator classes:
#   updating/displaying like its Pulsator base, but also moving (either in
#   a straight line or in pursuit of Prey), like its Mobile_Simultion base.


from prey import Prey
from pulsator import Pulsator
from mobilesimulton import Mobile_Simulton
from math import atan2


class Hunter(Pulsator, Mobile_Simulton):
    vision = 200
    def __init__(self,x,y):
        self.randomize_angle()
        Pulsator.__init__(self,x,y)
        Mobile_Simulton.__init__(self,x,y,self.radiusc*2,self.radiusc*2,self._angle,5)

    def update (self,model):
        closestd = Hunter.vision
        closest = None
        for p in model.find(lambda c: isinstance(c,Prey) and self.distance((c._x,c._y)) <= Hunter.vision):
            if self.distance(p.get_location()) < closestd:
                closestd = self.distance(p.get_location())
                closest = p
        if closest != None:
            px, py = closest.get_location()
            sx, sy = self.get_location()
            self.set_angle(atan2(py-sy,px-sx))
            
        Pulsator.update(self,model)
        self.move()
            
                
        