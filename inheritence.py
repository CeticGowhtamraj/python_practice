class animal:
    def make_sound(self):
        print("This are animals Sounds")
class dog(animal):
    def make_sound(self):
        print("Barks")

class cat(animal):
    def make_sound(self):
        print("meow")
animal=animal()
animal.make_sound()
i=cat()
i.make_sound()
dog=dog()
dog.make_sound()