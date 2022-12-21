class Student:
    pass_score = 40.0 # variable of class, we can access this using the class name Student.pass_score

    def __init__(self,roll,first_name, last_name,score, age=30, sexe="homme"):
        self.roll = roll
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        self.age = age
        self.sexe = sexe
        self.email = first_name.lower() + " " + last_name.lower() + '@gmail.com'


    def name(self):
        return self.first_name + " " + self.last_name

    def pass_or_fail(self):
        if self.score >= Student.pass_score:
            return "Passed"
        else:
            return "Failed"
    



ch1 = Student("John", 12) 
ch2 = Student("Harry", 18) 
