from functools import reduce

class bolunebilme_kurallar:

    def __init__ (self, number):

        number  = str(number)
        number_list = [int(i) for i in number]
        self.number = number_list

    def two(self):

        kalan = self.number[-1] % 2
        return 0 if kalan == 0 else kalan

    def three(self):

        number_toplami = reduce(lambda x,y: x+y, self.number)
        kalan = number_toplami % 3
        return 0 if kalan == 0 else kalan

    def four(self):

        if len(self.number) >= 2:

            son_iki = str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_iki) % 4
            return 0 if kalan == 0 else kalan

        else:

            son_bas = str(self.number[0])
            kalan = int(son_bas) % 4
            return 0 if kalan == 0 else kalan
    
    def five(self):

        if len(self.number) == 1:

            if self.number[-1] >= 5:

                number_5 = self.number[-1]
                cikar = self.number[-1] - 5
                return 0 if number_5 == 5 else cikar

            else:

                return self.number[-1]
        kalan = self.number[-1]
        return 0 if kalan == 0 or kalan == 5 else kalan

    def eight(self):

        if len(self.number) >= 3:

            son_uc = str(self.number[-3]) + str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_uc) % 8
            return 0 if kalan == 0 else kalan

        elif len(self.number) == 2:

            son_iki = str(self.number[-2]) + str(self.number[-1])
            kalan = int(son_iki) % 8
            return 0 if kalan == 0 else kalan

        else:

            tek_bas = self.number[0]

            if tek_bas == 8:

                return 0

            elif tek_bas > 8:

                cikar = self.number[0] - 8
                return cikar

            else: 

                return self.number[0]

    def nine(self):

        number_toplam = reduce(lambda x,y: x + y, self.number)
        kalan = number_toplam % 9
        return 0 if kalan == 0 else kalan

    def ten(self):

        son_bas = str(self.number[-1])
        return 0 if int(son_bas) == 0 else son_bas

    def eleven(self):

        if len(self.number) == 1:

            return self.number[0]

        ters_cevir = tuple(reversed(self.number))
        pozitif_kisim = reduce(lambda x,y: x+y, ters_cevir[0::2])
        negatif_kisim = reduce(lambda x,y:x+y, ters_cevir[1::2])
        kalan = (pozitif_kisim - negatif_kisim) % 11
        return 0 if kalan == 0 else kalan
    
    def all(self):
        return(
            """
two: {two}
three: {three}
four: {four}
five: {five}
eight: {eight}
nine: {nine}
ten: {ten}
eleven: {eleven}
            """
            ).format(
                two = self.two(), 
                three = self.three(), 
                four = self.four(),
                five = self.five(),
                eight = self.eight(),
                nine = self.nine(),
                ten = self.ten(),
                eleven = self.eleven()
                )
    