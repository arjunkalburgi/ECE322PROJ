import sys
import sqlite3
from time import strftime

conn = None # global for db connection
c = None # global for cursor

# start sqlite database connection
def connectDB():
    global conn
    global c
    conn = sqlite3.connect('test_db_files/test.db')
    conn.row_factory = dict_factory
    c = conn.cursor()

# dict_factory turns query result into a dict with {col_name: value}
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def getCurrentTime():
    return strftime("%Y-%m-%d %H:%M:%S")

def encrypt(s):
	r = ""
	for char in s:
		r = r + chr(ord(char) + 0)
	return r

def getUser(username, password):
    password = encrypt(password)
    c.execute("SELECT * FROM staff WHERE login=? AND password=?", (username, password))
    return c.fetchone()

def createUser(role, name, login, password):
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

def getChartsForPatient(patient):
    c.execute("SELECT * FROM patients, charts WHERE patients.hcno = charts.hcno AND patients.hcno=? ORDER BY adate", (patient,))
    return c.fetchall()

def symptomsForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM symptoms WHERE hcno=? AND chart_id=? ORDER BY obs_date", (hcno, chart_id))
    return c.fetchall()

def diagnosesForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM diagnoses WHERE hcno=? AND chart_id=? ORDER BY ddate", (hcno, chart_id))
    return c.fetchall()

def medicationsForPatientAndChart(hcno, chart_id):
    c.execute("SELECT * FROM medications WHERE hcno=? AND chart_id=? ORDER BY mdate", (hcno, chart_id))
    return c.fetchall()

def addSymptomToChart(hcno, chart_id, staff_id, symptom):
    c.execute("INSERT INTO symptoms VALUES (?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), symptom))
    conn.commit()

def addDiagnosisToChart(hcno, chart_id, staff_id, diagnoses):
    c.execute("INSERT INTO diagnoses VALUES (?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), diagnoses))
    conn.commit()

def getPatientWithHcno(hcno):
    c.execute("SELECT * FROM patients WHERE hcno=?", (hcno,))
    return c.fetchone()

def isMedicationAmountValid(drug_name, amount, age_group):
    c.execute("SELECT * FROM dosage WHERE drug_name=? AND age_group=? AND sug_amount >= ?", (drug_name, age_group, amount))
    return c.fetchone() != None

def getValidMedicationAmount(drug_name, age_group):
    c.execute("SELECT * FROM dosage WHERE drug_name=? AND age_group=?", (drug_name, age_group))
    return c.fetchone()

def isPatientAllergicToDrug(hcno, drug_name):
    c.execute("SELECT * FROM reportedallergies WHERE hcno=? AND drug_name=?", (hcno, drug_name))
    return c.fetchone() != None

# returns tuple if patient has an inferred allergy to drug_name
def inferredAllergy(hcno, drug_name):
    c.execute("SELECT * FROM reportedallergies, inferredallergies WHERE hcno=? AND reportedallergies.drug_name = inferredallergies.alg AND inferredallergies.canbe_alg=?", (hcno, drug_name))
    return c.fetchone()

def addMedicationToChart(hcno, chart_id, staff_id, start_med, end_med, drug_name, amount):
    c.execute("INSERT INTO medications VALUES (?,?,?,?,?,?,?,?)", (hcno, chart_id, staff_id, getCurrentTime(), start_med, end_med, amount, drug_name))
    conn.commit()

def createPatient(hcno, name, age_group, address, phone, emg_phone):
    c.execute("INSERT INTO patients VALUES (?,?,?,?,?,?)", (hcno, name, age_group, address, phone, emg_phone))
    conn.commit()

# returns the id of the open chart
def isChartOpenForPatient(hcno):
    c.execute("SELECT * FROM charts WHERE hcno=? AND edate IS NULL", (hcno,))
    chart = c.fetchone()
    if chart:
        return chart['chart_id']

# returns the id of the new chart
def createNewChartForPatient(hcno):
    c.execute("SELECT MAX(chart_id) as max_id FROM charts")
    res = c.fetchone()
    new_id = 0
    if res:
        new_id = int(res['max_id']) + 1
    c.execute("INSERT INTO charts VALUES (?,?,?,?)", (new_id, hcno, getCurrentTime(), None))
    conn.commit()
    return new_id

def closeChartWithId(chart_id):
    c.execute("UPDATE charts SET edate=? WHERE chart_id=?", (getCurrentTime(), chart_id))
    conn.commit()

def drugAmountForEachDoctor(start, end):
    c.execute("SELECT name as DoctorName, drug_name, SUM(amount) as total_amount FROM staff, medications WHERE staff.staff_id = medications.staff_id GROUP BY name, drug_name AND start_med > ? AND start_med < ?", (start, end))
    return c.fetchall()

def drugAmountForEachCategory(start, end):
    c.execute("SELECT category, drugs.drug_name, SUM(amount) as amount FROM drugs, medications WHERE drugs.drug_name = medications.drug_name AND mdate > ? AND mdate < ? GROUP BY category, drugs.drug_name", (start, end))
    return c.fetchall()

def totalAmountForEachCategory(start, end):
    c.execute("SELECT category, SUM(amount) as total FROM drugs, medications WHERE drugs.drug_name = medications.drug_name AND mdate > ? AND mdate < ? GROUP BY category", (start, end))
    return c.fetchall()

def listMedicationsForDiagnosis(diagnoses):
    c.execute("SELECT drug_name, COUNT(*) as frequency FROM diagnoses, medications WHERE diagnoses.chart_id = medications.chart_id AND diagnosis=? GROUP BY drug_name ORDER BY COUNT(*)", (diagnoses,))
    return c.fetchall()

def listDiagnosesMadeBeforePrescribingDrug(drug_name):
    c.execute("SELECT DISTINCT diagnosis FROM diagnoses, medications WHERE diagnoses.chart_id = medications.chart_id AND ddate < mdate AND drug_name=?", (drug_name,))
    return c.fetchall()
