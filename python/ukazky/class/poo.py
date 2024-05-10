class Student ():
    def __init__(self, name, school, colour):
        self.name = name
        self.school = school
        self.fav_colour = colour

    def speak(self, greeting):
        print(f"{greeting} Moje oblíbená barva je {self.fav_colour}")

class Zak(Student):
    def __init__(self, name, school, colour):
        super().__init__(name, school, colour)

hvezdon = Student("Hvězdoň", "Třebešín", "žlutá")

print(hvezdon.fav_colour)
hvezdon.speak("Meow")

ida = Zak("Ida", "AHGDSGADJ", "modrá")
ida.speak("Dobrej")