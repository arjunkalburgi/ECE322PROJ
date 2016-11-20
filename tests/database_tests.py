import sys
from software.app_files import database as db
from time import strftime
import pytest

def test_getCurrentTime():
	assert getCurrentTime() == null
	
def test_encrypt(s):
	assert encrypt() == null

def test_getUser(username, password):
	assert getUser() == null

def test_createUser(role, name, login, password):
	assert createUser() == null

def test_getChartsForPatient(patient):
	assert getChartsForPatient() == null

def test_symptomsForPatientAndChart(hcno, chart_id):
	assert symptomsForPatientAndChart() == null

def test_diagnosesForPatientAndChart(hcno, chart_id):
	assert diagnosesForPatientAndChart() == null

def test_medicationsForPatientAndChart(hcno, chart_id):
	assert medicationsForPatientAndChart() == null

def test_addSymptomToChart(hcno, chart_id, staff_id, symptom):
	assert addSymptomToChart() == null

def test_addDiagnosisToChart(hcno, chart_id, staff_id, diagnoses):
	assert addDiagnosisToChart() == null

def test_getPatientWithHcno(hcno):
	assert getPatientWithHcno() == null

def test_isMedicationAmountValid(drug_name, amount, age_group):
	assert isMedicationAmountValid() == null

def test_getValidMedicationAmount(drug_name, age_group):
	assert getValidMedicationAmount() == null

def test_isPatientAllergicToDrug(hcno, drug_name):
	assert isPatientAllergicToDrug() == null

def test_inferredAllergy(hcno, drug_name):
	assert inferredAllergy() == null

def test_addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name, amount):
	assert addMedicationToChart() == null

def test_createPatient(hcno, name, age_group, address, phone, emg_phone):
	assert createPatient() == null

def test_isChartOpenForPatient(hcno):
	assert isChartOpenForPatient() == null

def test_createNewChartForPatient(hcno):
	assert createNewChartForPatient() == null

def test_closeChartWithId(chart_id):
	assert closeChartWithId() == null

def test_drugAmountForEachDoctor(start, end):
	assert drugAmountForEachDoctor() == null

def test_drugAmountForEachCategory(start, end):
	assert drugAmountForEachCategory() == null

def test_totalAmountForEachCategory(start, end):
	assert totalAmountForEachCategory() == null

def test_listMedicationsForDiagnosis(diagnoses):
	assert listMedicationsForDiagnosis() == null

def test_listDiagnosesMadeBeforePrescribingDrug(drug_name):
	assert listDiagnosesMadeBeforePrescribingDrug() == null
