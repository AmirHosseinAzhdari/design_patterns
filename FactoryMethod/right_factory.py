"""
    Creational:
        Factory Method:
            3 component => 1.Product, 2.Creator, 3.Client
"""

from abc import ABC, abstractclassmethod

# Product -------------------------------------------------

class Product(ABC):
    @abstractclassmethod
    def edit(self):
        pass
    
    
class Json(Product):
    def edit(self):
        return "Editing json file ..."
    
    
class Xml(Product):
    def edit(self):
        return "Editing xml file ..."
    
class Pdf(Product):
    def edit(self):
        return "Editing pdf file ..."

# Creator -------------------------------------------------

class Creator(ABC):
    @abstractclassmethod
    def make(self):
        pass
    
    def call_edit(self):
        product = self.make()
        res = product.edit()
        return res
    
class JsonCreator(Creator):
    def make(self):
        return Json()
    
class XmlCreator(Creator):
    def make(self):
        return Xml()
    
class PdfCreator(Creator):
    def make(self):
        return Pdf()

# Client --------------------------------------------------

def client(format: Creator):
    return format.call_edit()

# --------------------------------------------------------

print(client(JsonCreator()))
print(client(XmlCreator()))
print(client(PdfCreator()))