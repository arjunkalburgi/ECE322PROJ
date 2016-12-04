import sys
from software.app_files.classes import Doctor
from software.app_files.classes import Nurse
from software.app_files.classes import AdminStaff
from software.app_files import database as db
import pytest

db.connectDB()

'''
def teardown_module():
    # reset db
	f = open('test_db_files/proj_tables.sql','r')
	sql = f.read()
	db.c.executescript(sql)
	f = open('test_db_files/test_data.sql','r')
	sql = f.read()
	db.c.executescript(sql)


'''
# CareStaff Tests
def test_getCharts(capsys):
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    patient = doc.getPatient("15384")
    doc.getCharts(patient['hcno'])
    out=capsys.readouterr()
    print(out)
    assert out[0] == '''Charts for patient with health care number 15384:\nChart 1:\n- adate: 2015-01-06 12:24:56\n- name: Angelina Jolie\n- edate: 2015-02-13 10:35:42\n- phone: 7801234567\n- hcno: 15384\n- address: 123-120 ST, Edmonton, Alberta\n- chart_id: 10001\n- emg_phone: 7801234567\n- age_group: 18-39\n'''


def test_printChartEntries(capsys):
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    patient = doc.getPatient("15384")
    print (doc.printChartEntries("15384", "10001"))
    out=capsys.readouterr()
    print (out)
    assert out == False
	# TODO
'''
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
	doc.addSymptom("15384","10001","00001","Flu")
	entry = db.symptomsForPatientAndChart("15384", "10001")
	assert entry["hcno"] == "15384"
	assert entry["chart_id"] == '10001'
	assert entry["staff_id"] == '37225'
	assert entry["obs_date"] == "2015-01-08 18:22:55"
	assert entry["symptom"] == "Nausea"
    assert true = false


# Doctor Tests
def test_introduce():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	assert doc.introduce() == "I'm a Doctor"

def test_addDiagnosis():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.addDiagnosis("15384", '10001', '14334', 'Flu')
	entry = db.diagnosesForPatientAndChart("15384", "10001");
    assert entry['hcno'] == "15384"
    assert entry['chart_id'] == "10001"
    assert entry['diagnosis'] == "Ebola"
    assert entry['staff_id'] == "14334"
    assert entry['ddate'] == strftime("%Y-%m-%d %H:%M:%S")

def test_checkMedicationAmountValid():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	doc.checkMedicationAmountValid(drug_name, amount, age_group)
	assert doc.checkMedicationAmountValid("ZMapp", "10", "18-39") == False
	assert doc.checkMedicationAmountValid("ZMapp", "5", "18-39") == True

def test_getValidMedicationAmount():
	doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
	validMedicationAmount = doc.getValidMedicationAmount("ZMapp", "18-39")
    assert validMedicationAmount['drug_name'] == "ZMapp"
    assert validMedicationAmount['age_group'] == "18-39"
    assert validMedicationAmount['sug_amount'] = 8

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
    start = "2015-01-11 19:50:32"
    end = "2015-01-13 19:50:32"
    adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
    adm.listDrugAmtForEachDoctor(start, end)


def test_listDrugAmtForEachCategory():
    start = "2015-01-11 19:50:32"
    end = "2015-01-13 19:50:32"
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	adm.listDrugAmtForEachCategory(start, end)

def test_listMedicationsForDiagnosis():
    diagnosis = "Ebola"
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	assert adm.listMedicationsForDiagnosis(diagnosis) == True

    diagnosis = "DoesNotExist"
    assert adm.listMedicationsForDiagnosis(diagnosis) == False

def test_listDiagnosesMadeBeforePrescribingDrug():
    drug_name = "ZMapp"
	adm = Admin(db.getUser('Lgtkejq', 'sygtv{'))
	assert adm.listDiagnosesMadeBeforePrescribingDrug(drug_name) == True
    drug_name = "Heroin"
    assert adm.listDiagnosesMadeBeforePrescribingDrug(drug_name) == False

'''
