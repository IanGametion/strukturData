
class Student:
    def __init__(self, fname="", lname="", yob=0, mob=0, dob=0, sex="", next=None):
        self.fname = fname
        self.lname = lname
        self.yob = yob
        self.mob = mob
        self.dob = dob
        self.sex = sex
        self.next = next

start = Student()
last = None
New = None

def insert(node):
    global last
    node = start.next
    last = start
    while node:
        node = node.next
        last = last.next

    if node is None:
        global New
        New = Student()
        New.next = node
        last.next = New
        name = input("\nEnter the first name: ")
        New.fname = name
        name = input("\nEnter the last name: ")
        New.lname = name
        n = int(input("\nEnter the year of birth: "))
        New.yob = n
        n = int(input("\nEnter the month of birth: "))
        New.mob = n
        n = int(input("\nEnter the day of birth: "))
        New.dob = n
        ch = input("\nEnter the sex [m/f]: ")
        New.sex = ch

def create(node):
    global start
    n = 0
    ch = ""
    start.next = None
    node = start
    while True:
        node.next = Student()
        node = node.next
        name = input("\nEnter the first name: ")
        node.fname = name
        name = input("\nEnter the last name: ")
        node.lname = name
        n = int(input("\nEnter the year of birth: "))
        node.yob = n
        n = int(input("\nEnter the month of birth: "))
        node.mob = n
        n = int(input("\nEnter the day of birth: "))
        node.dob = n
        ch = input("\nEnter the sex[m/f]: ")
        node.sex = ch
        node.next = None
        ch = input("\nDo you want to create more nodes[y/n]: ")
        if ch.lower() == "n":
            break

def display(node):
    node = start.next
    while node:
        print(f"\n{node.fname}"
              f"\t{node.lname}"
              f"\t{node.yob}"
              f"\t{node.mob}"
              f"\t{node.dob}"
              f"\t{node.sex}"
              f"\t{node.sex}")
        node = node.next
        
def get_oldest(node):
    if start.next is None:
        print("\nNo students in the list")
        return
    
    node = start.next
    oldest = node
    current_date = [2025, 3, 26]  # Assuming current date is March 26, 2025
    
    while node:
        if node.yob < oldest.yob:
            oldest = node
        elif node.yob == oldest.yob:
            if node.mob < oldest.mob:
                oldest = node
            elif node.mob == oldest.mob:
                if node.dob < oldest.dob:
                    oldest = node
        
        node = node.next
    
    # Calculate age
    age = current_date[0] - oldest.yob
    if (oldest.mob > current_date[1]) or (oldest.mob == current_date[1] and oldest.dob > current_date[2]):
        age -= 1  # Haven't had birthday yet this year
    
    print("\nOldest Student Information:")
    print(f"Name: {oldest.fname} {oldest.lname}")
    print(f"Date of Birth: {oldest.yob}-{oldest.mob}-{oldest.dob}")
    print(f"Sex: {oldest.sex}")
    print(f"Age: {age} years")

def get_youngest(node):
    if start.next is None:
        print("\nNo students in the list")
        return
    
    node = start.next
    youngest = node
    current_date = [2025, 3, 26]  # Asumsi harinya Maret 26, 2025
    
    while node:
        if node.yob > youngest.yob:
            youngest = node
        elif node.yob == youngest.yob:
            if node.mob > youngest.mob:
                youngest = node
            elif node.mob == youngest.mob:
                if node.dob > youngest.dob:
                    youngest = node
        
        node = node.next
    
    age = current_date[0] - youngest.yob
    if (youngest.mob > current_date[1]) or (youngest.mob == current_date[1] and youngest.dob > current_date[2]):
        age -= 1 
    
    print("\nOldest Student Information:")
    print(f"Name: {youngest.fname} {youngest.lname}")
    print(f"Date of Birth: {youngest.yob}-{youngest.mob}-{youngest.dob}")
    print(f"Sex: {youngest.sex}")
    print(f"Age: {age} years")

def get_average():
    node = start.next
    if node is None:
        print("\nNo students available to calculate average age.")
        return

    total_age = 0
    count = 0
    current_date = [2025, 3, 26]

    while node:
        age = current_date[0] - node.yob
        if (node.mob > current_date[1]) or (node.mob == current_date[1] and node.dob > current_date[2]):
            age -= 1 
        total_age += age
        count += 1
        node = node.next
        

    avg_age = total_age / count
    print(f"\nThe average age of students is: {avg_age:.2f} years")

def main():
    node = None
    create(node)
    while True:
        print("\n1. Add Student "
              "\n2. Display Students"
              "\n3. Delete"
              "\n4. Show Oldest"
              "\n5. Show Youngest"
              "\n6. Average"
              "\n0. Exit")
        opt = int(input("\nEnter your choice: "))
        if opt == 1:
            insert(node)
        elif opt == 2:
            display(node)
        elif opt == 3:
            delete(node)
        elif opt == 4:
            get_oldest(node)
        elif opt == 5:
            get_youngest(node)
        elif opt == 6:
            get_average()
        elif opt == 0:
            break
        else:
            print("\nInvalid Choice")

def delete(node):
    name = input("\nEnter the first name will be deleted: ")
    node = start.next
    preNode = start
    while node is not None and (node.fname != name or node):
        if node.fname == name:
            preNode.next = node.next
            return
        else:
            preNode = node
            node = node.next
    print("Data not found")

if __name__ == "__main__":
    main()
