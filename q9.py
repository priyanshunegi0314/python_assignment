class StudentRecord:
    def __init__(self, name):
        self.name = name
        self.__internal_marks = 0
        self.__medical_leave = 0
        self.__discipline_status = "Good"

    def set_marks(self, marks):
        if 0 <= marks <= 40:
            self.__internal_marks = marks

    def get_marks(self):
        return self.__internal_marks

    def set_medical_leave(self, days):
        self.__medical_leave = days

    def get_medical_leave(self):
        return self.__medical_leave

s = StudentRecord("Priyu")
s.set_marks(32)
s.set_medical_leave(3)
print(s.get_marks(), s.get_medical_leave())
