class myClass:
     __privateVar = 900;
     
     def __privateMeth(self):
        print("I am in a class that has a private method.I am in it.")

     def hello(self):
         print("Private Variable value is:", myClass.__privateVar)

foo = myClass()
foo.hello()
foo.__privateMeth