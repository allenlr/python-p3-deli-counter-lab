def line(deli):
    if len(deli) == 0:
        print("The line is currently empty.")
    else:
        l = []
        for index, person in enumerate(deli):
            l.append(f"{index + 1}. {person}")
        print(f"The line is currently: {' '.join(l)}")
    
def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    print(f"Welcome, {new_person}. You are number {katz_deli.index(new_person) + 1} in line.")

def now_serving(katz_deli):
    if len(katz_deli) > 0:
        print(f"Currently serving {katz_deli[0]}.")
        del(katz_deli[0])
    else:
        print("There is nobody waiting to be served!")