#Tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi,
# pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän
# ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:tunti_kuluu, joka toteuttaa
# aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen
# ja kutsuu kullekin autolle kulje-metodia.
#tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
#kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun
# kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
#Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle
# annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla
# toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi.
# Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä
# kertaalleen sen jälkeen, kun kilpailu on päättynyt.

import random


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def acceleration(self, speed_change):
        new_speed = self.current_speed + speed_change
        if new_speed >= self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif new_speed <= 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, kilometers, car_list):
        self.name = name
        self.kilometers = kilometers
        self.car_list = car_list
#tunnit mennyt
    def hour_passes(self):
        for raceCar in cars_list:
            raceCar.acceleration(random.randint(-10, 15))
            raceCar.drive(1)
#status
    def print_status(self):
        for raceCar in cars_list:
            print(f"{raceCar.registration_number}  Nopeus: {raceCar.maximum_speed} km/h, Liikuttu etäisyys {raceCar.travelled_distance} km")
#kilpailu loppuu
    def race_finished(self):
        travMax = 0
        for car in self.car_list:
            travMax = max(car.travelled_distance, travMax)
        if travMax >= self.kilometers:
            return True
     #voittaja
    def find_winner(self):
        winner = None
        max_distance = 0
        for car in self.car_list:
            if car.travelled_distance > max_distance:
                max_distance = car.travelled_distance
                winner = car
        return winner




cars_list = []

for i in range(10):
    cars_list.append(Car(f'abc-{i}', random.randint(100, 200)))

race = Race('Suuren romurallin', 8000, cars_list)
print()

hour = 0
while race.race_finished() is not True:
    hour +=1
    race.hour_passes()
    if hour % 10 == 0:
        print(f'After {hour} hours:')
        race.print_status()
        print()
print(f'Suuri romuralli päättyi {hour} tunnissa:')
race.print_status()
#Voittaja printti
winner = race.find_winner()
print(f"\n{race.name} Voittaja on {winner.registration_number}! Etäisyydellä {winner.travelled_distance} km")