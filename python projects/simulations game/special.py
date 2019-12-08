from ball import Ball
'''
My special is a unique ball that is pink and that gets faster as it bounces off of walls the max speed is 30
'''

class Special(Ball):
    
    def bounce(self,barrier_angle):
        if self._speed != 30:
            self.set_speed(self._speed+1)
        self._angle = 2*barrier_angle - self._angle
    
    def display(self,canvas):
        canvas.create_oval(self._x-Ball.radiusc      , self._y-Ball.radiusc,
                                self._x+Ball.radiusc, self._y+Ball.radiusc,
                                fill='pink')
