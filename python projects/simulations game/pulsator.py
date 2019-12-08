# A Pulsator is a Black_Hole; it updates as a Black_Hole
#   does, but also by growing/shrinking depending on
#   whether or not it eats Prey (and removing itself from
#   the simulation if its dimension becomes 0), and displays
#   as a Black_Hole but with varying dimensions


from blackhole import Black_Hole


class Pulsator(Black_Hole): 
    ecounter = 30
    def __init__(self,x,y):
        Black_Hole.__init__(self,x,y)
        self.counterc = 30
        
    def update(self, model):
        self.counterc -= 1
        eaten = len(Black_Hole.update(self,model))
        if eaten != 0:
            self.counterc = Pulsator.ecounter
            self.change_dimension(eaten,eaten)
        if self.counterc == 0:
            self.change_dimension(-1,-1)
            if self._height == 0 and self._width == 0:
                model.remove(self)
            self.counterc = Pulsator.ecounter
            
            