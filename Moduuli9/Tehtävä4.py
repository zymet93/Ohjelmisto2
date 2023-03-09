#Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu
# kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan
# seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:
#Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
#Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
#Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.


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
        elif new_speed <=0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self,hours):
        self.travelled_distance += self.current_speed * hours

cars_list=[]

for i in range(10):
    cars_list.append(Car(f'abc-{i}', random.randint(100, 200)))

travMax = 0
while travMax < 10000:
    for raceCar in cars_list:
        raceCar.acceleration(random.randint(-10, 15))
        raceCar.drive(1)
        travMax = max(raceCar.travelled_distance, travMax)
for raceCar in cars_list:
    print(f"{raceCar.registration_number:6s} : {raceCar.maximum_speed} km/h, {raceCar.travelled_distance} km")
print(f"the winner was able to travel {travMax}")


