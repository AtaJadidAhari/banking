
with open('./Data/Constants.txt', 'r') as f:
	lines = f.readlines()
	years_before_first_child_mean = float(lines[1])
	years_before_first_child_var = float(lines[3])
	average_age_of_marriage_men = float(lines[5])
	average_age_of_marriage_women = float(lines[7])
	marriage_age_var = float(lines[9])
	last_year_to_have_first_child = float(lines[11])

# To keep Counts of human by age
humans_by_age = [0 for i in range(100)] 	


years_to_first_child = [0 for i in range(11)]
with open('./Data/yearstofirstchild.txt', 'r') as f:
	lines = f.readlines()
	for i in range(11):
		years_to_first_child[i] = float(lines[i].split('\t')[1])
	

geographical_neighbourhood = [0 for i in range(30)]
with open('./Data/GeographicNeighbourhood.txt', 'r') as f:
	lines = f.readlines()
	for i in range(30):
		geographical_neighbourhood[i] = float(lines[i].split('\t')[1])
		

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
		

		
# mr nikbakhts: it is a 63 36 array
# data is 62 36
marriage_probs =  []
with open('./Data/MarriageProb.txt', 'r') as f:
	lines = f.readlines()
	
	for line in lines:
		marriage_probs.append(list(map(float, line.split('\t'))))

	
age_marriage_probs = []
with open('./Data/AgeMarriageProbs.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		age_marriage_probs.append(list(map(float, line.split('\t'))))

		
		
birth_probs = []
with open('./Data/BirthProbs.txt', 'r') as f:
	lines = f.readlines()
	for line in lines:
		birth_probs.append(list(map(float, line.split('\t'))))
		

degree_marriage_men = []		
degree_marriage_female = []		
income_marriage_men = []
religion_marriage_men = []

	
with open('./Data/DegreeInMarriage.txt', 'r') as f:
	lines = f.readlines()
	for i in range(1, 4):
		degree_marriage_men.append(list(map(float, lines[i].split('\t'))))
	
	for i in range(5, 8):
		degree_marriage_female.append(list(map(float, lines[i].split('\t'))))
		
	for i in range(9, 13):
		income_marriage_men.append(list(map(float, lines[i].split('\t'))))
		
	for i in range(14, 18):
		religion_marriage_men.append(list(map(float, lines[i].split('\t'))))


		

def	calculate_education(education, vaze_savad):
	if education == 11 or education == 21:
		education = 1
		
	elif education == 31 or education == 41:
		education = 2
		
	elif education == 51:
		education = 3
	elif education == 52:
		education = 4
		
	elif education == 53:
		education = 5
      
	elif education == 61:
		education = 6
	
	elif education == 71:
		education = 1
		
	if vaze_savad == 2:
		education = 0
	
	return education
	
	
def calculate_religion(V_religion):

                  
    if V_religion >= 9:                
	    V_religion = 4
                  
    elif V_religion == 1 or V_religion == 2:
                  
        V_religion = 1
                  
    elif V_religion >= 3 or V_religion <= 7:
                  
        V_religion = V_religion / 2
                  
    elif V_religion == 8:
                  
        V_religion = 3.5
                  
    return V_religion

class Person():
	
	def __init__(self ,id, age, gender, married, divorced, childnum, marriage_age, religion, education, income, spouse, \
				parent1, parent2, family_number, first_birth_age, relation, work_hour, age_radius_SN, IE, last_child_birth, ostan):
		self.id = id
		self.age = age
		self.gender = gender
		self.married = married
		self.divorced = divorced
		self.childnum = childnum
		self.marriage_age = marriage_age
		self.religion = religion
		self.education = education
		self.income = income
		self.spouse = spouse
		self.parent1 = parent1
		self.parent2 = parent2
		self.first_birth_age = first_birth_age
		self.relation = relation
		self.work_hour = work_hour
		self.age_marriage_probs = age_marriage_probs
		self.IE = IE
		self.last_child_birth = last_child_birth
		self.family_number = family_number
		self.ostan = ostan
		
		

		
class Family():
	
	def __init__(self, id, p1, p2, childnum, children, maxChildAge, minChildAge):
		self.id = id
		self.p1 = p1
		self.p2 = p2
		self.childnum = childnum
		self.children = children
		self.maxChildAge = maxChildAge
		self.minChildAge = minChildAge


# gender : men 1, women 0
family_number = 0
fn = 0
people = []
families = []
z = 0
with open('./Data/InitialSettings3.txt', 'r') as f:
	
	for line in f:
		z += 1
		processed = line.split('\t')
		processed[-1] = processed[-1][:-2]
		
		processed = [-1 if i == '' else float(i) for i in processed] 
		processed = list(map(float, processed))
		V_ID = processed[0] - 1  # make it zero based
    
		V_Ostan = processed[1]
		V_BodeKhanevar = processed[2]
    
		V_Relation = processed[3]
		V_Gender = processed[4] % 2
    
		V_Age = processed[5]
    
		V_Vaze_Eghamat = processed[6]
    
		V_IsStudent = processed[7]
    
		V_Vaze_Savad = processed[8]
    
		V_education =  processed[9]
    
    
		V_Edu_Field = processed[10]
		V_Vaze_Faaliat = processed[11]
		V_Shoghl = processed[12]
		V_Vaze_Shoghli = processed[13]
		V_Married = processed[14]
		V_NeedHelp = processed[15]
		V_childnum = processed[16]
    
    
		
		V_spouse = processed[17] - 1
		
		V_religion = processed[18]
		V_paidHour = processed[19]
		
		
		education = calculate_education(V_education, V_Vaze_Savad)
		religion = calculate_religion(V_religion)
		relation =  V_Relation
		work_hour = V_paidHour
		age = V_Age
		if age > 99:
			age = 99
		
		
		p1 = -1
		p2 = -1
		if V_Relation == 1:  # sarparast khanevar
			
			if V_Gender == 1:
				p1 = V_ID			
			else:
				p2 = V_ID
				
			childnum = V_childnum	
			
			families.append(Family(family_number, p1, p2, childnum, [], 0, 100))
			fn = family_number
			family_number += 1
			
		
		elif V_Relation == 2: 
			fn = families[-1].id
			if V_Gender == 1:
				families[-1].p1 = V_ID			
			else:
				families[-1].p2 = V_ID
			
		
		elif V_Relation == 3:  # child
			fn = families[-1].id
			
			families[-1].children.append(V_ID)
			
			
		if V_spouse >= 1:
			married = 1
			
		divorced = -1
		marriage_age = -1
		income = -1
		first_birth_age = -1
		age_radius_SN = -1
		IE = -1
		last_child_birth = -1

		# ID, Ostan, BODE_KHANEVAR, BASTEGY_BA_SARPARASTE_KHANEVAR, SEX, AGE, VAZE_EGHAMAT, Vaze_Tahsil, Vaze_Savad, Madrake_Tahsili, Reshte_Tahsili, Vaze_Faaliat, Shoghl, Vaze_Shoghli, Marital, NEED_TO_HELP, Childnumber, Spouse, religion, work_hour, Income_Statusque,Income_WelfarePlus, Income_WelfareMinus, Income_Compactness, Income_Scattered
		people.append(Person(V_ID, V_Age, V_Gender, married,  divorced, V_childnum, marriage_age, religion, education,\
					income, V_spouse, p1, p2, fn, first_birth_age, V_Relation, work_hour, age_radius_SN, IE, last_child_birth, V_Ostan))
		
		
print(len(families), 'number of families')
print(z, 'number of Agents')

print(families[0].children)
print(families[1].children)

