#Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja ylimmän kerroksen numeron.
# Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas. Uusi hissi on aina alimmassa kerroksessa.
# Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös-
# tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit
# ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on.
# Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen
# ja sen jälkeen takaisin alimpaan kerrokseen.





class Elevator:
    def __init__(self,bottom_floor,top_floor):
        self.bottom_floor= bottom_floor
        self.top_floor = top_floor
        self.current_floor= bottom_floor




    def floor_up (self):
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






h = Elevator(0,7)
h.go_to_floor(8)
h.go_to_floor(5)
h.go_to_floor(0)
[12.33]
