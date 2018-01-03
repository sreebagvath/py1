import datetime
class People(object):
    def __init__(self,name):
        self.name = name
        self.lastname = name.split()[-1]
        self.birthday = None
    def getlastname(self):
        return self.lastname
    def setbirthday(self,month,day,year):
        #sets self's birthday to birthdate
        self.birthday = datetime.date(year,month,day)
    def getage(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today()-self.birthday).days
    def __str__(self):
        return "people: "+ str(self.name) +','+ str(self.birthday) 

class NTUPeople(People):
    nextid = 0
    def __init__(self,name):
        People.__init__(self,name)
        self.id = NTUPeople.nextid
        NTUPeople.nextid +=1
    def getid(self):
        return self.id
    def speak(self,quote):
        return "please, "+ str(quote)

class Student(NTUPeople):
    pass

class UG(Student):
    def __init__(self,name,year):
        NTUPeople.__init__(self,name)
        self.year = year
    def getyear(self):
        return self.year
    def speak(self,quote):
        return NTUPeople.speak(self,"BRO, " + quote)

class PG(Student):
    pass

class TransferStudent(Student):
    pass





p1 = People("Tom Cruise")
p2 = People("Brad Pitt")
p3 = People("Ajith")
p4 = People("Sree Bagvath")

s1 = NTUPeople("bob")
t1 = UG("bob",2013)
