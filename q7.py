class Staff:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def show(self):
        print(f"Name: {self.name}, ID: {self.id}")

class Doctor(Staff):
    def duty(self):
        print("Doctor treats patients.")

class Nurse(Staff):
    def duty(self):
        print("Nurse assists patients and doctors.")

class Surgeon(Staff):
    def duty(self):
        print("Surgeon performs operations.")

class LabTechnician(Staff):
    def duty(self):
        print("Lab Technician performs tests.")

staff_list = [Doctor("Amit", 1), Nurse("Riya", 2), Surgeon("Raj", 3), LabTechnician("Karan", 4)]
for s in staff_list:
    s.show()
    s.duty()
