def people_you_know():
    people = raw_input("Enter the names of people you know, separated by commas")
    people = people.split(",")
    people_list = []
    for person in people:
        people_list.append(person.lower())
    return people_list

def ask_user():
    person = raw_input("Enter the person you know?")
    people = people_you_know()
    if person in people:
        print "You know {}".format(person)

# ask_user()
# print [n for n in range(10) if n % 2 == 0]

x = [n for n in range(1, 10)]
print x