class SeriesCalculator:
    def __init__(self,first_term, difference, last_term):
        self.a = first_term 
        self.d = difference 
        self.n = last_term 
    
    def calculate_sum(self):
        # An arithmetic series is the sum of terms in an arithmetic sequence....
        # a sequence where each term increases (or decreases) by a constant difference.
        # sum_n = n/2*(2a + (n-1)d)

        # n = number of terms
        # a = first term
        # d = common difference

        sum_num = (self.n/2) * (2*self.a + (self.n-1)* self.d) 
        return sum_num 
    
    def showData(self):
        print(f"The sum of the given arithamatic sequece is: {self.calculate_sum()}") 

r1 = SeriesCalculator(2,2,5)       
r1.showData() 