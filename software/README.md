Hello, 

# This is Mini Project 1 for CMPUT 291 Fall 2016.

To access the database, run:
  - sqlite3 database_files/hospital.db

To run sql statements from python, see:
  - app.py 
  
To see app class structure, see: 
  - app_files/
  
## Todo
- [x] figure out how to run sql queries from python
- [x] finish class structure
- [x] implement user flows (will call user actions)
- [x] implement user actions (actual class functions that will call sql queries)
- [ ] implement sql queries (will access the db)
- [ ] login encryption
- [x] nurse.py:line 19 -- return open chart's chart ID
- [x] nurse.py:line 8 -- weird new patient
- [x] nurse.py:line 32 -- new chart flow
- [x] doctor.py:line 29 -- add medication flow

## Full Spec
https://eclass.srv.ualberta.ca/mod/page/view.php?id=2065436

### Introduction

The goal of this assignment is twofolds: (1) to teach the use of SQL in a host programming language, and (2) to demonstrate some of the functionalities that result from combining SQL with a host programming language.

Your job in this project is to build a system that keeps the enterprise data in a database and to provide services to users. You will be storing data in an SQLite database (called hospital.db) , and you will be writing code in Python (version 2.7) using the sqlite3 Python module to access it. Your code will implement a simple command line interface. You are free to implement a GUI interface instead but there will be no support nor bonus for doing that. 

Your project will be evaluated on the basis of 80% of the mark for implementing the functionalities listed in this specification; this component will be assessed in a demo session. Another 15% of the mark will be assigned for the documentation and quality of your source code and for your design document. 5% of the mark is assigned for the quality of your group coordination and the project break-down between partners.

### Database Specification

You are given the following relational schema (which is similar to the schema for Assignment 2 and is based on the application description in Assignment 1).

+ staff(staff_id, role, name, login, password )
  + Staff information. role can be one of the following: 'D', 'N', 'A' - standing for "doctor", "nurse", and "administration", respectively. login and password are the login and the password required to authenticate as a user of the system.
+ patients(hcno, name, age_group, address, phone, emg_phone)
  + Patient information. hcno =  "health care number".
+ charts(chart_id, hcno, adate, edate)
  + Chart information. A chart with id chart_id is associated with each stay of a patient with health care number hcno in the hospital. adate is the date of admission to the hospital, and edate is the date of discharge from the hospital. chart_id is unique among all charts, and a patient can have several charts corresponding to several periods of staying in the hospital.
+ symptoms(hcno, chart_id, staff_id, obs_date, symptom)
  + Information about observed symptoms. A row in this table records information about an observed symptom symptom, which was observed by a care staff member (doctor or nurse) with staff_id on the date obs_date; the symptom was observed for a patient who is associated with a chart chart_id.
+ diagnoses(hcno, chart_id, staff_id, ddate, diagnosis)
  + Information about diagnoses. A row in this table records information about a diagnosis diagnosis that was made by a doctor with staff_id on the date ddate for a patient who is associated with a chart chart_id.
+ medications(hcno, chart_id, staff_id, mdate, start_med, end_med, amount, drug_name)
  + Information about medications. A row in this table records information about a drug drug_name that was prescribed by a doctor with staff_id on date mdate and to be taken by a patient who is associated with a chart chart_id, from the start date start_med to the end date end_med in the amount specified in amount.
+ reportedallergies(hcno, drug_name)
  + Information about drug allergies provided by a patient with health care number hcno
+ drugs(drug_name, category)
  + Drug category information.
+ dosage(drug_name, age_group, sug_amount)
  + Drug dosage information. A row gives the suggested amount sug_amount for a drug drug_name and an age group age_group.
+ inferredallergies(alg, canbe_alg)
  + Lists all pairs of drugs for which it is known that if someone is allergic to the drug alg, the person may also be allergic to the drug canbe_alg
The SQL commands to create the tables of the system are given to you, and you must not change any table/column names since we will be testing your project with the given schema.

### Login Screen

The system has two classes of users:care staff (doctors and nurses) use the system to query and update information about patients, and administrative staff members use the system to create certain types of reports. All searches performed by users must be case-insensitive even though the data stored in tables could be in both uppercase and lowercase.

All users have to authenticate to the system using a login and a password (which should not be stored in plain text, but should be encrypted). After authentication, your system will present them with choices depending on their user role (indicated in the staff table). A main choice common to all users is the ability to logout from the system.

### System Functionalities

+ Doctors are able to perform all of the following tasks.
  + For a given patient, list all charts in the system ordered by adate (indicating also whether they are closed or open). The user should be given the option to select a chart. Once a chart is selected, all entries (symptoms, diagnoses, and medications) associated with that chart must be listed, and the result must be ordered by the date of the entries.
  + For a given patient and an open chart of the patient add an entry for symptoms. The date obs_date should be set to the current date and time.
  + For a given patient and an open chart of the patient add an entry for diagnosis. The date ddate should be set to the current date and time.
  + For a given patient and an open chart of the patient add an entry for medications. The date mdate should be set to the current date and time. Additional checks should be performed before adding the entry: (1) if the prescribed amount for the patient is larger than the recommended amount sug_amount for that drug and the patient's age group, a warning should be issued that contains the information about recommended amount for a patient for that age group, and the doctor should be given the choice to confirm his prescription or to change the amount. (2) If the patient could be allergic to the prescribed drug drug_name, a warning should be issued that contains the information about the reported allergy; the warning should display the name of the drug that the patient reported being allergic to, and, if that is not directly drug_name, the name of the drug D  should be dsiplayed, which the patient reported being allergic to and from which it can be "inferred" that the patient may also be allergic to drug_name.

+ Nurses are able to perform all of the following tasks.
  + Create a new chart for a patient at the time of admission to the hospital. At that point in time, the adate is filled with the current date and time, and the edate is filled with a NULL value, indicating an "open" chart. Before creating a new chart, the system should check whether there is already an open chart for that patient, and if so, provide the options to either close this chart before creating a new one, or not creating a new one. When creating a new chart, the system also must provide the functionality to add the patient information, if the patient information is not already in the system (from a previous stay in the hospital).
  + Close a chart when a patient is dismissed from the hospital. At that point in time, the edate is filled with the current date and time, indicating that the chart is closed.
  + Same as 1. for the doctors.
  + Same as 2. for the doctors.

+ An administrative staff user can perform the following tasks:
  + Create a report, that lists for each doctor the name and the total amount of each drug that the doctor prescribed in a specified period of time. (Drugs that he did not prescribe in that period of time should not be listed.)
  + For each category of drugs, list the total amount prescribed for each drug in that category in a specified period of time. The report should also contain a total for each category.
  + List for a given diagnosis all possible medications that have been prescribed over time after that diagnosis (over all charts). The list should be ordered by the frequency of the medication for the given diagnosis.
  + List for a given drug all the diagnoses that have been made before prescribing the drug (over all charts). The list should be ordered by the average amount of the drug prescribed for the diagnoses.


### Testing

At development time you will be testing your programs with your own data sets (make sure that it conforms to the project specification). At demo time we will be creating the database using the SQL statements for creating the tables mentioned above, and we will be populating it with our own test data set. Your application will be tested under a demo account (and not your account). You need to provide a mechanism for adding users with login and password.

The demo will be run using the source code submitted and nothing else. Make sure your submission includes every file that is needed. You will neither be able to change your code, nor use any file other than those submitted. This policy can be altered only in exceptional cases at the instructor's discretion and for a hefty penalty. The code will be executed under a demo account. As a test drill, you should be able to set up your application under someone else's account (in case of testing, this would be under a demo/TA account) within 3 minutes at most.

Every group will book a time slot convenient to all group members to demo their projects during one of the labs. At demo time, all group members must be present.The TA will be using a script to both create and populate the tables. The TA will be asking you to perform various tasks and show how your application is handling each task. A mark will be assigned to your demo immediately after the testing.
