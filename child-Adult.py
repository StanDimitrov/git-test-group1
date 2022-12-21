class Child:

    def __init__(self, name, age, sexe, say_hello) -> None:
        self.name = name
        self.age = age
        self.sexe = sexe
        self.say_hello = say_hello
        print("You have sweet {name}")
        

class Adult:

    def __init__(self, name, age, sexe, say_hello) -> None:
        self.name = name
        self.age = age
        self.sexe = sexe
        self.say_hello = say_hello
        print("Hello to you:" + say_hello)
        



s1 = Child(1,'Stanimir', 'Dimitrov',75.0) # 
s2 = Child(2,"John", "Rambo",85.0) #