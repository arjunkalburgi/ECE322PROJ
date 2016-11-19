from .classes import Nurse
from . import database as db
# from .login import start

def getPatientFlow(nur):
	patient_hcno = raw_input("What patient are you working with today? (hcno) ")
	if nur.getPatient(patient_hcno) is None:
		print "The patient with that hcno does not exist! Please create a new patient:"
		nur.newPatient(patient_hcno, raw_input("Patient name: "), raw_input("Patient age group: "), raw_input("Patient address: "), raw_input("Patient phone number: "), raw_input("Patient emergency number: "))
	return patient_hcno

def newChartFlow(nur, patient):
	print "New chart has been selected"
	return nur.newChart(patient["hcno"])

def selectChart(nur, patient):
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

def addSymptomsFlow(nur, patient, chart):
	symptom = raw_input("Name the symptom: ")
	nur.addSymptom(patient, chart, nur.id, symptom)
	print("Symptom has been added to the database.")

def closeChartFlow(nur, chart):
	nur.closeChart(chart)
	print("The chart for this patient has been closed.")

def main_nurse(n):
	# select a patient and show their charts
	patient_hcno = getPatientFlow(n)
	patient = n.getPatient(patient_hcno)
	n.getCharts(patient["hcno"])

	# select chart
	chartId = selectChart(n, patient)
	n.printChartEntries(patient["hcno"], chartId)

	action = ""
	while True:
		action = raw_input("\nWhat would you like to do with this chart?\n\
		(1) Report this patient's symptom\n \
		(2) Close the patient's chart\n \
		(3) Open a new chart\n \
		(4) Logout\n")

		if action == "1":
			addSymptomsFlow(n, patient_hcno, chartId) # flow to get patient and insert symptom
			n.printChartEntries(patient["hcno"], chartId)

		elif action == "2":
			closeChartFlow(n, chartId) # flow to get patient and insert medication

		elif action == "3":
			break;

		elif action == "4":
			# logout the user
			break;

		else:
			print("That is not an option (e.g.: 1), please try again")

	if action == "3":
		main_nurse(n)
	else:
		print("Bye")
		return

def flow(user):

	n = Nurse(user)
	print "Welcome nurse: " + n.name

	main_nurse(n)
	return
