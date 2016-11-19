from .classes import Doctor
from . import database as db
# from .login import start

def getChartsFlow(doc):
	patient_hcno = raw_input("What patient are you working with today? (hcno) ")
	returnobj = doc.getCharts(patient_hcno)
	if returnobj == "no_patient":
		print("That is not a patient's hcno that we have registered. Please use hcno for the patient. ")
		patient_hcno = getChartsFlow(doc)
	return patient_hcno

def selectChart(doc, patient):
	chartId = raw_input("Which chart would you like to open? (select id) ")
	if not doc.printChartEntries(patient, chartId):
		print("There was a problem, please type the chartid. ")
		selectChart(doc, patient)
	return chartId

def addSymptomsFlow(doc, patient, chart):
	symptom = raw_input("Name the symptom:")
	doc.addSymptom(patient, chart, doc.id, symptom)
	print("Symptom has been added to the database.")

def addDiagnosisFlow(doc, patient, chart):
	diagnosis = raw_input("Name the diagnosis:")
	doc.addDiagnosis(patient, chart, doc.id, diagnosis)
	print("Diagnosis has been added to the database.")

def addMedicationFlow(doc, patient, chart):
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

def flow(user):

	d = Doctor(user)
	print "Welcome doctor: " + d.name

	# select a patient and show their charts
	patient_hcno = getChartsFlow(d)
	patient = d.getPatient(patient_hcno)

	# select chart
	chartId = selectChart(d, patient["hcno"])
	print(chartId)

	while True:

		action = raw_input("\nWhat would you like to do with this chart?\n \
		(1) Report this patient's symptom\n \
		(2) Report your diagnosis of this patient\n \
		(3) Report your medication prescription for this patient\n \
		(4) Logout\n")

		if action == "1":
			addSymptomsFlow(d, patient["hcno"], chartId) # flow to get patient and insert symptom

		elif action == "2":
			addDiagnosisFlow(d, patient["hcno"], chartId) # flow to get patient and insert diagnosis

		elif action == "3":
			addMedicationFlow(d, patient, chartId) # flow to get patient and insert medication

		elif action == "4":
			# logout the user
			break;

		else:
			print("That is not an option (e.g.: 1), please try again")

	print("Bye")
	return
