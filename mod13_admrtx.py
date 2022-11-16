import unittest
from datetime import date, datetime

class Test(unittest.TestCase):

    def yo(x,i):
        x = ""
        i = True
        return x,i

    
    def test_symbol(input2):
        i = True
        x = ""
        while i:
            
            input2  = input("What is the symbol? ").upper()
            input2.isalpha()
            print(input2)
            len(input2)

            if len(input2) > 8 or input2.isalpha() == False:
                print("error try again")
            elif len(input2) < 8 and input2.isalpha() == True:
                i = False
                x = input2
                print(f"Your choice is",x)

    def test_chart(input3):
        i = True
        x = 0
        while i:
            input3 = input("What is the chart type? ")
            #print(input3.isnumeric())
            #print(input3)

            if input3 > "2" or input3.isnumeric() == False:
                print("try again")
            elif input3 > "0" and input3.isnumeric() == True:
                i = False
                x = input3
                print("The graph style is",x)

    def test_timeseries(input4):
        i = True
        x = 0
        while i:
            input4 = input("What is the time series? ")

            if input4 > "4" or input4.isnumeric() == False:
                print("try again.")
            elif input4 > "0" and input4.isnumeric() == True:
                i = False
                x = input4
                print("the time series is",x)

    def test_startdate(input5):
        i = True
        x = ""
        while i:
            input5 = input("What is the start date? YYYY-MM-DD ONLY ")

            try:
                x = date.fromisoformat(input5)
                i = False
                print(x)
                return x
            except:
                print("wrong format, try again")


    def test_enddate(input6):
        i = True
        x = ""
        while i:
            input6 = input("What is the end date? YYYY-MM-DD ONLY ")

            try:
                x = date.fromisoformat(input6)
                i = False
                print(x)
                return
            except:
                print("wrong format try again")


if __name__ == "__main__":
    unittest.main()
