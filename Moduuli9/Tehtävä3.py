#Laajenna ohjelmaa siten, että mukana on kulje-metodi, joka saa parametrinaan tuntimäärän. Metodi
#kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla annetussa tuntimäärässä edennyt.
#Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h. Metodikutsu auto.kulje(1.5)
#kasvattaa kuljetun matkan lukemaan 2090 km.


class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 2000

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







new_car=Car('ABC-123', 200)
print( f"Rekisteri nro: {new_car.registration_number}\nHuippunopeus: {new_car.maximum_speed} km/h" 
               f"\nNykyinen nopeus: {new_car.current_speed} km/h\nLiikuttu etäisyys: {new_car.travelled_distance}km")


new_car.acceleration(60)
new_car.drive(1.5)
print(f"Car's traveled distance is {new_car.travelled_distance} km.")


