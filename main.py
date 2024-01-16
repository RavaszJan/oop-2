# class Mojakalkulacka:
#     @staticmethod
#     def sucet(a,b):
#         return a+b
#     @staticmethod
#     def sucin(a,b):
#         return a*b
#
#     print(Mojakalkulacka.sucet(2,2))
#     print(Mojakalkulacka.sucet(2,2))

class Zviera:
    def hlas(self):
        raise NotImplementedError("Podtrieda musi implementovat tuto metodu")

class Pes(Zviera):
    def hlas(self):
        return "Haf"

class Kohut(Zviera):
    def hlas(self):
        return"Kotkodak"

class Macka(Zviera):
     def hlas(self):
        return"Mnau"

def vydaj_zvuk(zviera):
    return zviera.hlas()

pes=Pes()
macka=Macka()
kohut=Kohut()

for zviera in [pes,macka,kohut]:
     print(vydaj_zvuk(zviera))



