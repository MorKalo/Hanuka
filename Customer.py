class Customer():
    def __init__(self, id, lname, fname, address, mobile):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.address=address
        self.mobile=mobile

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

