import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.DEBUG, filename='class_demon.log', format='%(asctime)s - %(levelname)s - %(message)s')

'''demonstrate use of abstract class, multiple inheritance, and decorator'''


class Animal(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        logging.info(f'Creating {self.name}')

    @abstractmethod
    def abstract_method(self):
        pass

class Dog(Animal):
    def abstract_method(self):
        return 'i am a dog from abstract method'

class Cat(Animal):
    def abstract_method(self):
        return 'i am a cat from abstract method'

class Fish(Animal):
    def abstract_method(self):
        return 'i am a fish from abstract method'

class DogCatFish(Dog, Cat, Fish):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        logging.info(f'Creating {self.name}')
        print(Dog.abstract_method(self))
        print(Cat.abstract_method(self))
        print(Fish.abstract_method(self))

if __name__ == "__main__":
    logging.info('calling DogCatFish')
    dog_cat_fish = DogCatFish('DogCatFish')
