class Node:
    def __init__(self, id, name, priority):
        self.id = id
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, id, name, priority):
        patient = Node(id, name, priority)

        if self.front is None or priority < self.front.priority:
            patient.next = self.front
            self.front = patient
        else:
            temp = self.front
            
            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            patient.next = temp.next
            temp.next = patient

        print("Added Patient in Queue")

    def dequeue(self):
        if self.front:
            patient = self.front
            self.front = self.front.next
            print(f"Patient Removed After Treatment : id={patient.id} name={patient.name}")
        else:
            print("No Patients in Queue")

    def display_next(self):
        if self.front:
            patient = self.front
            print(f"Patient : id={patient.id} name={patient.name}")
        else:
            print("No Patients in Queue")

    def display_all(self):
        if self.front is None:
            print("No patients waiting")
            return

        patient = self.front
        while patient:
            print(f"Patient : priority={patient.priority} id={patient.id} name={patient.name}")
            patient = patient.next

PQ = PriorityQueue()
while True:
    print("""
** Hospital Patient Queue **
1. Add Patient
2. Display next Patient
3. Remove Patient from Queue
4. Display All Patients in Queue
5. Exit
    """)

    s = int(input("Enter Choice: "))
    match s:
        case 1:
            id = input("Enter Patient id: ")
            name = input("Enter Patient name: ")
            priority = int(input("Enter Priority (1 - Critical, 2 - Serious, 3 - Normal): "))

            if priority not in range(1, 4):
                print("invlaid Priority")
            else:
                PQ.enqueue(id, name, priority)
        case 2:
            PQ.display_next()
        case 3:
            PQ.dequeue()
        case 4:
            PQ.display_all()
        case 5:
            print("Exiting....")
            break
        case _:
            print("invlaid choice")