# Submitter: cslam2(Lam, Christopher)

from collections import defaultdict
from goody import type_as_str
from pip._internal.utils.outdated import SELFCHECK_DATE_FMT

class Bag:

    def __init__(self, bag = dict()):
        bags = {}
        if len(bag) != 0:
            for b in bag:
                bags.setdefault(b,0)
                bags[b] += 1
        self.bag = bags

    
    def __repr__(self):
        return 'Bag('+str([str(b) for b in self.bag for i in range(self.bag[b])])+')'

    def __str__(self):
        return 'Bag('+', '.join(str(b)+'['+str(i)+']' for b,i in self.bag.items())+')'    
    
    def __len__(self):
        return sum([n[1] for n in self.bag.items()])
    
    def unique(self):
        return len(self.bag)
    
    def __contains__(self, item):
        return item in self.bag
    
    def count(self, item):
        if item in self.bag:
            return self.bag[item]
        return 0
    
    def add(self,item):
        if item in self.bag:
            self.bag[item] += 1
        else:
            self.bag[item] = 1
    
    def __add__(self,right):
        if type(right) != Bag:
            raise TypeError
        newlist = [b for b in self.bag for i in range(self.bag[b])]
        newlist.extend([b for b in right.bag for i in range(right.bag[b])])
        return Bag(newlist)
        
    def remove (self,item):
        if item not in self.bag:
            raise ValueError (item, 'could not be removed')
        self.bag[item] -= 1
        if self.bag[item] == 0:
            self.bag.pop(item)
            
    def __eq__(self,right):
        if type(right) != Bag:
            return False
        return self.bag.items() == right.bag.items()
    
    def __iter__(self):
        def gen(bags):
            for b in bags:
                for i in range(b[1]):
                    yield b[0]
        return gen(list(self.bag.items()))
    
    
if __name__ == '__main__':
    #Put your own test code here to test Bag before doing bsc tests

    print('Start simple testing')

    import driver
    driver.default_file_name = 'bscp21F19.txt'
#     driver.default_show_exception =True
#     driver.default_show_exception_message =True
#     driver.default_show_traceback =True
    driver.driver()
