class cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("hello i am a cat and my name is ",self.name , "and my age is ",self.age)

    def sound(self):
        print("cats meows")

class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def intro(self):
        print("hello i am a dog and my name is ",self.name , "and my age is ",self.age)

    def sound(self):
        print("dogs barks")

cat1=cat("pussy",2)
dog1=dog("bunny",1)

for animal in (cat1,dog1):
     animal.intro()
     animal.sound()
