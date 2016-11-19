from database import *
from abc import ABCMeta, abstractmethod

def printRow(row):
    for key, value in row.iteritems():
        print '- ' + str(key) + ': ' + str(value)

class CareStaff:
    __metaclass__ = ABCMeta

    @abstractmethod
    def introduce(self):
          return "I'm a "

    # Doctor Q1
    def getCharts(self, patient):
        print 'Charts for patient with health care number ' + patient + ':'
        charts = getChartsForPatient(patient)
        if len(charts) == 0:
            print 'No charts for patient ' + patient + '!'
            return "no_patient"
        for idx, row in enumerate(charts):
            print 'Chart ' + str(idx + 1) + ':'
            printRow(row)

    # Doctor Q1
    def printChartEntries(self, patient, chart_id):
        symptoms = symptomsForPatientAndChart(patient, chart_id)
        diagnoses = diagnosesForPatientAndChart(patient, chart_id)
        medications = medicationsForPatientAndChart(patient, chart_id)
        printed = False
        for idx, row in enumerate(symptoms):
            print 'Symptom ' + str(idx + 1) + ':'
            printRow(row)
            printed = True
        for idx, row in enumerate(diagnoses):
            print 'Diagnosis ' + str(idx + 1) + ':'
            printRow(row)
            printed = True
        for idx, row in enumerate(medications):
            print 'Medication ' + str(idx + 1) + ':'
            printRow(row)
            printed = True
        return printed

    def getPatient(self, hcno):
        return getPatientWithHcno(hcno)

    # Doctor Q2
    def addSymptom(self, hcno, chart_id, staff_id, symptom):
        addSymptomToChart(hcno, chart_id, staff_id, symptom)

class Doctor(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Doctor, self).introduce() + "Doctor"

    def addDiagnosis(self, hcno, chart_id, staff_id, diagnosis):
        addDiagnosisToChart(hcno, chart_id, staff_id, diagnosis)

    def checkMedicationAmountValid(self, drug_name, amount, age_group):
        return isMedicationAmountValid(drug_name, amount, age_group)

    def getValidMedicationAmount(self, drug_name, age_group):
        return getValidMedicationAmount(drug_name, age_group)

    # returns true if patient is allergic to drug
    def checkPatientAllergicToDrug(self, hcno, drug_name):
        return isPatientAllergicToDrug(hcno, drug_name)

    # returns the drug that causes the inferred allergy if there is one. else returns none
    def checkInferredAllergyToDrug(self, hcno, drug_name):
        return inferredAllergy(hcno, drug_name)

    def addMedication(self, hcno, chart_id, staff_id, start_med, end_med, drug_name, amount):
        addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name, amount)

class Nurse(CareStaff):
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def introduce(self):
        return super(Nurse, self).introduce() + "Nurse"

    # returns the new chart's id
    def newChart(self, hcno):
        return createNewChartForPatient(hcno)

    def newPatient(self, hcno, name, age_group, address, phone, emg_phone):
        createPatient(hcno, name, age_group, address, phone, emg_phone)

    def checkIfPatientHasOpenChart(self, hcno):
        return isChartOpenForPatient(hcno)

    def closeChart(self, chart_id):
        closeChartWithId(chart_id)

class AdminStaff():
    def __init__(self, usr):
        self.id = usr["staff_id"]
        self.name = usr["name"]

    def listDrugAmtForEachDoctor(self, start, end):
        print 'Report: Drug Amount Prescribed For Each Doctor Between ' + start + ' and ' + end + ':'
        result = drugAmountForEachDoctor(start, end)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)

    def listDrugAmtForEachCategory(self, start, end):
        print 'Report Part 1: Drug Amount Prescribed For Each Category Between ' + start + ' and ' + end
        result = drugAmountForEachCategory(start, end)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)
        print '-------------------------------------------------'
        print 'Report Part 2: Total Amount Prescribed For Each Category Between ' + start + ' and ' + end
        result = totalAmountForEachCategory(start, end)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)

    def listMedicationsForDiagnosis(self, diagnosis):
        print 'Report: Drugs Prescribed to Treat ' + diagnosis
        result = listMedicationsForDiagnosis(diagnosis)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)
        if result != None:
            return True
        else:
            return False

    def listDiagnosesMadeBeforePrescribingDrug(self, drug_name):
        print 'Report: Diagnoses Made Before Prescribing ' + drug_name
        result = listDiagnosesMadeBeforePrescribingDrug(drug_name)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)
        if result != None:
            return True
        else:
            return False
