def myFun(arg1, **kwargs):
   for key, value in kwargs.items():
      print("hello","%s : %s" % (key, value))

myFun("hello",first='Himani', mid='Sharma', last='Vashisht')