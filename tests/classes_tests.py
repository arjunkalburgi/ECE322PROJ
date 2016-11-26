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

def test_checkMedicationAmountValid():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkMedicationAmountValid(drug_name, amount, age_group)

def test_getValidMedicationAmount():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.getValidMedicationAmount(drug_name, age_group)

def test_checkPatientAllergicToDrug():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkPatientAllergicToDrug(hcno, drug_name)

def test_checkInferredAllergyToDrug():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkInferredAllergyToDrug(hcno, drug_name)

def test_addMedication():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.addMedication(hcno, chart_id, staff_id, start_med, end_med, drug_name, amount)


# Nurse Tests
def test_introduce():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	assert nur.introduce() == "I'm a Nurse"

def test_newChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.newChart(hcno)

def test_newPatient():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.newPatient(hcno, name, age_group, address, phone, emg_phone)

def test_checkIfPatientHasOpenChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.checkIfPatientHasOpenChart(hcno)

def test_closeChart():
	nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
	nur.closeChart(chart_id)


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
