import random
import math


ProvinceNames = {'آذربایجان غربی': 0, 'آذربایجان شرقی': 1, 'اردبیل': 2, 'گیلان': 3, 'کردستان': 4, 'زنجان': 5, 'قزوین': 6,'تهران': 7, 'البرز': 7, 'مازندران': 8,'گلستان': 9, 'خراسان شمالی': 10,'خراسان رضوی': 11, 'کرمانشاه': 12, 'همدان': 13, 'مرکزی': 14, 'قم': 15,'سمنان': 16, 'ایلام': 17, 'لرستان': 18, 'اصفهان': 19, 'یزد': 20, 'خراسان جنوبی' : 21, 'خوزستان': 22, 'چهارمحال وبختیاری' : 23, 'کهگیلویه و بویراحمد': 24, 'بوشهر':25, 'فارس': 26, 'کرمان':27, 'سیستان و بلوچستان': 28, 'هرمزگان': 29}


death_probs_male = [0 for i in range(99)]
with open('./Data/deathprobmale.txt', 'r') as f:
    lines = f.readlines()
    for i in range(99):
        death_probs_male[i] = (float(lines[i]))

death_probs_female = [0 for i in range(99)]
with open('./Data/deathprobfemale.txt', 'r') as f:
    lines = f.readlines()
    for i in range(99):
        death_probs_female[i] = (float(lines[i]))



marriage_probs = []
with open('./Data/MarriageProb.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        marriage_probs.append(list(map(float, line.split('\t'))))

age_marriage_probs = []
with open('./Data/AgeMarriageProbs.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        age_marriage_probs.append(list(map(float, line.split('\t'))))



def get_age(raw_age):
    ages.append(2020 - int(raw_age.split('-')[0]))
    return 2020 - int(raw_age.split('-')[0])



class Family:

    def __init__(self, id, parent_id, father, mother, childnum, children, maxChildAge, minChildAge):
        self.family_id = id
        self.father = father
        self.mother = mother
        self.childnum = childnum
        self.children = children
        self.maxChildAge = maxChildAge
        self.minChildAge = minChildAge
        self.parent_id = parent_id
        self.alive = True

class Person:

    def __init__(self, index, Id, ParentId, Gender, BirthDate, PostalCode, IsUrban, ProvinceName, CountyName,
                 Trip_AirNonPilgrimageCount_95, Trip_AirNonPilgrimageCount_96, Trip_AirNonPilgrimageCount_97,
                 Trip_AirNonPilgrimageCount_98, Cars_Count, CarPrice_Sum, Bardasht95, Variz95, MandehAval95,
                 MandehAkhar95, Sood95, Bardasht96, Variz96, MandehAval96, MandehAkhar96, Sood96, Bardasht97,
                 Variz97, MandehAval97, MandehAkhar97, Sood97, Card9801, Card9802, Card9803, Card9804,
                 Card9805, Card9806, IsBehzisti_Malool, IsBimarkhas, SenfName, IsTamin_Karfarma, Tamin_KargarCount,
                 IsBazneshaste_Sandoghha, IsBimePardaz_Sandoghha, Daramad_Total_Rials):
        self.id = Id
        self.parent_id = ParentId
        self.gender = 0 #man

        if Gender == 'زن':
            self.gender = 1
        self.age = get_age(BirthDate)
        self.PostalCode = PostalCode
        self.IsUrban = IsUrban
        self.ProvinceName = ProvinceName
        self.ProvinceId = 0
        self.get_provinceId()
        self.CountyName = CountyName
        self.Trip_AirNonPilgrimageCount_95 = Trip_AirNonPilgrimageCount_95
        self.Trip_AirNonPilgrimageCount_96 = Trip_AirNonPilgrimageCount_96
        self.Trip_AirNonPilgrimageCount_97 = Trip_AirNonPilgrimageCount_97
        self.Trip_AirNonPilgrimageCount_98 = Trip_AirNonPilgrimageCount_98
        self.Cars_Count = Cars_Count
        self.CarPrice_Sum = CarPrice_Sum
        self.Bardasht95 = Bardasht95
        self.Variz95 = Variz95
        self.MandehAval95 = MandehAval95
        self.MandehAkhar95 = MandehAkhar95
        self.Sood95 = Sood95
        self.Bardasht96 = Bardasht96
        self.Variz96 = Variz96
        self.MandehAval96 = MandehAval96
        self.MandehAkhar96 = MandehAkhar96
        self.Sood96 = Sood96
        self.Bardasht97 = Bardasht97
        self.Variz97 = Variz97
        self.MandehAval97 = MandehAval97
        self.MandehAkhar97 = MandehAkhar97
        self.Sood97 = Sood97
        self.Card9801 = Card9801
        self.Card9802 = Card9802
        self.Card9803 = Card9803
        self.Card9804 = Card9804
        self.Card9805 = Card9805
        self.Card9806 = Card9806
        self.IsBehzisti_Malool = IsBehzisti_Malool
        self.IsBimarkhas = IsBimarkhas
        self.SenfName = SenfName
        self.IsTamin_Karfarma = IsTamin_Karfarma
        self.Tamin_KargarCount = Tamin_KargarCount
        self.IsBazneshaste_Sandoghha = IsBazneshaste_Sandoghha
        self.IsBimePardaz_Sandoghha = IsBimePardaz_Sandoghha
        self.Daramad_Total_Rials = Daramad_Total_Rials

        self.religion = random.randint(0, 7)
        self.education = random.randint(0, 5)
        self.alive = True
        self.x = self.ProvinceId//5
        self.y = self.ProvinceId - (self.ProvinceId//5 * 5)
        self.IE = 0 #intended education
        self.w = 0
        self.married = False
        self.family_id = -1

        self.index = index

    def get_provinceId(self):

        self.ProvinceId = ProvinceNames[self.ProvinceName]




def add_ages(age):
    ages[(age - 1) // 5] += 1

families = []
family_id = 0
person_index = 0
people = []
ages = [0 for i in range(20)]

men = []
women = []

men_num = 0
women_num = 0


def set_parent_to_orphans(family):
    max_age = 0
    max_age_index = -1
    for i in range(len(family.children)):
        if family.children[i].age > max_age:
            max_age = family.children[i].age
            max_age_index = i
    parent = family.children[max_age_index]

    for i in range(len(family.children)):
        family.children[i].parent_id = parent.parent_id

    if parent.gender == 0:
        family.father = parent
    else:
        family.mother = parent






def set_parent():
    to_remove = []
    children = []
    for i in range(len(families)):
        minimum_difference = 100
        index = -1

        if families[i].mother is None and families[i].father is None:
            to_remove.append(i)
            set_parent_to_orphans(families[i])
        elif families[i].mother is None:
            for j in range(len(families[i].children)):
                if families[i].children[j].gender == 1:

                    if math.fabs(families[i].children[j].age - families[i].father.age) < minimum_difference:
                        index = j
                        minimum_difference =  math.fabs(families[i].children[j].age - families[i].father.age)
            if minimum_difference < 15:
                families[i].mother = families[i].children[index]
                del(families[i].children[index])

        else:
            for j in range(len(families[i].children)):

                if families[i].children[j].gender == 0:
                    if math.fabs(families[i].children[j].age - families[i].mother.age) < minimum_difference:
                        index = j
                        minimum_difference = math.fabs(families[i].children[j].age - families[i].mother.age)
            if minimum_difference <= 15:
                families[i].father = families[i].children[index]
                del (families[i].children[index])
    """
    to_remove = [to_remove[i] - i for i in range(len(to_remove))]
    for i in to_remove:
        del (families[i])

    children = [children[i] - i for i in range(len(children))]
    for i in children:
        del (people[i])
    """


parent_ids = []
with open("Sample_AllNafar_981126.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines[1:50000]: #simulating on a part of data

        p = Person(person_index, *line.split(','))
        person_index += 1
        parent_ids.append(p.parent_id)
        #print(p.x, p.y, p.ProvinceId)
        people.append(p)

        if p.parent_id == p.id: #this person is sarparast khanevar


            if p.gender == 0:


                if len(families) == 0:

                    families.append(Family(family_id, p.id, p, None, 0, [], 0, 100))
                    family_id += 1

                elif families[-1].parent_id != p.id:
                    families.append(Family(family_id, p.id, p, None, 0, [], 0, 100))
                    family_id += 1
                else:

                    families[-1].father = p
            else:

                women_num += 1
                if len(families) == 0:
                    families.append(Family(family_id, p.id, None, p, 0, [], 0, 100))
                    family_id += 1
                elif families[-1].parent_id != p.id:
                    families.append(Family(family_id, p.id, None, p, 0, [], 0, 100))
                    family_id += 1
                else:

                    families[-1].mother = p

        else: #this person is not sarparast khanevar
            #if p.gender == 0 and p.age > 15:

            #    men.append(p)

            #else:
            #    women.append(p)

            if families[-1].parent_id != p.parent_id:


                families.append(Family(family_id, p.parent_id, None, None, 0, [], 0, 100))
                family_id += 1

            families[-1].children.append(p)

        p.family_id = families[-1].family_id
        add_ages(p.age)


set_parent()

for i in range(len(families)):
    if families[i].father is not None and families[i].mother is not None:
        families[i].father.married = True
        families[i].mother.married = True
print(len(people))



