#!/usr/bin/env python3

class Animal(object):
    def __init__(self, name):
        self._name = name
    @staticmethod
    def order_animal_food():
        print('ording...')
        print('ok')
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if len(value) > 4:
            self._name = value
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound wang wang wang...')

class Cat(Animal):
    def make_sound(self):
        print(self.get_name() + ' is making sound miu miu miu...')

#dog = Dog('erHa')
#cat = Cat('kittY')
#
#dog.make_sound()
#cat.make_sound()
#dog.set_name('wangcaI')
#cat.set_name('miMi')
#dog.make_sound()
#cat.make_sound()
#
#animals = [Dog('wangcai'), Cat('kitty'), Dog('laifu'), Cat('betty')]
#for animal in animals:
#    animal.make_sound()
#cat = Cat('kit')
print(Animal.order_animal_food())
