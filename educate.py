import Person

people = Person.people


def educate():
    for i in range(len(people)):
        if people[i].age > 7 and people[i].IE >= 1:
            people[i].education = 1
        if people[i].age > 15 and people[i].IE >= 2:
            people[i].education = 2
        if people[i].age > 18 and people[i].IE >= 3:
            people[i].education = 3
        if people[i].age > 20 and people[i].IE >= 4:
            people[i].education = 4
        if people[i].age > 22 and people[i].IE >= 5:
            people[i].education = 5
        if people[i].age > 27 and people[i].IE >= 6:
            people[i].education = 6
