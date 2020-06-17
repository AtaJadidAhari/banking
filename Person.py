def get_age(raw_age):

    return 2020 - int(raw_age.split('-')[0])



class Person:

    def __init__(self, Id, ParentId, Gender, BirthDate, PostalCode, IsUrban, ProvinceName, CountyName,
                 Trip_AirNonPilgrimageCount_95, Trip_AirNonPilgrimageCount_96, Trip_AirNonPilgrimageCount_97,
                 Trip_AirNonPilgrimageCount_98, Cars_Count, CarPrice_Sum, Bardasht95, Variz95, MandehAval95,
                 MandehAkhar95, Sood95, Bardasht96, Variz96, MandehAval96, MandehAkhar96, Sood96, Bardasht97,
                 Variz97, MandehAval97, MandehAkhar97, Sood97, Card9801, Card9802, Card9803, Card9804,
                 Card9805, Card9806, IsBehzisti_Malool, IsBimarkhas, SenfName, IsTamin_Karfarma, Tamin_KargarCount,
                 IsBazneshaste_Sandoghha, IsBimePardaz_Sandoghha, Daramad_Total_Rials):
        self.Id = Id
        self.ParentId = ParentId
        self.Gender = Gender
        self.Age = get_age(BirthDate)
        self.PostalCode = PostalCode
        self.IsUrban = IsUrban
        self.ProvinceName = ProvinceName
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

people = []
ages = [0 for i in range(20)]

def add_ages(age):
    if age <= 5:
        ages[0] += 1
    elif age <= 10:
        ages[1] += 1
    elif age <= 15:
        ages[2] += 1
    elif age <= 20:
        ages[3] += 1
    elif age <= 25:
        ages[4] += 1
    elif age <= 30:
        ages[5] += 1
    elif age <= 35:
        ages[6] += 1
    elif age <= 40:
        ages[7] += 1
    elif age <= 45:
        ages[8] += 1
    elif age <= 50:
        ages[9] += 1
    elif age <= 55:
        ages[10] += 1
    elif age <= 60:
        ages[11] += 1
    elif age <= 65:
        ages[12] += 1
    elif age <= 70:
        ages[13] += 1
    elif age <= 75:
        ages[14] += 1
    elif age <= 80:
        ages[15] += 1
    elif age <= 85:
        ages[16] += 1
    elif age <= 90:
        ages[17] += 1
    elif age <= 95:
        ages[18] += 1
    else:
        ages[19] += 1



with open("Sample_AllNafar_981126.txt", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines[1:]:
        people.append(Person(*line.split(',')))

        add_ages(people[-1].Age)


print(ages)
