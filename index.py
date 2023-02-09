#! First exercise
#!class Car:
#!    def __init__(self, name, color, speed):
#!        self.name = name
#!        self.color = color
#!        self.speed = speed
#!
#!    def get_info(self):
#!        return f'{self.color} rangli {self.name} mashinasining tezligi {self.speed} ga teng.'


#!car = Car("Lasetti", "oq", 220)
#!print(car.get_info())

#! ***************************************************

#* Second exercise
class Phone:
    def __init__(self, name, color, price):
        self._name = name
        self._color = color
        self._price = price

    @property
    def Name(self):
        return self._name

    @Name.setter
    def newName(self, name):
        self._name = name

    @property
    def Color(self):
        return self._color

    @Name.setter
    def newColor(self, color):
        self._color = color

    @property
    def Price(self):
        return self._price

    @Price.setter
    def newPrice(self, price):
        self._price = price

    def get_information(self):
        return f" Name: {self._name}\n Color: {self._color}\n Price: {self._price}"


phone = Phone("Realme", "qora", "200$")
print(phone.Name)
print(phone.Color)
print(phone.Price)
print(phone.get_information())

phone.newPrice = "300$"
phone.newColor = "oq"
phone.newName = "redmi"
print(phone.get_information())
