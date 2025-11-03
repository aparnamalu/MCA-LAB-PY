class HidingDemo:
    "Program for Hiding Data"
    __num = 0   

    def numbercount(self):
        self.__num += 1
        print("Number Count =", self.__num)

number = HidingDemo()
number.numbercount()
print(number.__num)
