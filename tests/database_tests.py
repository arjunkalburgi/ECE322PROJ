import sys
from software.app_files import database as db
from time import strftime
import pytest

db.connectDB()

def teardown_module():
    # reset db
    f = open('test_db_files/proj_tables.sql','r')
    tables = f.read()
    db.c.executescript(tables)
    db.conn.commit()
    f = open('test_db_files/test_data.sql','r')
    data = f.read()
    db.c.executescript(data)
    db.conn.commit()

def test_getCurrentTime():
    assert db.getCurrentTime() == strftime("%Y-%m-%d %H:%M:%S")

def test_encrypt():
    assert db.encrypt("ABC") == "CDE"


def test_getUser():
    username = "Lq{3"
    password = "Lq{345"
    user = db.getUser(username,password)
    assert user['login'] == 'Lq{3'
    assert user['password'] == 'Lq{345'

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



def test_getChartsForPatient():

    patient = '15384'
    chartsForPatients =  db.getChartsForPatient(patient)
    assert chartsForPatients[0]['adate'] == '2015-01-06 12:24:56'
    assert chartsForPatients[0]['name'] == 'Angelina Jolie'
    assert chartsForPatients[0]['edate'] == '2015-02-13 10:35:42'
    assert chartsForPatients[0]['phone'] == '7801234567'
    assert chartsForPatients[0]['hcno'] == '15384'
    assert chartsForPatients[0]['address'] == '123-120 ST, Edmonton, Alberta'
    assert chartsForPatients[0]['chart_id'] == '10001'
    assert chartsForPatients[0]['emg_phone'] == '7801234567'
    assert chartsForPatients[0]['age_group'] == '18-39'

def test_symptomsForPatientAndChart():
    entry = db.symptomsForPatientAndChart("15384", "10001")
    assert entry[0]["hcno"] == "15384"
    assert entry[0]["chart_id"] == '10001'
    assert entry[0]["staff_id"] == '37225'
    assert entry[0]["obs_date"] == "2015-01-08 18:22:55"
    assert entry[0]["symptom"] == "Nausea"

def test_diagnosesForPatientAndChart():
    
    hcno = "15384"
    chart_id = "10001"
    
    diagnosesForPatientAndChart = db.diagnosesForPatientAndChart(hcno, chart_id);
    print(diagnosesForPatientAndChart)
    assert diagnosesForPatientAndChart[0]['chart_id'] == "10001"
    assert diagnosesForPatientAndChart[0]['diagnosis'] == "Ebola"
    assert diagnosesForPatientAndChart[0]['staff_id'] == "14334"
    assert diagnosesForPatientAndChart[0]['ddate'] == "2015-01-11 14:06:01"
    assert diagnosesForPatientAndChart[0]['hcno'] == "15384"


def test_medicationsForPatientAndChart():
    entry = db.medicationsForPatientAndChart("15384", "10001")
    assert entry[0]["hcno"] == "15384"
    assert entry[0]["chart_id"] == '10001'
    assert entry[0]["staff_id"] == '14334'
    assert entry[0]["mdate"] == "2015-01-12 02:20:09"
    assert entry[0]["start_med"] == "2015-01-12 19:50:32"
    assert entry[0]["end_med"] == "2015-02-21 02:51:33"
    assert entry[0]["amount"] == 8
    assert entry[0]["drug_name"] == "ZMapp"


def test_addSymptomToChart():
    addSymptomToChart = db.addSymptomToChart("15385", "10001", "00001", "Flu")
    entry = db.symptomsForPatientAndChart("15385", "10001")
    assert entry[0]["hcno"] == "15385"
    assert entry[0]["chart_id"] == '10001'
    assert entry[0]["staff_id"] == '00001'
    assert entry[0]["obs_date"] == strftime("%Y-%m-%d %H:%M:%S")
    assert entry[0]["symptom"] == "Flu"


def test_addDiagnosisToChart():
    db.addDiagnosisToChart("15384", '10001', '14334', 'Flu')
    entry = db.diagnosesForPatientAndChart("15384", "10001")
    assert entry[1]['hcno'] == "15384"
    assert entry[1]['chart_id'] == "10001"
    assert entry[1]['diagnosis'] == "Flu"
    assert entry[1]['staff_id'] == "14334"
    assert entry[1]['ddate'] == strftime("%Y-%m-%d %H:%M:%S")

def test_getPatientWithHcno():
    hcno = "15384"
    getPatientWithHcno = db.getPatientWithHcno(hcno)
    assert getPatientWithHcno['hcno'] == "15384"
    assert getPatientWithHcno['name'] == "Angelina Jolie"
    assert getPatientWithHcno['phone'] == "7801234567"
    assert getPatientWithHcno['address'] == "123-120 ST, Edmonton, Alberta"
    assert getPatientWithHcno['emg_phone'] == "7801234567"
    assert getPatientWithHcno['age_group'] == "18-39"


def test_isMedicationAmountValid():
    assert db.isMedicationAmountValid("ZMapp", "10", "18-39") == False
    assert db.isMedicationAmountValid("ZMapp", "5", "18-39") == True


def test_getValidMedicationAmount():

    drug_name = "ZMapp"
    age_group = "18-39"

    validMedicationAmount = db.getValidMedicationAmount(drug_name, age_group)
    assert validMedicationAmount['drug_name'] == "ZMapp"
    assert validMedicationAmount['age_group'] == "18-39"
    assert validMedicationAmount['sug_amount'] == 8


def test_isPatientAllergicToDrug():
    assert db.isPatientAllergicToDrug("15384", "Tamiflu") == True
    assert db.isPatientAllergicToDrug("15384", "ZMapp") == False

def test_inferredAllergy():
    hcno = ""
    drug_name = ""
    
    inferredAllergy = db.inferredAllergy(hcno, drug_name)
    assert inferredAllergy == None


def test_addMedicationToChart():
    #place in the database
    db.addMedicationToChart("15384", '10001', '14334', "2015-01-21 19:50:32", "2015-02-21 02:51:33", "Viread", "8")
    #make sure it's in the db
    entry = db.medicationsForPatientAndChart("15384", '10001')
    assert entry[1]["hcno"] == "15384"
    assert entry[1]["chart_id"] == '10001'
    assert entry[1]["staff_id"] == '14334'
    assert entry[1]["amount"] == 8
    assert entry[1]["mdate"] == strftime("%Y-%m-%d %H:%M:%S")
    assert entry[1]["drug_name"] == "Viread"
    assert entry[1]["start_med"] == "2015-01-21 19:50:32"
    assert entry[1]["end_med"] == "2015-02-21 02:51:33"

def test_createPatient():
    hcno = "11111"
    name = "Aaron Philips"
    age_group = "18-39"
    address = "Not quite sure, Edmonton Alberta"
    phone = "1234567890"
    emg_phone = "0987654321"
    createPatient = db.createPatient(hcno, name, age_group, address, phone, emg_phone)
    getPatientWithHcno = db.getPatientWithHcno(hcno)
    assert getPatientWithHcno['hcno'] == "11111"
    assert getPatientWithHcno['name'] == "Aaron Philips"
    assert getPatientWithHcno['phone'] == "1234567890"
    assert getPatientWithHcno['address'] == "Not quite sure, Edmonton Alberta"
    assert getPatientWithHcno['emg_phone'] == "0987654321"
    assert getPatientWithHcno['age_group'] == "18-39"

def test_createNewChartForPatient():
    ## can have multiple charts for patients?
    hcno = "11121"
    name = "Aaron Philips"
    age_group = "18-39"
    address = "Not quite sure, Edmonton Alberta"
    phone = "1234567890"
    emg_phone = "0987654321"
    createPatient = db.createPatient(hcno, name, age_group, address, phone, emg_phone)

    createNewChartForPatient = db.createNewChartForPatient(hcno)
    getChartsForPatient = db.getChartsForPatient(hcno)
    assert getChartsForPatient[0]['name'] == name
    assert getChartsForPatient[0]['edate'] == None
    assert getChartsForPatient[0]['phone'] == phone
    assert getChartsForPatient[0]['address'] == address
    assert getChartsForPatient[0]['emg_phone'] == emg_phone
    assert getChartsForPatient[0]['age_group'] == age_group


def test_isChartOpenForPatient():
    assert db.isChartOpenForPatient("20195") == "10009"
    assert db.isChartOpenForPatient("15384") == None

def test_closeChartWithId():
    chartid = db.createNewChartForPatient("15384")
    if db.isChartOpenForPatient("15384") != None: 
        db.closeChartWithId(chartid)
        assert db.isChartOpenForPatient("15384") == None

def test_drugAmountForEachDoctor():

    start = "2015-01-11 19:50:32"
    end = "2015-01-13 19:50:32"
    drugAmountForEachDoctor = db.drugAmountForEachDoctor(start,end);
    assert drugAmountForEachDoctor[0]["DoctorName"] == "Phil McGraw"
    assert drugAmountForEachDoctor[0]['drug_name'] == "Viread"
    assert drugAmountForEachDoctor[0]['total_amount'] == 16


def test_drugAmountForEachCategory():
    start = "2015-01-11 02:20:09"
    end = "2015-01-13 02:20:09"
    drugAmountForEachCategory = db.drugAmountForEachCategory(start,end)
    assert drugAmountForEachCategory[0]['category'] == "anti-Ebola"
    assert drugAmountForEachCategory[0]['drug_name'] == "ZMapp"
    assert drugAmountForEachCategory[0]['amount'] == 8


def test_totalAmountForEachCategory():
    
    start = "2015-01-11 02:20:09"
    end = "2015-01-13 02:20:09"
    totalAmountForEachCategory = db.totalAmountForEachCategory(start,end)
    assert totalAmountForEachCategory['category'] == "anti-Ebola"
    assert totalAmountForEachCategory['total'] == "8"

    entry = db.drugAmountForEachCategory("2015-01-11 19:50:32", "2015-02-22 02:51:33")
    assert entry[0]["hcno"] == "15384"
    assert entry[0]["chart_id"] == '10001'
    assert entry[0]["staff_id"] == '14334'
    assert entry[0]["mdate"] == "2015-01-12 02:20:09"
    assert entry[0]["start_med"] == "2015-01-12 19:50:32"
    assert entry[0]["end_med"] == "2015-02-21 02:51:33"
    assert entry[0]["amount"] == "8"
    assert entry[0]["drug_name"] == "ZMapp"

def test_totalAmountForEachCategory(start, end):
    
    start = "2015-01-11 02:20:09"
    end = "2015-01-13 02:20:09"
    totalAmountForEachCategory = db.totalAmountForEachCategory(start,end)
    assert totalAmountForEachCategory['category'] == 'anti-Ebola'
    assert totalAmountForEachCategory['total'] == "8"


def test_listMedicationsForDiagnosis():
    entry = db.listMedicationsForDiagnosis("Ebola")
    assert entry[0]["frequency"] == 1
    assert entry[0]["drug_name"] == "Viread"

def test_listDiagnosesMadeBeforePrescribingDrug():
    
    drug_name = "ZMapp"
    
    listDiagnosesMadeBeforePrescribingDrug = db.listDiagnosesMadeBeforePrescribingDrug(drug_name)
    assert listDiagnosesMadeBeforePrescribingDrug[0]['diagnosis'] == 'Ebola'
