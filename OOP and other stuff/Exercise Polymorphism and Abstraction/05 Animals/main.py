from project.dog import Dog
from project.tomcat import Tomcat

if __name__ == "__main__":
    dog = Dog("Rocky", 3, "Male")
    print(dog.make_sound())
    print(dog)
    tomcat = Tomcat("Tom", 6)
    print(tomcat.make_sound())
    print(tomcat)
