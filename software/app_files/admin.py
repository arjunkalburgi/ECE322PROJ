from .classes import AdminStaff

def listDrugAmtForEachDoctorFlow(adm):
	start = raw_input("What time would you like to begin your search with? ")
	end = raw_input("What time would you like to end your search with? ")
	adm.listDrugAmtForEachDoctor(start, end)

def listDrugAmtForEachCategoryFlow(adm):
	start = raw_input("What time would you like to begin your search with? ")
	end = raw_input("What time would you like to end your search with? ")
	adm.listDrugAmtForEachCategory(start, end)

def listMedicationsForDiagnosisFlow(adm):
	diagnosis = raw_input("Which diagnosis would you like to search? ")
	if not adm.listMedicationsForDiagnosis(diagnosis):
		print("That diagnosis is not in the database")

def listDiagnosisesForDrugFlow(adm):
	drug = raw_input("Which drug would you like to search? ")
	if not adm.listDiagnosesMadeBeforePrescribingDrug(drug):
		print("That drug is not in the database")

def flow(user):

	a = AdminStaff(user)
	print "Welcome admin: " + a.name

	while True:

		action = raw_input("\nWhat would you like to do?\n\
		(1) List drug amounts prescribed by each doctor\n \
		(2) List drug amounts prescribed recently by category\n \
		(3) List medications used for a given diagnosis\n \
		(4) List diagnoses that require a given drug\n \
		(5) Logout\n")

		if action == "1":
			listDrugAmtForEachDoctorFlow(a)
			print("Your task has been completed.")

		elif action == "2":
			listDrugAmtForEachCategoryFlow(a)
			print("Your task has been completed.")

		elif action == "3":
			listMedicationsForDiagnosisFlow(a)
			print("Your task has been completed.")

		elif action == "4":
			listDiagnosisesForDrugFlow(a)
			print("Your task has been completed.")

		elif action == "5":
			print("Thank you. Logging out.")
			break;

		else:
			print("That is not an option, please try again")

	print("Bye")
	return
