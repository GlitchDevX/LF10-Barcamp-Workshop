from typing import Literal


type Food = Literal["meat", "vegetables", "fish food", "seeds"]

class Cat:
    def feed(self, food: Food):
        if food == "meat":
            print("cat ate the food 😺")

    def pet(self):
        print("rrrrrrr 😸")

class Dog:
    def feed(self, food: Food):
        if food == "meat" or food == "vegetables":
            print("dog ate the food 🐶")

    def pet(self):
        print("Hooooonk-sigh 🐾")

class Hamster:
    def feed(self, food: Food):
        if food == "seeds" or food == "vegetables":
            print("hamster ate the food 🌿")

    def pet(self):
        print("Whirrr 🐹")

class Fish:
    def feed(self, food: Food):
        if food == "fish food":
            print("fish ate the food 🐟")

    def pet(self):
        print("blub blub 💧")
