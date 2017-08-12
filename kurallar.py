"""
bolunebilme_kurallar adındaki sınıf tek parametre almaktadır. 2,3,4,5,8,9,10,11 ile bölünebilme
kurallarını uygulatacağımız değerdir. 
Bu değeri biri liste içinde yollamalıyız. Örn: 
deger = "123"
liste =[int(i) for i in deger]
Artık hangi bölünebilme kuralını kullanacaksak onu çağırmalıyız.
"""
# 3,9 gibi bölünebilme kurallarında sayıların hepsini topluyorduk hatırla lambda ile bunu kullanacağız.
from functools import reduce
class bolunebilme_kurallar:
    # Class başlangıcı bölünebilme kurallarını uygulayabileceğimiz sayıyı istiyoruz.
    def __init__(self,sayi):
        self.sayi = sayi

    def iki_ile(self):
        kalan = self.sayi[-1] % 2
        # Eğer sayımızın son hanesi 2 ile tam bölünürse bölünür bölünmezse bölünmez return eder.
        return "Sayı 2 ile tam bölünmektedir." if kalan == 0 else "Sayı 2 ile bölümünden kalan: {}".format(kalan)

    def uc_ile(self):
        # reduce ile sayı tuple(demetini) sürekli döndürüp lambda ile topluyoruz.
        Sayi_toplami = reduce(lambda x,y: x+y, self.sayi)
        kalan = Sayi_toplami % 3
        # Sayıların toplamı 3 ve 3 ün katı ise o sayı 3 ile bölünür. Demek oluyor ki sayıların toplamı 3 ile de tam bölünür eğer sayıların
        # toplamı 3ün katı ise
        return "Sayı 3 ile tam bölünebilmektedir." if kalan == 0 else "Sayı 3 ile bölümünden kalan: {}".format(kalan)

    def dort_ile(self):
        # Sayı 2 basamaklı veya daha fazla ise. 
        if len(self.sayi) >= 2:
            # Son 2 basamağını bir değişkene atadık.
            son_iki = str(self.sayi[-2]) + str(self.sayi[-1])
            kalan = int(son_iki) % 4
            # Son 2 basamağı eğer 4 ile tam bölünürse bölünür yoksa bölünmez değeri döndürür.
            return "Sayı 4 ile tam bölünebilmektedir." if kalan == 0 else "Sayı 4 ile bölümünden kalan: {}".format(kalan)
        # Tek basamklı ise
        else:
            son_bas = str(self.sayi[0])
            kalan = int(son_bas) % 4
            return "Sayı 4 ile tam bölünmektedir." if kalan == 0 else "Sayı 4 ile bölümünden kalan: {}".format(kalan)
    
    def bes_ile(self):
        # Eğer sayı tek basamaklı ise.
        if len(self.sayi) == 1:
            if self.sayi[-1] >= 5:
                sayi_5 = self.sayi[-1]
                cikar = self.sayi[-1] - 5
                return "Sayı 5 ile tam bölünür." if sayi_5 == 5 else "Sayı 5 ile bölümünden kalan: {}".format(cikar)
            else:
                return "Sayı 5 ile bölümünden kalan: {}".format(self.sayi[-1])
        kalan = self.sayi[-1]
        return "Sayı 5 ile tam bölünür." if kalan == 0 or kalan == 5 else "Sayı 5 ile bölümünden kalan: {}".format(kalan)

    def sekiz_ile(self):
        # Eğer sayı 3 basamak ve üzeri ise.
        if len(self.sayi) >= 3:
            # Son 3 basamağının değerini aldık.
            son_uc = str(self.sayi[-3]) + str(self.sayi[-2]) + str(self.sayi[-1])
            kalan = int(son_uc) % 8
            return "Sayı 8 ile tam bölünür." if kalan == 0 else "Sayı 8 ile bölümünden kalan: {}".format(kalan)

        # Sayı 2 basamak ise.
        elif len(self.sayi) == 2:
            son_iki = str(self.sayi[-2]) + str(self.sayi[-1])
            kalan = int(son_iki) % 8
            return "Sayı 8 ile tam bölünür." if kalan == 0 else "Sayı 8 ile bölümünden kalan: {}".format(kalan)

        # 1 basamak ise.
        else:
            tek_bas = self.sayi[0]
            if tek_bas == 8:
                return "Sayı 8 ile tam bölünür."
            elif tek_bas > 8:
                cikar = self.sayi[0] - 8
                return "Sayı 8 ile bölümünden kalan: {}".format(cikar)
            else: 
                return "Sayı 8 ile bölümünden kalan: {}".format(self.sayi[0])

    def dokuz_ile(self):
        # girin x kadar basmaklı sayının tüm rakamları toplanır.
        sayi_toplam = reduce(lambda x,y: x + y, self.sayi)
        kalan = sayi_toplam % 9
        return "Sayı 9 ile tam bölünür." if kalan == 0 else "Sayı 9 ile bölümünden kalan: {}".format(kalan)

    def on_ile(self):
        # Son basamağı 0 ise bölünür.
        son_bas = str(self.sayi[-1])
        return "Sayı 10 ile tam bölünür." if int(son_bas) == 0 else "Sayı 10 ile bölümünden kalan: {}".format(son_bas)

    def onbir_ile(self):
        # Eğer sayı tek basamaklı ise.
        if len(self.sayi) == 1:
            return "Sayı 11 ile bölümünden kalan: {}".format(self.sayi[0])
        # Gelen tuple reversed ile ters çeviriyoruz. Unutma return ederken tuple şeklinde göndermen gerekir.
        # Ama ben burada direk tuple içine aldığım için sorun yok.
        ters_cevir = tuple(reversed(self.sayi))
        pozitif_kisim = reduce(lambda x,y: x+y, ters_cevir[0::2])
        negatif_kisim = reduce(lambda x,y:x+y, ters_cevir[1::2])
        kalan = (pozitif_kisim - negatif_kisim) % 11
        return "Sayı 11 ile tam bölünür." if kalan == 0 else "Sayı 11 ile bölümünden kalan: {}".format(kalan)