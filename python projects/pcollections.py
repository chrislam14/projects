import re, traceback, keyword
from keyword import kwlist

def unique(iterable):
    iterated = set()
    for i in iterable:
        if i not in iterated:
            iterated.add(i)
            yield i

def pnamedtuple( type_name,  field_names,  mutable= False, defaults={}):
    def show_listing(s):
        for line_number, line_text in enumerate( s.split('\n'),1 ):
            print(f' {line_number: >3} {line_text.rstrip()}')
    
    pattern = r"^([A-Za-z])([A-z\_0-9])*$"
    m = re.match(pattern, str(type_name))
    if not m or type_name in kwlist:
        raise SyntaxError ('type_name is not a legal name or is already a Python keyword')
    if type(field_names) not in (list, str):
        raise SyntaxError ('field_names is not a list or a string')
    elif type(field_names) == list:
        fieldnames = [fn for fn in unique(field_names)]
        for fn in fieldnames:
            m = re.match(pattern, fn)
            if not m or fn in kwlist:
                raise SyntaxError ('one or more field_name is not a legal name')
    else:
        if ',' in field_names:
            fieldnames = ''.join(field_names.split()).split(',')
        else:
            fieldnames = field_names.split()
        fieldnames = [fn for fn in unique(fieldnames)]
        for fn in fieldnames:
            m = re.match(pattern, fn)
            if not m or fn in kwlist:
                raise SyntaxError ('one or more field_name is not a legal name')
    for fn in defaults:
        if fn not in fieldnames:
            raise SyntaxError ('defaults key not in field_names')
    class_template = '''
class {tn}:
    _fields = {fn_list}
    _mutable = {mutable}
        
    def __init__(self,*args,**kargs):
        for fn, arg in zip({fn_list}, args):
            self.__dict__[fn] = arg
        for karg in kargs:
            if karg in self._fields:
                self.__dict__[karg] = kargs[karg]
    
    def __repr__(self):
        return '{tn}({reprargs})'.format({reprformat})
    {defget}
    def __getitem__(self, index):
        if type(index) == int:
            if index in range(len(self._fields)):
                return self.__dict__[self._fields[index]]
            raise IndexError
        elif type(index) == str:
            if index in self._fields:
                return self.__dict__[index]
            raise IndexError
        else:
            raise IndexError
    def __eq__(self,right):
        if type(right) == {tn}:
            for fn in self._fields:
                if fn in right._fields:                    
                    if self.__getitem__(fn) == right.__getitem__(fn):
                        pass
                    else:
                        return False
                else:
                    return False
        else:
            return False
        return True
    def _asdict(self):
        dictres = dict()
        for fn in self._fields:
            dictres[fn] = self.__getitem__(fn)
        return dictres
        
    def _make(iteri):
        resstr = ','.join([str(fn)+'='+str(args) for fn, args in zip({fn_list},iteri)])
        return '{tn}('+resstr+')'
    
    def _replace(self,**kargs):
        for karg in kargs:
            if karg not in self._fields:
                raise TypeError
        if self._mutable:
             for k,i in kargs.items():
                self.__dict__[k] = i
        else:
            for fn in self._fields:
                if fn not in kargs:
                    kargs[fn] = self.__getitem__(fn)
            return {tn}(**kargs)
        
    def __setattr__(self, name, value):
        if {tn}.__dict__['_mutable'] == False:
            raise AttributeError
        self.__dict__[name] = value
    '''
    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_definition = class_template.format(
        tn = type_name,
        fn_list = fieldnames,
        mutable = mutable,
        reprargs = ','.join([n+'={'+n+'}' for n in fieldnames]),
        reprformat = ','.join([n+'=self.'+n for n in fieldnames]),
        defget = '\n    '.join(['def get_'+n+'(self):\n\t      return self.'+n for n in fieldnames])
        )
    # When debugging, uncomment following line to show source code for the class
    # show_listing(class_definition)

    # Execute this class_definition, a str, in a local name space; then bind the
    #   the source_code attribute to class_definition; after try/except return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error

    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )    
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):        
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test pnamedtuple below in script with Point = pnamedtuple('Point','x,y')

    #driver tests
    import driver
    driver.default_file_name = 'bscp3F19.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
