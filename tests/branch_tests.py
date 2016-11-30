import sys
import pytest

from software.app_files.classes import Doctor
from software.app_files.classes import Nurse
from software.app_files.classes import Admin

from software.app_files import database as db

from software.app_files import login


# From: database.py
def test_db_createUser(): 
	db.createUser(role, name, login, password):

def test_db_isChartOpenForPatient(): 
	db.isChartOpenForPatient(hcno):

def test_db_createNewChartForPatient(): 
	db.createNewChartForPatient(hcno):


# From: classes.py
def test_classes_Doctor_getCharts(): 
	classes.Doctor.getCharts(self, patient):

def test_classes_Admin_listMedicationsForDiagnosis(): 
	classes.Admin.listMedicationsForDiagnosis(self, diagnosis):

def test_classes_Admin_listDiagnosesMadeBeforePrescribingDrug(): 
	classes.Admin.listDiagnosesMadeBeforePrescribingDrug(self, drug_name):


# From: admin.py
def test_admin_listMedicationsForDiagnosisFlow(): 
	admin.listMedicationsForDiagnosisFlow(adm):

def test_admin_listDiagnosisesForDrugFlow(): 
	admin.listDiagnosisesForDrugFlow(adm):


# From: nurse.py
def test_nurse_getPatientFlow(): 
	nurse.getPatientFlow(nur):

def test_nurse_selectChart(): 
	nurse.selectChart(nur, patient):


# From: doctor.py
def test_doctor_getChartsFlow(): 
	doctor.getChartsFlow(doc):

def test_doctor_selectChart(): 
	doctor.selectChart(doc, patient):

def test_doctor_addMedicationFlow(): 
	doctor.addMedicationFlow(doc, patient, chart):


# From: login.py
def test_login_start(): 
	login.start():

