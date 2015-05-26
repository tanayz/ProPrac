class tanay:
    salary=126500
    papers=1
    def __init__(self,salary,papers):
        print 'at start'
    def getattr(self):
        return tanay.salary

class kutti(tanay):
    def __init__(self):
        print 'nothing'
    def salval(self):
        return tanay.salary*0.006


am=kutti()
#print 'papers:',tan.papers,'salary:',tan.salary
#print tan.getattr()
print 'Kuttas salary:',am.salval()

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2

class JustCounter:
   __secretCount = 0
  
   def count(self):
      self.__secretCount += 1
      print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
#print counter.__secretCount
print counter._JustCounter__secretCount