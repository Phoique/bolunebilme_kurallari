from functools import reduce
class bolunebilme_kurallar:
    def __init__ (self, number):

        number  = str(number)
        number_list = [int(i) for i in number]
        self.number = number_list

    def two(self):
        kalan = self.number[-1] % 2
        # Eğer sayımızın son hanesi 2 ile tam bölünürse bölünür bölünmezse bölünmez return eder.
        return "Sayı 2 ile tam bölünmektedir." if kalan == 0 else "Sayı 2 ile bölümünden kalan: {}".format(kalan)

    def three(self):
        # reduce ile sayı tuple(demetini) sürekli döndürüp lambda ile topluyoruz.
        number_toplami = reduce(lambda x,y: x+y, self.number)
        kalan = number_toplami % 3
        # Sayıların toplamı 3 ve 3 ün katı ise o sayı 3 ile bölünür. Demek oluyor ki sayıların toplamı 3 ile de tam bölünür eğer sayıların
        # toplamı 3ün katı ise
        return "Sayı 3 ile tam bölünebilmektedir." if kalan == 0 else "Sayı 3 ile bölümünden kalan: {}".format(kalan)

    def four(self):
        # Sayı 2 basamaklı veya daha fazla ise. 
        if len(self.number) >= 2:
            # Son 2 basamağını bir değişkene atadık.
            son_iki = str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_iki) % 4
            # Son 2 basamağı eğer 4 ile tam bölünürse bölünür yoksa bölünmez değeri döndürür.
            return "Sayı 4 ile tam bölünebilmektedir." if kalan == 0 else "Sayı 4 ile bölümünden kalan: {}".format(kalan)
        # Tek basamklı ise
        else:
            son_bas = str(self.number[0])
            kalan = int(son_bas) % 4
            return "Sayı 4 ile tam bölünmektedir." if kalan == 0 else "Sayı 4 ile bölümünden kalan: {}".format(kalan)
    
    def five(self):
        # Eğer sayı tek basamaklı ise.
        if len(self.number) == 1:
            if self.number[-1] >= 5:
                number_5 = self.number[-1]
                cikar = self.number[-1] - 5
                return "Sayı 5 ile tam bölünür." if number_5 == 5 else "Sayı 5 ile bölümünden kalan: {}".format(cikar)
            else:
                return "Sayı 5 ile bölümünden kalan: {}".format(self.number[-1])
        kalan = self.number[-1]
        return "Sayı 5 ile tam bölünür." if kalan == 0 or kalan == 5 else "Sayı 5 ile bölümünden kalan: {}".format(kalan)

    def eight(self):
        # Eğer sayı 3 basamak ve üzeri ise.
        if len(self.number) >= 3:
            # Son 3 basamağının değerini aldık.
            son_uc = str(self.number[-3]) + str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_uc) % 8
            return "Sayı 8 ile tam bölünür." if kalan == 0 else "Sayı 8 ile bölümünden kalan: {}".format(kalan)

        # Sayı 2 basamak ise.
        elif len(self.number) == 2:
            son_iki = str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_iki) % 8
            return "Sayı 8 ile tam bölünür." if kalan == 0 else "Sayı 8 ile bölümünden kalan: {}".format(kalan)

        # 1 basamak ise.
        else:
            tek_bas = self.number[0]
            if tek_bas == 8:
                return "Sayı 8 ile tam bölünür."
            elif tek_bas > 8:
                cikar = self.number[0] - 8
                return "Sayı 8 ile bölümünden kalan: {}".format(cikar)
            else: 
                return "Sayı 8 ile bölümünden kalan: {}".format(self.number[0])

    def nine(self):
        # girin x kadar basmaklı sayının tüm rakamları toplanır.
        number_toplam = reduce(lambda x,y: x + y, self.number)
        kalan = number_toplam % 9
        return "Sayı 9 ile tam bölünür." if kalan == 0 else "Sayı 9 ile bölümünden kalan: {}".format(kalan)

    def ten(self):
        # Son basamağı 0 ise bölünür.
        son_bas = str(self.number[-1])
        return "Sayı 10 ile tam bölünür." if int(son_bas) == 0 else "Sayı 10 ile bölümünden kalan: {}".format(son_bas)

    def eleven(self):
        # Eğer sayı tek basamaklı ise.
        if len(self.number) == 1:
            return "Sayı 11 ile bölümünden kalan: {}".format(self.number[0])
        # Gelen tuple reversed ile ters çeviriyoruz. Unutma return ederken tuple şeklinde göndermen gerekir.
        # Ama ben burada direk tuple içine aldığım için sorun yok.
        ters_cevir = tuple(reversed(self.number))
        pozitif_kisim = reduce(lambda x,y: x+y, ters_cevir[0::2])
        negatif_kisim = reduce(lambda x,y:x+y, ters_cevir[1::2])
        kalan = (pozitif_kisim - negatif_kisim) % 11
        return "Sayı 11 ile tam bölünür." if kalan == 0 else "Sayı 11 ile bölümünden kalan: {}".format(kalan)