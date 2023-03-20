#Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto.
# Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko
# litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen,
# huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa
# oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja
# yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja
# ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat.
import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        self.km_counter = 0

    def acceleration(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed <=0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours
        self.km_counter += self.maximum_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed,kilowatt_hour):
        self.kilowatt_hour = kilowatt_hour
        super().__init__(registration_number,maximum_speed)


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        self.tank_volume = tank_volume
        super().__init__(registration_number, maximum_speed)




electric_car = ElectricCar("ABC-15", 180, 52.5)
gasoline_car = GasolineCar("ACD-123", 165, 32.3)



electric_car.drive(3)
gasoline_car.drive(3)

print(f"Electric car km counter: {electric_car.km_counter} km")
print(f"Gasoline car km counter: {gasoline_car.km_counter} km")