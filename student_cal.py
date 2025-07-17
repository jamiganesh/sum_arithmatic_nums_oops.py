class StudentGradeCalculator:
    def __init__(self,name,marks):
        self.name = name 
        self.marks = marks 

    def average(self):
        if not self.marks:
            return 0 
        avg_marks = sum(self.marks) / len(self.marks) 
        return round(avg_marks) 
    
    def grade(self):
        avg_marks = self.average() 
        if avg_marks > 90:
            return "A+" 
        elif avg_marks > 70:
            return "A" 
        elif avg_marks > 60:
            return "B" 
        elif avg_marks > 40:
            return "C" 
        else:
            return "Fail" 
        
    def showData(self):
        print(f"Student Name: {self.name}")
        print(f"Average Marks: {self.average()}")
        print(f"Grade: {self.grade()}")    


s1 = StudentGradeCalculator("Jami Ganesh", [25,68,94,89,78,20]) 
s1.showData()        