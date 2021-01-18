import csv

ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

def load_list_data(lst, data_file, column_name):
    with open(data_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

load_list_data(ages, 'insurance.csv', 'age')
load_list_data(sexes, 'insurance.csv', 'sex')
load_list_data(bmis, 'insurance.csv', 'bmi')
load_list_data(num_children, 'insurance.csv', 'children')
load_list_data(smoker_statuses, 'insurance.csv', 'smoker')
load_list_data(regions, 'insurance.csv', 'region')
load_list_data(insurance_charges, 'insurance.csv', 'charges')


class PatientInfo:
    def __init__(self, patients_ages, patients_sexes, patients_bmis, patients_num_children, patients_smoker_statuses, patients_regions, patients_insurance_charges):
        self.patients_ages = patients_ages
        self.patients_sexes = patients_sexes
        self.patients_bmis = patients_bmis
        self.patients_num_children = patients_num_children
        self.patients_smoker_statuses = patients_smoker_statuses
        self.patients_regions = patients_regions
        self.patients_insurance_charges = patients_insurance_charges
    
    def AnalyzeAge(self):
        #Analyze the average age of the dat file
        total_age = 0 
        for age in self.patients_ages:
            total_age += int(age)
        print('Average Age for people using Insurance service is ' + str(round(total_age/len(self.patients_ages), 2)) + ' years')
    
    def AnalyzeSex(self):
        #Analyze sex of people using insurance service
        female = 0
        male = 0
        for sex in self.patients_sexes:
            if sex == 'male': 
                male += 1
            else:
                female += 1
        print('Male counts: ', male)
        print('Female counts: ', female)
    

    def AnalyzeRegion(self):
        #Analyze the region where the user using insurance service comes from
        unique_region = [] #since the regions are duplicate, this list is created to erase duplicated ones
        for region in self.patients_regions:
            if region not in unique_region:
                unique_region.append(region)
        print(unique_region)
    def AverageCharge(self):
        #Analyze average yearly charges
        total_charge = 0
        for charge in self.patients_insurance_charges:
            total_charge += float(charge)
        return ('Avarage charge is ' + str(round(total_charge/len(self.patients_insurance_charges), 2)) + ' dollars')

patient_info = PatientInfo(ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges)
patient_info.AnalyzeAge()
patient_info.AnalyzeRegion()