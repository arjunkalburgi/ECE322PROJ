import sys
from software.app_files import classes as cl
from time import strftime
import pytest


# CareStaff
def test_getCharts():
	Doc = Doctor(db.getUser())
	cl.getCharts(self, patient)

def test_printChartEntries():
	Doc = Doctor(db.getUser())
	cl.printChartEntries(self, patient, chart_id)

def test_getPatient():
	cl.getPatient(self, hcno)

def test_addSymptom():
	Doc = Doctor(db.getUser())
	cl.addSymptom(self, hcno, chart_id, staff_id, symptom)


# Doctor Tests
def test_introduce():
	cl.introduce(self)

def test_addDiagnosis():
	Doc = Doctor(db.getUser())
	cl.addDiagnosis(self, hcno, chart_id, staff_id, diagnosis)

def test_checkMedicationAmountValid():
	Doc = Doctor(db.getUser())
	cl.checkMedicationAmountValid(self, drug_name, amount, age_group)

def test_getValidMedicationAmount():
	Doc = Doctor(db.getUser())
	cl.getValidMedicationAmount(self, drug_name, age_group)

def test_checkPatientAllergicToDrug():
	Doc = Doctor(db.getUser())
	cl.checkPatientAllergicToDrug(self, hcno, drug_name)

def test_checkInferredAllergyToDrug():
	Doc = Doctor(db.getUser())
	cl.checkInferredAllergyToDrug(self, hcno, drug_name)

def test_addMedication():
	Doc = Doctor(db.getUser())
	cl.addMedication(self, hcno, chart_id, staff_id, start_med, end_med, drug_name, amount)


def test_introduce():
	cl.introduce(self)

def test_newChart():
	cl.newChart(self, hcno)

def test_newPatient():
	cl.newPatient(self, hcno, name, age_group, address, phone, emg_phone)

def test_checkIfPatientHasOpenChart():
	cl.checkIfPatientHasOpenChart(self, hcno)

def test_closeChart():
	cl.closeChart(self, chart_id)


def test_listDrugAmtForEachDoctor():
	cl.listDrugAmtForEachDoctor(self, start, end)

def test_listDrugAmtForEachCategory():
	cl.listDrugAmtForEachCategory(self, start, end)

def test_listMedicationsForDiagnosis():
	cl.listMedicationsForDiagnosis(self, diagnosis)

def test_listDiagnosesMadeBeforePrescribingDrug():
	cl.listDiagnosesMadeBeforePrescribingDrug(self, drug_name)
