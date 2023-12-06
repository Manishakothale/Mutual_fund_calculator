class MutualFundProfitConstructor:
    def __init__(self, scheme_code , start_date, end_date, capital):
        self.scheme_code = scheme_code
        self.start_date = start_date
        self.end_date = end_date
        self.capital = capital


    def display_info(self):
        print(f"scheme_code:{self .scheme_code}")
        print(f"start_date:{self.start_date}")
        print(f"end_date:{self.end_date}")
        print(f"capital: {self.capital}")
    

obj = MutualFundProfitConstructor(101206, "26-07-2023", "18-10-2023", 1000000)

obj.display_info()