import sys
import pytest

from software.app_files.classes import Doctor
from software.app_files.classes import Nurse
from software.app_files.classes import AdminStaff

from software.app_files import doctor as docfile
from software.app_files import nurse as nurfile
from software.app_files import admin as admfile

from software.app_files import database as db

from software.app_files import login

from tests.modified_app_files import nurse_mod
from tests.modified_app_files import doctor_mod

db.connectDB()

def teardown_module():
    f = open('test_db_files/proj_tables.sql','r')
    sql = f.read()
    db.c.executescript(sql)
    db.conn.commit()
    f = open('test_db_files/test_data.sql','r')
    sql = f.read()
    db.c.executescript(sql)
    db.conn.commit()

def db_wipe():
    f = open('test_db_files/proj_tables.sql','r')
    sql = f.read()
    db.c.executescript(sql)
    db.conn.commit()


# From: database.py

'''
Fails! Because res is empty when there is no staff and cannot get max id of an empty list.
TypeError: int() argument must be a string or a number, not 'NoneType'
    
'''

def test_db_createUser(): 
    ''' 
    db.createUser(role, name, login, password):
        password = encrypt(password)
        c.execute("SELECT MAX(staff_id) as max_id FROM staff")
        res = c.fetchone()
        new_id = 0
        if res:
            new_id = int(res['max_id']) + 1
        c.execute("INSERT INTO staff VALUES (?,?,?,?,?)", (new_id, role, name, login, password))
        conn.commit()
        c.execute("SELECT * FROM staff WHERE staff_id=?", (new_id,))
        return c.fetchone()
    '''
    # if db has staff
    username = "new"
    password = "new"
    newuser = db.createUser("D", "doc", username, password)
    assert newuser['login'] == username
    assert newuser['password'] == password
    
    # if db doesnt have staff
    db_wipe()
    username = "Lq{3"
    password = "Lq{345"
    newuser = db.createUser("D", "doc", username, password)
    assert newuser['login'] == username
    assert newuser['password'] == password





'''
Passes but Uhh neither of these have open charts..
    
'''

def test_db_isChartOpenForPatient(): 
    '''
    db.isChartOpenForPatient(hcno):
        c.execute("SELECT * FROM charts WHERE hcno=? AND edate IS NULL", (hcno,))
        chart = c.fetchone()
        if chart:
            return chart['chart_id']
    '''
    # if patient has an open chart
    assert db.isChartOpenForPatient('20195') == None

    # if patient doesn't have an open chart
    assert db.isChartOpenForPatient('15384') == None


'''
Passes
    
'''
def test_db_createNewChartForPatient(): 
    '''
    db.createNewChartForPatient(hcno):
        c.execute("SELECT MAX(chart_id) as max_id FROM charts")
        res = c.fetchone()
        new_id = 0
        if res:
            new_id = int(res['max_id']) + 1
        c.execute("INSERT INTO charts VALUES (?,?,?,?)", (new_id, hcno, getCurrentTime(), None))
        conn.commit()
        return new_id
    '''

    # if db has a chart for the user
    assert db.createNewChartForPatient('15384') == "10010"

    db_wipe()
    # if there isn't a patient hcno
    assert db.createNewChartForPatient('395') == "0"



# From: classes.py
def test_classes_Doctor_getCharts(): 
    '''
    classes.Doctor.getCharts(self, patient):
        print 'Charts for patient with health care number ' + patient + ':'
        charts = getChartsForPatient(patient)
        if len(charts) == 0:
            print 'No charts for patient ' + patient + '!'
            return "no_patient"
        for idx, row in enumerate(charts):
            print 'Chart ' + str(idx + 1) + ':'
            printRow(row)
    '''
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    # if there are no charts for patient
    assert doc.getCharts('15385') == "no_patient"

    # if there are charts for patient
    assert doc.getCharts('15384') == None
 
 #actually wrong, listDiagnosesMadeBeforePrescribingDrug doesn't return None

def test_classes_Admin_listMedicationsForDiagnosis(): 
    '''
    classes.Admin.listMedicationsForDiagnosis(self, diagnosis):
        print 'Report: Drugs Prescribed to Treat ' + diagnosis
        result = listMedicationsForDiagnosis(diagnosis)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)
        if result != None:
            return True
        else:
            return False
    '''
    adm = AdminStaff(db.getUser('Lgtkejq', 'sygtv{'))
    # if there are medications for diagnosis
    assert adm.listMedicationsForDiagnosis('Ebola') == True

    # if there are no medications for diagnosis
    assert adm.listMedicationsForDiagnosis('DoesNotExdgfsgdfsist') == False
    
 #actually wrong, listDiagnosesMadeBeforePrescribingDrug doesn't return None

def test_classes_Admin_listDiagnosesMadeBeforePrescribingDrug(): 
    '''
    classes.Admin.listDiagnosesMadeBeforePrescribingDrug(self, drug_name):
        print 'Report: Diagnoses Made Before Prescribing ' + drug_name
        result = listDiagnosesMadeBeforePrescribingDrug(drug_name)
        for idx, row in enumerate(result):
            print '-----------------------'
            printRow(row)
        if result != None:
            return True
        else:
            return False
    '''
    adm = AdminStaff(db.getUser('Lgtkejq', 'sygtv{'))
    # if there are diagnoses before drug
    assert adm.listDiagnosesMadeBeforePrescribingDrug("ZMapp") == True
    # if there are no diagnoses before drug
    assert adm.listDiagnosesMadeBeforePrescribingDrug("Heroin") == False
    
# From: admin.py
def test_admin_listMedicationsForDiagnosisFlow(capsys):
    '''
    admin.listMedicationsForDiagnosisFlow(adm):
        diagnosis = raw_input("Which diagnosis would you like to search? ")
        if not adm.listMedicationsForDiagnosis(diagnosis):
            print("That diagnosis is not in the database")
    '''
    adm = AdminStaff(db.getUser('Lgtkejq', 'sygtv{'))
    # if there are medications for diagnosis
    admfile.listMedicationsForDiagnosisFlow(adm)
    out=capsys.readouterr()
    assert out[0] == ''
    
    # if there are medications for diagnosis
    db_wipe()
    admfile.listMedicationsForDiagnosisFlow(adm)
    out=capsys.readouterr()
    assert out[0] == 'That diagnosis is not in the database'
    
def test_admin_listDiagnosisesForDrugFlow(capsys):
    '''
    admin.listDiagnosisesForDrugFlow(adm):
        drug = raw_input("Which drug would you like to search? ")
        if not adm.listDiagnosesMadeBeforePrescribingDrug(drug):
            print("That drug is not in the database")
    '''
    adm = AdminStaff(db.getUser('Lgtkejq', 'sygtv{'))

    # if there are diagnosis for drug
    admfile.listMedicationsForDiagnosisFlow(adm)
    out=capsys.readouterr()
    assert out[0] == ''

    # if there are no diagnosis for drug
    db_wipe()
    admfile.listMedicationsForDiagnosisFlow(adm)
    out=capsys.readouterr()
    assert out[0] == 'That drug is not in the database'

# From: nurse.py
def test_nurse_getPatientFlow(capsys):
    '''
    nurse.getPatientFlow(nur):
        patient_hcno = raw_input("What patient are you working with today? (hcno) ")
        if nur.getPatient(patient_hcno) is None:
            print "The patient with that hcno does not exist! Please create a new patient:"
            nur.newPatient(patient_hcno, raw_input("Patient name: "), raw_input("Patient age group: "), raw_input("Patient address: "), raw_input("Patient phone number: "), raw_input("Patient emergency number: "))
        return patient_hcno
    '''
    nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
    # if user exists
    hcno = nurfile.getPatientFlow(nur)
    out = capsys.readouterr()
    assert out[0] == ''
    assert hcno == '15384'

    # if patient doesn't exist
    nurfile.getPatientFlow(nur)
    out = capsys.readouterr()
    assert out[0] == 'The patient with that hcno does not exist! Please create a new patient:'

def test_nurse_selectChart(): 
    '''
    nurse.selectChart(nur, patient):
        if nur.checkIfPatientHasOpenChart(patient["hcno"]) is not None:
            if raw_input("This patient already has an open chart (shown above), would you like to open it (y)? ") == "y":
        # return open chart
                return nur.checkIfPatientHasOpenChart(patient["hcno"])

        while(True):
            chartId = raw_input("Which chart would you like to open? (type chart's id or 'new') ")
            if chartId == "new":
        # return new chart id
                return newChartFlow(nur, patient)
            else:
        # return chart id
                if not nur.printChartEntries(patient["hcno"], chartId):
                    print("There was a problem, please type the chartid. ")
                else:
                    return chartId
    '''
    nur = Nurse(db.getUser('Lq{3', 'Lq{345'))
    # patient doesn't have open chart - opens old 
    assert nurse_mod.selectChart(nur, nur.getPatient("15384"), True, '10001', True) == "10001"
    # patient has open chart chooses not to - opens old
    assert nurse_mod.selectChart(nur, nur.getPatient("20195"), False, '10009', True) == "10009"
    
    # patient has open chart chooses to open it
    assert nurse_mod.selectChart(nur, nur.getPatient("20195"), True, '10009', True) == "10009"
    # patient has open chart chooses not to - opens new
    assert nurse_mod.selectChart(nur, nur.getPatient("20195"), False, 'new', True) == 10010

    # patient doesn't have open chart - opens old 
    assert nurse_mod.selectChart(nur, nur.getPatient("15384"), True, '10001', True) == "10001"
    # patient has open chart chooses not to - opens new
    assert nurse_mod.selectChart(nur, nur.getPatient("20195"), False, 'new', True) == 10011

    # COULDN'T GET THIS WORKING
        # patient doesn't have open chart - opens old 
        # out = capsys.readouterr()
        # nurse_mod.selectChart(nur, nur.getPatient("15384"), True, '10231', False)
        # print(out)
        # assert out[0] == "There was a problem, please type the chartid."
    
# From: doctor.py
def test_doctor_getChartsFlow(capsys):
    '''
    doctor.getChartsFlow(doc):
        patient_hcno = raw_input("What patient are you working with today? (hcno) ")
        returnobj = doc.getCharts(patient_hcno)
        if returnobj == "no_patient":
            print("That is not a patient's hcno that we have registered. Please use hcno for the patient. ")
            patient_hcno = getChartsFlow(doc)
        return patient_hcno
    '''
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    # if there is no patient with that hcno 
    docfile.getChartsFlow(doc)
    out = capsys.readouterr()
    assert out[0] == '''That is not a patient's hcno that we have registered. Please use hcno for the patient. '''
    
    # if patient with hcno exists
    hcno = docfile.getChartsFlow(doc)
    out = capsys.readouterr()
    assert out[0] == ''
    assert hcno == '15384'

def test_doctor_selectChart(capsys):
    '''
    doctor.selectChart(doc, patient):
        chartId = raw_input("Which chart would you like to open? (select id) ")
        if not doc.printChartEntries(patient, chartId):
            print("There was a problem, please type the chartid. ")
            selectChart(doc, patient)
        return chartId
    '''
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    # if there is no chart id
    # do not input 10001
    docfile.selectChart(doc, "15384")
    out = capsys.readouterr()
    assert out[0] == 'There was a problem, please type the chartid. '

    # if there is a chart id
    # input 10001
    docfile.selectChart(doc, "15384")
    out = capsys.readouterr()
    assert out[0] == ''


'''
We have to make a patient that has allergies
    
'''
def test_doctor_addMedicationFlow(): 
    '''
    doctor.addMedicationFlow(doc, patient, chart):
        drug = raw_input("Name the drug for the medication: ")
        amount = raw_input("How much would you like to prescribe? ")

        while not doc.checkMedicationAmountValid(drug, amount, patient["age_group"]):
            print("Warning, that is above the recommended amount.")
            rec = doc.getValidMedicationAmount(drug, patient["age_group"])
            print "the suggested amount is " + str(rec["sug_amount"])
            action = raw_input("\nWould you like to:\n \
                (1) Confirm your prescription\n \
                (2) Change your amount\n")
            if action == "2":
                amount = raw_input("How much would you like to prescribe? ")
            else: 
                break

        if doc.checkPatientAllergicToDrug(patient["hcno"], drug):
            print("The patient is allergic to " + drug)

        if doc.checkInferredAllergyToDrug(patient["hcno"], drug) is not None:
            print("... and is also allergic to " + doc.checkInferredAllergyToDrug(patient["hcno"], drug))

        start_med = raw_input("When would you like to start the medications? (YYYY-MM-DD HH:MM:SS) ")
        end_med = raw_input("When would you like to end the medications? (YYYY-MM-DD HH:MM:SS) ")

    doc.addMedication(patient["hcno"], chart, doc.id, start_med, end_med, drug, amount)
        print("Medication has been added to the database.")
    '''
    doc = Doctor(db.getUser('RwiNqxg:', 'Vjgug"Pggf"Jcujkpi'))
    patient = db.getPatient('15384')
    charts = db.getChartsForPatient('15384')
    drug = "ZMapp"
    amount = "8"
    action = "2"
    start_med = "2015-01-12 19:50:32"
    end_med = "2015-02-21 02:51:33"

    assert doctor_mod.addMedicationFlow(doc, patient, chart, drug, amount, action, start_med, end_med) == ''

    assert doctor_mod.addMedicationFlow(doc, patient, chart, drug, "12", 1, start_med, end_med) == "Above recommended amount the suggested amount is 8"

    assert doctor_mod.addMedicationFlow(doc, patient, chart, "Tamiflu", amount, action, start_med, end_med) == "The patient is allergic to Tamiflu"


    

# From: login.py
def test_login_start(): 
    '''
    login.start():
        username = raw_input('Please login with your username: ')
        password = raw_input('And password: ')

        user = getUser(encrypt(username), encrypt(password)) # return obj of user info, or None if can't be found

        if user is not None:
            beginFlow(user)
        else:
            if raw_input("Not a user, would you like to make a new user with this username and password? (y) ") == "y":
                user = createUser(raw_input("Role (D, N or A) "), raw_input("Name "), encrypt(username), encrypt(password))
                beginFlow(user)
            else:
                start()
    '''
    # if proper user
    assert login_mod.start('Joy1', 'Joy123', False) == "Begin user flow"
    # if improper user | not new user
    assert login_mod.start('Joys1', 'Joy1fd23', False) == "start()"
    # if improper user | new user
    assert login_mod.start('Joys1', 'Joy1fd23', True) == "Create user flow"
    
