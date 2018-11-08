from functools import reduce

class remainingCalculation():
    """
        number = 99
        calculation.remainingCalculation(number).all()
        .two(), 
        .three(), 
        .four(),
        .five(),
        .eight(),
        .nine(),
        .ten(),
        .eleven()
        .all()
    """
    def __init__ (self, number):

        number  = str(number)
        number_list = [int(i) for i in number]
        self.number = number_list

    def two(self):

        remaining = self.number[-1] % 2
        return 0 if remaining == 0 else remaining

    def three(self):

        numberTotal = reduce(lambda x,y: x+y, self.number)
        remaining = numberTotal % 3
        return 0 if remaining == 0 else remaining

    def four(self):

        if len(self.number) >= 2:

            lastTwoDigits = str(self.number[-2]) + str(self.number[-1])
            remaining = int(lastTwoDigits) % 4
            return 0 if remaining == 0 else remaining

        else:

            lastDigit = str(self.number[0])
            remaining = int(lastDigit) % 4
            return 0 if remaining == 0 else remaining
    
    def five(self):

        if len(self.number) == 1:

            if self.number[-1] >= 5:

                number_5 = self.number[-1]
                decrease = self.number[-1] - 5
                return 0 if number_5 == 5 else decrease

            else:

                return self.number[-1]

        remaining = self.number[-1]
        return 0 if remaining == 0 or remaining == 5 else remaining

    def eight(self):

        if len(self.number) >= 3:

            lastThreeDigits = str(self.number[-3]) + str(self.number[-2]) + str(self.number[-1])
            remaining = int(lastThreeDigits) % 8
            return 0 if remaining == 0 else remaining

        elif len(self.number) == 2:

            lastTwoDigits = str(self.number[-2]) + str(self.number[-1])
            remaining = int(lastTwoDigits) % 8
            return 0 if remaining == 0 else remaining

        else:

            singleDigit = self.number[0]

            if singleDigit == 8:

                return 0

            elif singleDigit > 8:

                decrease = self.number[0] - 8
                return decrease

            else: 

                return self.number[0]

    def nine(self):

        sumOfNumbers = reduce(lambda x,y: x + y, self.number)
        remaining = sumOfNumbers % 9
        return 0 if remaining == 0 else remaining

    def ten(self):

        lastDigit = str(self.number[-1])
        return 0 if int(lastDigit) == 0 else lastDigit

    def eleven(self):

        if len(self.number) == 1:

            return self.number[0]

        reverse = tuple(reversed(self.number))
        positive = reduce(lambda x,y: x+y, reverse[0::2])
        negative = reduce(lambda x,y:x+y, reverse[1::2])
        remaining = (positive - negative) % 11
        return 0 if remaining == 0 else remaining
    
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