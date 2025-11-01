
class Student:
    school_name="KMHS SCHOOL"
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
    def display_info(self):
        print(f"{self.name} Roll NO: {self.roll_no} Marks: {self.marks} ,Grade: {self.grade()}")
    def grade(self):
        if self.marks>=90:
            return 'A'
        elif self.marks>=80:
            return 'B'
        elif self.marks>=70:
            return 'C'
        elif self.marks>=60:
            return 'D'
        else:
            return 'F'
s1=Student('Abbas',1,76)
s1.display_info()
s1.grade()
s2=Student('Ali',2,89)
s2.display_info()
s2.grade()
s3=Student('Ayan',3,96)
s3.display_info()
s3.grade()
s3=Student('Arham',4,40)
s3.display_info()
s3.grade()

