import sys
from software.app_files import database as db
from time import strftime
import pytest

def test_getCurrentTime():
	assert db.getCurrentTime() == null
	
def test_encrypt():
	assert db.encrypt("ABC") == "CDE"

def test_getUser(username, password):
	assert db.getUser() == null

def test_createUser():
	assert db.createUser("D", "name", login, password) == null

def test_getChartsForPatient(patient):
	assert db.getChartsForPatient() == null

def test_symptomsForPatientAndChart(hcno, chart_id):
	assert db.symptomsForPatientAndChart() == null

def test_diagnosesForPatientAndChart(hcno, chart_id):
	assert db.diagnosesForPatientAndChart() == null

def test_medicationsForPatientAndChart(hcno, chart_id):
	assert db.medicationsForPatientAndChart() == null

def test_addSymptomToChart(hcno, chart_id, staff_id, symptom):
	assert db.addSymptomToChart() == null

def test_addDiagnosisToChart(hcno, chart_id, staff_id, diagnoses):
	assert db.addDiagnosisToChart() == null

def test_getPatientWithHcno(hcno):
	assert db.getPatientWithHcno() == null

def test_isMedicationAmountValid(drug_name, amount, age_group):
	assert db.isMedicationAmountValid() == null

def test_getValidMedicationAmount(drug_name, age_group):
	assert db.getValidMedicationAmount() == null

def test_isPatientAllergicToDrug(hcno, drug_name):
	assert db.isPatientAllergicToDrug() == null

def test_inferredAllergy(hcno, drug_name):
	assert db.inferredAllergy() == null

def test_addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name, amount):
	assert db.addMedicationToChart() == null

def test_createPatient(hcno, name, age_group, address, phone, emg_phone):
	assert db.createPatient() == null

def test_isChartOpenForPatient(hcno):
	assert db.isChartOpenForPatient() == null

def test_createNewChartForPatient(hcno):
	assert db.createNewChartForPatient() == null

def test_closeChartWithId(chart_id):
	assert db.closeChartWithId() == null

def test_drugAmountForEachDoctor(start, end):
	assert db.drugAmountForEachDoctor() == null

def test_drugAmountForEachCategory(start, end):
	assert db.drugAmountForEachCategory() == null

def test_totalAmountForEachCategory(start, end):
	assert db.totalAmountForEachCategory() == null

def test_listMedicationsForDiagnosis(diagnoses):
	assert db.listMedicationsForDiagnosis() == null

def test_listDiagnosesMadeBeforePrescribingDrug(drug_name):
	assert db.listDiagnosesMadeBeforePrescribingDrug() == null
