"""
    Creational:
        Factory Method:
            3 component => 1.Creator, 2.Product, 3.Client
"""
class File:
    def __init__(self, name, format):
        self.name = name
        self.format = format
        

"""
    The edit method in WrongB class does a lot of work in class B, and that's wrong.
    Also, if we want to add another format to the file, we have to add another 
    condition to the edit method, which is not true.
    To solve these problems, we can use the factory design Pattern, 
    which puts code changes in the right_factory file
"""
class WrongB:
    def edit(self, file):
        if file.format == "json":
            print(f"Editing json file ... {file.name}")
        elif file.format == "xml":
            print(f"Editing xml file ... {file.name}")
        else:
            raise ValueError(f"Invalid format for file {file.name}.{file.format}")
        
        
"""
If we want to work more principledly, an example is given in the right_factory file
"""
class RightB:
    
    def edit(self, file): # Client
        edit = self._get_edit(file)
        return edit(file)
    
    def _get_edit(self, file): # Creator
        if file.format == "json":
            return self.edit_json(file)
        elif file.format == "xml":
            return self.edit_xml(file)
        else:
            raise ValueError(f"Invalid format for file {file.name}.{file.format}")
    
    def edit_json(self, file): # Product
        print(f"Editing json file ... {file.name}")
        
    def edit_xml(self, file): # Product
        print(f"Editing xml file ... {file.name}")
    
        
a1 = File("first", "json")
b1 = RightB().edit(a1)