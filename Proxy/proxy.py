"""Proxy (Structural)

avoid using extra recources with a interface class

"""


class Db:
    def work(self):
        print("You can work with database ..")


class Proxy:
    _admin_password = "admin"

    def check_admin(self, password):
        if password == self._admin_password:
            d1 = Db()
            d1.work()
        else:
            print("you're not admin, so you can't work with database ..")


p = Proxy()
p.check_admin("admin")
