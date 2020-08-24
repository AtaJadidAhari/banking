from helper_functions import *
import Person


families = Person.families
people = Person.people

#print('Marriage')
def probability_of_marriage(neighbors):

    married = 0
    for person in neighbors:
        if person.married:
            married += 1

    return married/len(neighbors)



def select_wife(wifes, man):
    #TODO select wife based on probability

    return wifes[0]

def create_family(husband, wife):
    #print(husband.family_id, wife.family_id, 'here')
    wife_family = families[wife.family_id]
    husband_family = families[husband.family_id]
    if husband.id == husband.parent_id:

        family = families[husband.family_id]
        wife.family_id = family.family_id
        if wife.parent_id == wife.id:
            for i in range(len(wife_family.children)):
                family.children.append(wife_family.children[i])
                wife_family.children[i].family_id = family.family_id
                wife_family.children[i].parent_id = husband.id

            wife_family.alive = False
    elif wife.id == wife.parent_id:
        family = families[wife.family_id]
        family.father = husband
        if husband.parent_id == husband.id:
            for i in range(len(husband_family.children)):
                family.children.append(husband_family.children[i])
                husband_family.children[i].family_id = family.family_id
                husband_family.children[i].parent_id = husband.id

        husband.family_id = family.family_id

    else:
        id = len(families)
        families.append(Person.Family(id, husband.id, husband, wife, 0, [], 0, 100))
        family = families[-1]
        husband.family_id = id

        wife.family_id = id



    husband.married = True
    wife.married = True
    wife.parent_id = husband.id
    husband.parent_id = husband.id
    family.mother = wife
    family.father = husband
    added_familis.append(family.family_id)





def marriage():
    for i in range(len(people)):

        if people[i].gender == 0 and not people[i].married and people[i].alive: #bachelors
            if random.random() < 0.1: #TODO fix probabilty
                neighbors = []
                for j in range(len(people)):

                    if province_neighbor(people[i], people[j]) and  economic_neighbor(people[i], people[j])  :
                        if i != j:
                            neighbors.append(people[j])

                social_network = []

                b = random.randint(people[i].age - gammaBar, people[i].age + gammaBar)


                for j in range(len(neighbors)):

                    if b - gammaBar <= neighbors[j].age <= b + gammaBar and  religion_neighbor(people[i], neighbors[j]) and education_neighbor(people[i], neighbors[j]):
                        if i != j:
                            social_network.append(people[j])
                potential_wives = []

                if len(social_network) == 0:
                    continue
                social_pressure = math.exp(beta * (probability_of_marriage(social_network) - alpha)) / (1 + math.exp(beta * (probability_of_marriage(social_network) - alpha)))

                set_parameters(social_pressure)
                for j in range(len(social_network)):
                    if social_network[j].gender == 1 and not social_network[j].married and social_network[j].alive: #bachelors
                        if religion_neighbor(people[i], social_network[j], 1) and \
                                people[i].age - 2 <= social_network[j].age <= people[i].age + 2 and \
                                education_neighbor(people[i], social_network[j], 1) and \
                                economic_neighbor(people[i], social_network[j], 1) and \
                                province_neighbor(people[i], social_network[j], 1):
                            potential_wives.append(social_network[j])

                if len(potential_wives) > 0:

                    wife = select_wife(potential_wives, people[i])
                    create_family(people[i], wife)
