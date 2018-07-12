class patient(object):
    def __init__(self, p_id, name, alleg):
        self.p_id = p_id
        self.name = name
        self.alleg = alleg
        self.b_num = ''
        self.display()

    def assign_bed(self, num):
        self.b_num = num
        self.display()

    def unassign_bed(self, num):
        self.b_num = ''
        self.display()
    
    def display(self):
        print "ID: {} NAME: {} ALLEGERIES: {} BED NUMBER: {}".format(self.p_id, self.name, self.alleg, self.b_num)

class hospital(object):
    def __init__(self, patients, name, capacity):
        self.patients = patients
        self.name = name
        self.capacity = capacity
        # Lets say beds = capacity
        self.beds = 0
        self.display() 
    
    def admit(self, item):
        print len(self.patients)
        print self.capacity
        if len(self.patients) < self.capacity:
            print item.name
            self.patients.append(item)
            item.assign_bed(self.beds)
            self.beds += 1
        else:
            print "Hospital is currently full!"
        return self
    
    def discharge(self, id):
        if len(self.patients) < 1:
            print "Hospital is currently empty"
        else:
            if any(x in self.patients if x.p_id == id):
                self.patients.remove(self.patients[x])
                print "Patient ID found, and removed"
            else:
                print "Patient ID not found"
    
    def display(self):
        print self.patients, self.capacity


array_of_ps = []
nola_h = hospital(array_of_ps, 'Nola Hospital', 4)

patrick = patient(001, 'Patrick Patch', 'Bees')
michelle = patient(002, 'Michelle', 'Shellfish')
scot = patient(003, 'Scot Nelson', 'Smart')
john = patient(004, 'J Kenning', 'Food')
matt = patient(005, 'Mathew Ashley', 'Anime')
joey = patient(006, 'Joey Ke', 'Apples')

nola_h.admit(patrick).admit(michelle).admit(scot).admit(john).admit(matt).admit(joey)
nola_h.discharge(002)
nola.admi(patrick)