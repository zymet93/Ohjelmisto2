#Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
# tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja, joka asettaa ominaisuuksista kaksi
# ensin mainittua parametreina saatuihin arvoihin. Uuden auton nopeus
# ja kuljetut matka on asetettava automaattisesti nollaksi.
# Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
# Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.



class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


new_car=Car('abc-123', 70)
print( f"Registration Number: {new_car.registration_number}\nMaximum Speed: {new_car.maximum_speed} km/h" \
               f"\nCurrent Speed: {new_car.current_speed} km/h\nTravelled Distance: {new_car.travelled_distance} km")

"""new_car = Car('abc-123', 142)
new_car.str()"""