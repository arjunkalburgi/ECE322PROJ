import sys
from software.app_files.classes import Doctor
from software.app_files.classes import Nurse
from software.app_files.classes import Admin
from software.app_files import database as db
import pytest


# CareStaff Tests
def test_getCharts():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.getCharts(patient)

def test_printChartEntries():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.printChartEntries(patient, chart_id)

def test_getPatient():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	patient = doc.getPatient("15384")
    assert patient['hcno'] == "15384"
    assert patient['name'] == "Angelina Jolie"
    assert patient['phone'] == "7801234567"
    assert patient['address'] == "123-120 ST, Edmonton, Alberta"
    assert patient['emg_phone'] == "7801234567"
    assert patient['age_group'] == "18-39"

def test_addSymptom():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	# doc.addSymptom("15384","10001","00001","Flu")
	# entry = db.symptomsForPatientAndChart("15384", "10001")
	# assert entry["hcno"] == "15384"
	# assert entry["chart_id"] == '10001'
	# assert entry["staff_id"] == '37225'
	# assert entry["obs_date"] == "2015-01-08 18:22:55"
	# assert entry["symptom"] == "Nausea"
    assert true = false


# Doctor Tests
def test_introduce():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	assert doc.introduce() == "I'm a Doctor"

def test_addDiagnosis():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	# doc.addDiagnosis(hcno, chart_id, staff_id, diagnosis)
	# addDiagnosisToChart(hcno, chart_id, staff_id, diagnosis)

def test_checkMedicationAmountValid():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkMedicationAmountValid(drug_name, amount, age_group)
	# return isMedicationAmountValid(drug_name, amount, age_group)
	# assert db.isMedicationAmountValid("ZMapp", "10", "18-39") == False
	# assert db.isMedicationAmountValid("ZMapp", "5", "18-39") == True

def test_getValidMedicationAmount():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.getValidMedicationAmount(drug_name, age_group)
    # validMedicationAmount = db.getValidMedicationAmount("ZMapp", "18-39")
    # assert validMedicationAmount['drug_name'] == "ZMapp"
    # assert validMedicationAmount['age_group'] == "18-39"
    # assert validMedicationAmount['sug_amount'] = 8

def test_checkPatientAllergicToDrug():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))

	assert doc.checkPatientAllergicToDrug("15384", "Tamiflu") == True
	assert doc.checkPatientAllergicToDrug("15384", "ZMapp") == False

def test_checkInferredAllergyToDrug():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkInferredAllergyToDrug(hcno, drug_name)
	# return inferredAllergy(hcno, drug_name)

def test_addMedication():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.addMedication("15384", '10001', '14334', "2015-01-22 19:50:32", "2015-02-22 02:51:33", "Viread", "8")

	entry = db.medicationsForPatientAndChart(hcno, chart_id)
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '14334'
	assert entry["mdate"] == "2015-01-12 02:20:09"
	assert entry["start_med"] == "2015-01-22 19:50:32"
	assert entry["end_med"] == "2015-02-22 02:51:33"
	assert entry["amount"] == "8"
	assert entry["drug_name"] == "Viread"


# Nurse Tests
def test_introduce():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	assert nur.introduce() == "I'm a Nurse"

def test_newChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.newChart(hcno)
	# return createNewChartForPatient(hcno)

def test_newPatient():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.newPatient(hcno, name, age_group, address, phone, emg_phone)
	# createPatient(hcno, name, age_group, address, phone, emg_phone)

def test_checkIfPatientHasOpenChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	assert nur.checkIfPatientHasOpenChart("15384") == True
	assert nur.checkIfPatientHasOpenChart("20195") == False

def test_closeChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))

	chartid = db.createNewChartForPatient("15384")
	if db.isChartOpenForPatient("15384") != None: 
		nur.closeChart(chart_id)
		assert db.isChartOpenForPatient("15384") == None


# Admin tests
def test_listDrugAmtForEachDoctor():
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	adm.listDrugAmtForEachDoctor(start, end)

def test_listDrugAmtForEachCategory():
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	adm.listDrugAmtForEachCategory(start, end)

def test_listMedicationsForDiagnosis():
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	adm.listMedicationsForDiagnosis(diagnosis)

def test_listDiagnosesMadeBeforePrescribingDrug():
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	adm.listDiagnosesMadeBeforePrescribingDrug(drug_name)
