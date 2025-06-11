from ermode import ERModel, Patient, Condition

class ERView(object):
    def __init__(self, model):
        self.model = model
        
    def run(self):
        menu = "Main menu\n" +\
               "1. Schedule a patient\n" + \
               "2. Treat the next patient\n" + \
               "3. Treat all patients\n" + \
               "4. Exit the program\n"
        while True:
            command = self.getCommand(4, menu)
            if command == 1: self.schedule()
            elif command == 2: self.treatNext()
            elif command == 3: self.treatAll()
            else: break
            
    def treatNext(self):
        if self.model.isEmpty():
            print("No patients available to treat.")
        else:
            patient = self.model.treatNext()
            print(patient, " is being treated.")
            
    def treatAll(self):
        if self.model.isEmpty():
            print("No patients available to treat.")
        else:
            while not self.model.isEmpty():
                patient = self.treatNext()
                
    def schedule(self):
        name = input("Enter the patient's name: ")
        condition = self.getCondition()
        self.model.schedule(Patient(name,condition))
        print(name, " is added to the ", condition, " list\n")
        
    def getCondition(self):
        