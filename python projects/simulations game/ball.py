# A Ball is Prey; it updates by moving in a straight
#   line and displays as blue circle with a radius
#   of 5 (width/height 10).


from prey import Prey


class Ball(Prey): 
    radiusc = 5
    def __init__(self,x,y):
        self.randomize_angle()
        Prey.__init__(self,x,y,Ball.radiusc*2,Ball.radiusc*2,self._angle,5)
    
    def update(self,model):
        self.move()
    
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radiusc      , self._y-Ball.radiusc,
                                self._x+Ball.radiusc, self._y+Ball.radiusc,
                                fill='blue')