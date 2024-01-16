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

#
# class Zviera:
#     def hlas(self):
#         raise NotImplementedError("Podtrieda musi implementovat tuto metodu")
#
# class Pes(Zviera):
#     def hlas(self):
#         return "Haf"
#
# class Kohut(Zviera):
#     def hlas(self):
#         return"Kotkodak"



#
# class Macka(Zviera):
#      def hlas2(self):
#         return"Mnau"
#
# def vydaj_zvuk(zviera):
#     return zviera.hlas()
#
# pes=Pes()
# macka=Macka()
# kohut=Kohut()
#
# for zviera in [pes,macka,kohut]:
#      print(vydaj_zvuk(zviera))



class Stadium:
    def __init__(self,stadiumsname,dateofopening,country,city,seatingcapacity):
        self.stadiumsname=stadiumsname
        self.dateofopening=dateofopening
        self.country=country
        self.city=city
        self.seatingcapacity=seatingcapacity

    def capacity(self):
        print(self.seatingcapacity)


stadium1=Stadium("Bratislava",1_2_1970,"Slovakia","Bratislava",1000000)
stadium1.capacity()
stadium2=Stadium("Zilina",2_2_1980,"Slovakia","Zilina",50000)
stadium2.capacity()
stadium3=Stadium("Wien",3_3_2000,"Austria","Wiena",200000)
stadium3.capacity()
stadiums=[stadium1,stadium2,stadium3]
#
# kapacita=0
# nazov="nic"
#
# for a in stadiums:
#     if a.capacity


class Book:
    def __init__(self,title,pages,price):
        self.titile=title
        self.pages=pages
        self.price=price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self,value):
        if value >=0:
            self.__price=value
        else:
            raise  ValueError("Price is negative")

kniha=Book("Harry Poter",400,10)
print(kniha.price)
kniha.price=20
print(kniha.price)
kniha.price=-10



