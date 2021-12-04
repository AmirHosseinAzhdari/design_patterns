"""
Decorator()
    decorator pattern != python decorator
    
Add properties for an object -> we can use python decorator
"""

class Article:
    def show(self):
        print("All articles .. ")
        

class login:
    def check_login(self, name, password):
        if name == "admin" and password == "123":
            return True
        
        
def outor_login(func):
    def inner_login():
        name = input("Enter your name : ")
        password = input("Enter your password : ")
        l = login()
        result = l.check_login(name, password)
        if result:
            func()
        else: 
            print("Wrong user or password")
    return inner_login

@outor_login         
def show_all_articles():
    a = Article()
    a.show()
    
show_all_articles()