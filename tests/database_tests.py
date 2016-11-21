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
	#place in the database correctly
	createuser = db.createUser("D", "Calvin Ho", "Calvin", "CLHO")
	assert createuser['password'] == 'CLHO'
	assert createuser['role'] == 'D'
	assert createuser['login'] == 'Calvin'
	assert createuser['name'] == 'Calvin Ho'
	#make sure it's in the db
	user = db.getUser("Calvin", "CLHO") 
	assert user['password'] == 'CLHO'
	assert user['role'] == 'D'
	assert user['login'] == 'Calvin'
	assert user['name'] == 'Calvin Ho'

def test_getChartsForPatient(patient):
	assert db.getChartsForPatient() == null

def test_symptomsForPatientAndChart():
	entry = db.symptomsForPatientAndChart("15384", "10001")
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '37225'
	assert entry["obs_date"] == "2015-01-08 18:22:55"
	assert entry["symptom"] == "Nausea"

def test_diagnosesForPatientAndChart(hcno, chart_id):
	assert db.diagnosesForPatientAndChart() == null

def test_medicationsForPatientAndChart():
	entry = db.medicationsForPatientAndChart(hcno, chart_id)
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '14334'
	assert entry["mdate"] == "2015-01-12 02:20:09"
	assert entry["start_med"] == "2015-01-12 19:50:32"
	assert entry["end_med"] == "2015-02-21 02:51:33"
	assert entry["amount"] == "8"
	assert entry["drug_name"] == "ZMapp"

def test_addSymptomToChart(hcno, chart_id, staff_id, symptom):
	assert db.addSymptomToChart() == null

def test_addDiagnosisToChart():
	db.addDiagnosisToChart("15384", '10001', '14334', 'Flu')
	# copy test_diagnosesForPatientAndChart()
	assert true == false 

def test_getPatientWithHcno(hcno):
	assert db.getPatientWithHcno() == null

def test_isMedicationAmountValid():
	assert db.isMedicationAmountValid("ZMapp", "10", "18-39") == False
	assert db.isMedicationAmountValid("ZMapp", "5", "18-39") == True

def test_getValidMedicationAmount(drug_name, age_group):
	assert db.getValidMedicationAmount() == null

def test_isPatientAllergicToDrug():
	assert db.isPatientAllergicToDrug("15384", "Tamiflu") == True
	assert db.isPatientAllergicToDrug("15384", "ZMapp") == False

def test_inferredAllergy(hcno, drug_name):
	assert db.inferredAllergy() == null

def test_addMedicationToChart():
	#place in the database correctly
	entry = db.addMedicationToChart("15384", '10001', '14334', "2015-01-21 19:50:32", "2015-02-21 02:51:33", "Viread", "8")
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '14334'
	assert entry["mdate"] == "2015-01-12 02:20:09"
	assert entry["start_med"] == "2015-01-21 19:50:32"
	assert entry["end_med"] == "2015-02-21 02:51:33"
	assert entry["amount"] == "8"
	assert entry["drug_name"] == "Viread"
	#make sure it's in the db
	entry = db.medicationsForPatientAndChart(hcno, chart_id)
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '14334'
	assert entry["mdate"] == "2015-01-12 02:20:09"
	assert entry["start_med"] == "2015-01-21 19:50:32"
	assert entry["end_med"] == "2015-02-21 02:51:33"
	assert entry["amount"] == "8"
	assert entry["drug_name"] == "Viread"

def test_createPatient(hcno, name, age_group, address, phone, emg_phone):
	assert db.createPatient() == null

def test_createNewChartForPatient(hcno):
	assert db.createNewChartForPatient() == null

def test_isChartOpenForPatient():
	assert db.isChartOpenForPatient("15384") == "10034"
	assert db.isChartOpenForPatient("20195") == None

def test_closeChartWithId():
	chartid = db.createNewChartForPatient("15384")
	if db.isChartOpenForPatient("15384") != None: 
		db.closeChartWithId(chartid)
		assert db.isChartOpenForPatient("15384") == None

def test_drugAmountForEachDoctor(start, end):
	assert db.drugAmountForEachDoctor() == null

def test_drugAmountForEachCategory():
	assert db.drugAmountForEachCategory(start, end) == null

def test_totalAmountForEachCategory(start, end):
	assert db.totalAmountForEachCategory() == null

def test_listMedicationsForDiagnosis():
	assert db.listMedicationsForDiagnosis(diagnoses) == null

def test_listDiagnosesMadeBeforePrescribingDrug(drug_name):
	assert db.listDiagnosesMadeBeforePrescribingDrug() == null
