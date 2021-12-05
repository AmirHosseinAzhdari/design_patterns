"""
    Facade(Structural)
        Reduce complexity in code
"""

class Raw:
    def raw(self):
        print("Buying raw foods from market ..")
        
        
class Transfer:
    def transfer(self):
        print("Transfering raw foods to resturanst ..")
        
        
class Cook:
    def cook(self):
        print("Cooking raw foods ..")
        

class Serve:
    def serve(self):
        print("Serving foods to clients")


class Resturant:
    def get(self):
        r = Raw()
        r.raw()
        
        t = Transfer()
        t.transfer()
        
        c = Cook()
        c.cook()
        
        s = Serve()
        s.serve()
        

def order():
    i = Resturant()
    i.get()
    
order()