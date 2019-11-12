# Submitter: cslam2(Lam, Christopher)

from goody import type_as_str
from math import sqrt

class Interval:
    def __init__(self, mini, maxi):
        self.min = mini
        self.max = maxi
    
    @staticmethod
    def min_max(mini, maxi = None):
        assert type(mini) in (float, int), 'min value is not of the float or int type'
        assert type(maxi) in(float,int) or maxi == None, 'max value is not of the float or int type'
        if maxi == None:
            return Interval(mini,mini)
        assert mini <= maxi, 'min value is greater than the max value'
        return Interval(mini,maxi)
    
    @staticmethod
    def mid_err (midn, error = 0):
        assert type(midn) in (float, int), 'min value is not of the float or int type'
        assert type(error) in (float, int) and error >= 0, 'error is not of the float or int type or error is negative'
        return Interval(midn-error,midn+error)
    
    def best(self):
        return (self.min + self.max)/2
    
    def error(self):
        return abs(Interval.best(self)-self.min)
    
    def relative_error(self):
        return  abs((Interval.error(self)/Interval.best(self))*100)

    def __repr__ (self):
        return 'Interval('+str(self.min)+','+str(self.max)+')'
    
    def __str__(self):
        return str(Interval.best(self))+'(+/-'+str(Interval.error(self))+')'
    
    def __bool__(self):
        return Interval.error(self) != 0
    
    def __pos__(self):
        return Interval(self.min,self.max)
    
    def __neg__(self):
        return Interval(-self.min,-self.max)
    
    def __add__(self,right):
        if type(right) not in (Interval, int, float):
            return NotImplemented
        elif type(right) == Interval:
            return Interval(self.min+right.min,self.max+right.max)
        elif type(right) in (float, int):
            return Interval(self.min+right,self.max+right)

    def __radd__(self,left):
        if type(left) not in (Interval, int, float):
            return NotImplemented
        elif type(left) == Interval:
            return Interval(self.min+left.min,self.max+left.max)
        elif type(left) in (float, int):
            return Interval(self.min+left,self.max+left)
    
    def __sub__(self,right):
        if type(right) not in (Interval, int, float):
            return NotImplemented
        elif type(right) == Interval:
            return Interval(self.min-right.max,self.max-right.min)
        elif type(right) in (float, int):
            return Interval(self.min-right,self.max-right)

    def __rsub__(self,left):
        if type(left) not in (Interval, int, float):
            return NotImplemented
        elif type(left) == Interval:
            return Interval(left.min-self.max,left.max-self.min)
        elif type(left) in (float, int):
            return Interval(left-self.max,left-self.min)
     
    def __mul__(self,right):
        if type(right) not in (Interval, int, float):
            return NotImplemented
        elif type(right) == Interval:
            sortvalues = sorted([self.max*right.max, self.max*right.min, self.min*right.min, self.min*right.max])
            return Interval(sortvalues[0], sortvalues[3])
        elif type(right) in (float, int):
            return Interval(self.min*right,self.max*right)

    def __rmul__(self,left):
        if type(left) not in (Interval, int, float):
            return NotImplemented
        elif type(left) == Interval:
            sortvalues = sorted([self.max*left.max, self.max*left.min, self.min*left.min, self.min*left.max])
            return Interval(sortvalues[0], sortvalues[3])
        elif type(left) in (float, int):
            return Interval(self.min*left,self.max*left)
    
    def __truediv__(self,right):
        if type(right) not in (Interval, int, float):
            return NotImplemented
        elif type(right) == Interval:
            if right.min <= 0 and 0 <= right.max:
                raise ZeroDivisionError
            sortvalues = sorted([self.max/right.max, self.max/right.min, self.min/right.min, self.min/right.max])
            return Interval(sortvalues[0], sortvalues[3])
        elif type(right) in (float, int):
            return Interval(self.min/right,self.max/right)

    def __rtruediv__(self,left):
        if type(left) not in (Interval, int, float):
            return NotImplemented
        elif type(left) == Interval:
            if self.min <= 0 and 0 <= self.max:
                raise ZeroDivisionError
            sortvalues = sorted([left.max/self.max, left.max/self.min, left.min/self.min, left.min/self.max])
            return Interval(sortvalues[0], sortvalues[3])
        elif type(left) in (float, int):
            if self.min <= 0 and 0 <= self.max:
                raise ZeroDivisionError
            return Interval(left/self.max,left/self.min) 

    def __pow__(self, right):
        if type(right) != int:
            return NotImplemented
        if right > 0:
            mini, maxi = self.min**right, self.max**right
        elif right == 0:
            mini, maxi = 1.0, 1.0
        elif right < 0:
            mini, maxi = self.max**right, self.min**right
        return Interval(mini, maxi)
        
    def __eq__(self, right):
        if type(right) not in (float, int, Interval):
            return NotImplemented
        if type(right) == Interval:
            return (self.min == right.min) and (self.max == self.max)
        if type(right) in (float, int):
            return (self.min == right) and (self.max==right)
    
    @staticmethod
    
    def _relhelp(left, right):
        if Interval.compare_mode == 'liberal':
            bv1 = Interval.best(left)
            if type(right) == Interval:
                bv2 = Interval.best(right)
            elif type(right) in [float,int]:
                bv2 = right
            else:
                return NotImplemented
            return [bv1,bv2]
        if Interval.compare_mode == 'conservative':
            bv1 = left.max
            if type(right) == Interval:
                bv2 = right.min
            elif type(right) in [float,int]:
                bv2 = right
            else:
                return NotImplemented
            return [bv1,bv2]
            
    def __lt__(self,right):
        assert('compare_mode' in Interval.__dict__), 'compare_mode not found'
        assert(Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'), 'compare_mode not equal to liberal or conservative'
        relres = Interval._relhelp(self,right)
        return relres[0] < relres[1]
        
    def __le__(self,right):
        assert('compare_mode' in Interval.__dict__), 'compare_mode not found'
        assert(Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'), 'compare_mode not equal to liberal or conservative'
        relres = Interval._relhelp(self,right)
        return relres[0] <= relres[1]

    def __abs__(self):
        if self.min >= 0 and self.max >= 0:
            return Interval(self.min,self.max)
        elif self.min < 0 and self.max > 0:
            return Interval(0.0,self.max)
        elif self.min < 0 and self.max < 0:
            absvalues = sorted([abs(self.min),abs(self.max)])
            return Interval(absvalues[0],absvalues[1])
    
    def sqrt(self):
        if self.min < 0 or self.max < 0:
            raise ValueError
        return Interval(sqrt(self.min),sqrt(self.max))
        
    def __setattr__(self, name, value):
        if name == 'min' or name == 'max':
            if name not in self.__dict__:
                self.__dict__[name] = value
            else:
                raise AssertionError
        else:
            raise AssertionError
            
if __name__ == '__main__':
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    

    import driver    
    driver.default_file_name = 'bscp22F19.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
