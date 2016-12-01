import sys
import pytest

from software.app_files.classes import Doctor
from software.app_files.classes import Nurse
from software.app_files.classes import Admin

from software.app_files import database as db

from software.app_files import login


# From: database.py
def test_db_createUser(): 
	# db.createUser(role, name, login, password):
	'''	
	password = encrypt(password)
    c.execute("SELECT MAX(staff_id) as max_id FROM staff")
    res = c.fetchone()
    new_id = 0
    if res:
        new_id = int(res['max_id']) + 1
    c.execute("INSERT INTO staff VALUES (?,?,?,?,?)", (new_id, role, name, login, password))
    conn.commit()
    c.execute("SELECT * FROM staff WHERE staff_id=?", (new_id,))
    return c.fetchone()
    '''
    # test 1 normal createUser
    # test 2 incorrect createUser

def test_db_isChartOpenForPatient(): 
	# db.isChartOpenForPatient(hcno):
	'''
	c.execute("SELECT * FROM charts WHERE hcno=? AND edate IS NULL", (hcno,))
    chart = c.fetchone()
    if chart:
        return chart['chart_id']
	'''
	# test 1 
	# test 2
	
def test_db_createNewChartForPatient(): 
	# db.createNewChartForPatient(hcno):
	'''
    c.execute("SELECT MAX(chart_id) as max_id FROM charts")
    res = c.fetchone()
    new_id = 0
    if res:
        new_id = int(res['max_id']) + 1
    c.execute("INSERT INTO charts VALUES (?,?,?,?)", (new_id, hcno, getCurrentTime(), None))
    conn.commit()
    return new_id
	'''
	# test 1 
	# test 2
	

# From: classes.py
def test_classes_Doctor_getCharts(): 
	# classes.Doctor.getCharts(self, patient):
	'''
    print 'Charts for patient with health care number ' + patient + ':'
    charts = getChartsForPatient(patient)
    if len(charts) == 0:
        print 'No charts for patient ' + patient + '!'
        return "no_patient"
    for idx, row in enumerate(charts):
        print 'Chart ' + str(idx + 1) + ':'
        printRow(row)
	'''
	# test 1 
	# test 2
	
def test_classes_Admin_listMedicationsForDiagnosis(): 
	# classes.Admin.listMedicationsForDiagnosis(self, diagnosis):
	'''
    print 'Report: Drugs Prescribed to Treat ' + diagnosis
    result = listMedicationsForDiagnosis(diagnosis)
    for idx, row in enumerate(result):
        print '-----------------------'
        printRow(row)
    if result != None:
        return True
    else:
        return False
	'''
	# test 1 
	# test 2
	
def test_classes_Admin_listDiagnosesMadeBeforePrescribingDrug(): 
	# classes.Admin.listDiagnosesMadeBeforePrescribingDrug(self, drug_name):
	'''
    print 'Report: Diagnoses Made Before Prescribing ' + drug_name
    result = listDiagnosesMadeBeforePrescribingDrug(drug_name)
    for idx, row in enumerate(result):
        print '-----------------------'
        printRow(row)
    if result != None:
        return True
    else:
        return False
	'''
	# test 1 
	# test 2
	

# From: admin.py
def test_admin_listMedicationsForDiagnosisFlow(): 
	# admin.listMedicationsForDiagnosisFlow(adm):
	'''
	diagnosis = raw_input("Which diagnosis would you like to search? ")
	if not adm.listMedicationsForDiagnosis(diagnosis):
		print("That diagnosis is not in the database")
	'''
	# test 1 
	# test 2
	
def test_admin_listDiagnosisesForDrugFlow(): 
	# admin.listDiagnosisesForDrugFlow(adm):
	'''
	drug = raw_input("Which drug would you like to search? ")
	if not adm.listDiagnosesMadeBeforePrescribingDrug(drug):
		print("That drug is not in the database")
	'''
	# test 1 
	# test 2
	

# From: nurse.py
def test_nurse_getPatientFlow(): 
	# nurse.getPatientFlow(nur):
	'''
	patient_hcno = raw_input("What patient are you working with today? (hcno) ")
	if nur.getPatient(patient_hcno) is None:
		print "The patient with that hcno does not exist! Please create a new patient:"
		nur.newPatient(patient_hcno, raw_input("Patient name: "), raw_input("Patient age group: "), raw_input("Patient address: "), raw_input("Patient phone number: "), raw_input("Patient emergency number: "))
	return patient_hcno
	'''
	# test 1 
	# test 2
	
def test_nurse_selectChart(): 
	# nurse.selectChart(nur, patient):
	'''
	if nur.checkIfPatientHasOpenChart(patient["hcno"]) is not None:
		if raw_input("This patient already has an open chart (shown above), would you like to open it (y)? ") == "y":
	# return open chart
			return nur.checkIfPatientHasOpenChart(patient["hcno"])

	while(True):
		chartId = raw_input("Which chart would you like to open? (type chart's id or 'new') ")
		if chartId == "new":
	# return new chart id
			return newChartFlow(nur, patient)
		else:
	# return chart id
			if not nur.printChartEntries(patient["hcno"], chartId):
				print("There was a problem, please type the chartid. ")
			else:
				return chartId
	'''
	# test 1 
	# test 2
	

# From: doctor.py
def test_doctor_getChartsFlow(): 
	# doctor.getChartsFlow(doc):
	'''
	patient_hcno = raw_input("What patient are you working with today? (hcno) ")
	returnobj = doc.getCharts(patient_hcno)
	if returnobj == "no_patient":
		print("That is not a patient's hcno that we have registered. Please use hcno for the patient. ")
		patient_hcno = getChartsFlow(doc)
	return patient_hcno
	'''
	# test 1 
	# test 2
	
def test_doctor_selectChart(): 
	# doctor.selectChart(doc, patient):
	'''
	chartId = raw_input("Which chart would you like to open? (select id) ")
	if not doc.printChartEntries(patient, chartId):
		print("There was a problem, please type the chartid. ")
		selectChart(doc, patient)
	return chartId
	'''
	# test 1 
	# test 2
	
def test_doctor_addMedicationFlow(): 
	# doctor.addMedicationFlow(doc, patient, chart):
	'''
	drug = raw_input("Name the drug for the medication: ")
	amount = raw_input("How much would you like to prescribe? ")

	while not doc.checkMedicationAmountValid(drug, amount, patient["age_group"]):
		print("Warning, that is above the recommended amount.")
		rec = doc.getValidMedicationAmount(drug, patient["age_group"])
		print "the suggested amount is " + str(rec["sug_amount"])
		action = raw_input("\nWould you like to:\n \
			(1) Confirm your prescription\n \
			(2) Change your amount\n")
		if action == "2":
			amount = raw_input("How much would you like to prescribe? ")
		else: 
			break

	if doc.checkPatientAllergicToDrug(patient["hcno"], drug):
		print("The patient is allergic to " + drug)

	if doc.checkInferredAllergyToDrug(patient["hcno"], drug) is not None:
		print("... and is also allergic to " + doc.checkInferredAllergyToDrug(patient["hcno"], drug))

	start_med = raw_input("When would you like to start the medications? (YYYY-MM-DD HH:MM:SS) ")
	end_med = raw_input("When would you like to end the medications? (YYYY-MM-DD HH:MM:SS) ")

	doc.addMedication(patient["hcno"], chart, doc.id, start_med, end_med, drug, amount)
	print("Medication has been added to the database.")
	'''
	# test 1 
	# test 2
	

# From: login.py
def test_login_start(): 
	# login.start():
	'''
	username = raw_input('Please login with your username: ')
	password = raw_input('And password: ')

	user = getUser(encrypt(username), encrypt(password)) # return obj of user info, or None if can't be found

	if user is not None:
		beginFlow(user)
	else:
		if raw_input("Not a user, would you like to make a new user with this username and password? (y) ") == "y":
			user = createUser(raw_input("Role (D, N or A) "), raw_input("Name "), encrypt(username), encrypt(password))
			beginFlow(user)
		else:
			start()
	'''
	# test 1 
	# test 2
	
