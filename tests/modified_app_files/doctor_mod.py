import sys


def addMedicationFlow(doc, patient, chart, drug, amount, action, start_med, end_med):

	string = ''
	while not doc.checkMedicationAmountValid(drug, amount, patient["age_group"]):
		string = "Above recommended amount"
		rec = doc.getValidMedicationAmount(drug, patient["age_group"])
		string = string + " the suggested amount is " + str(rec["sug_amount"])
		if action == "2":
		else: 
			break

	if doc.checkPatientAllergicToDrug(patient["hcno"], drug):
		string = "The patient is allergic to " + drug

	if doc.checkInferredAllergyToDrug(patient["hcno"], drug) is not None:
		string = "... and is also allergic to " + doc.checkInferredAllergyToDrug(patient["hcno"], drug)


	doc.addMedication(patient["hcno"], chart, doc.id, start_med, end_med, drug, amount)

	return string

