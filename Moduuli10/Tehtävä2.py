#Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman
# ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä.
# Hissien lista tallennetaan talon ominaisuutena.
# Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen.
# Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def floor_up(self):
        self.current_floor += 1
        print(f'the elevator goes up to the floor {self.current_floor}')

    def floor_down(self):
        self.current_floor -= 1
        print(f'the elevator goes down to the floor {self.current_floor}')

    def go_to_floor(self, floor):
        if floor >= self.bottom_floor and floor <= self.top_floor:
            while self.current_floor != floor:
                if floor > self.current_floor:
                    self.floor_up()
                else:
                    self.floor_down()
            print("You have reached floor ", floor)
        else:
            print("Invalid floor number")


class Talo:
    def __init__(self, bottom_floor, top_floor, hissit):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.hissit = []
        for i in range(hissit):
            self.hissit.append(Elevator(bottom_floor, top_floor))

    def aja_hissiä(self, hissi_numero, kohdekerros):
        if hissi_numero >= 1 and hissi_numero <= len(self.hissit):
            hissi = self.hissit[hissi_numero-1]
            hissi.go_to_floor(kohdekerros)


#Hissien kohdekerrokset
talo = Talo(0, 7, 3)
talo.aja_hissiä(1, 3)
talo.aja_hissiä(2, 7)

