Healthcare Record Keeper- Project Documentation

1.	Real World Problem – Basic patient record management:-
Basic patient record mismanagement is one of the genuine real world problems. Many clinics, small hospitals, and community health centers need a simple way to organize essential information about their patients. Without proper record-keeping, it becomes hard to access patient histories, track treatment progress, and coordinate care—all of which can lead to errors, inefficiency, and poorer health outcomes. This problem is fundamental, practical, and universally relevant in healthcare. Solving it helps improve care quality, streamline clinic operations, and minimize mistakes. There is a need for a simple user friendly tool that allows individuals to maintain the healthcare records efficiently.
2.	Objectives and Expected Outcomes:-
Objectives:-
•	To design a python based system that collects and manages healthcare records of patients.
•	Centralize patient information in one digital location.
•	Providing a straightforward method to add new patients and review the existing records and update the treatment whenever changes occur.
•	Reduce time and effort spent manually, thus improving efficiency.
•	Introduce digital record keeping to the users worldwide.
Expected outcomes:-
•	A working python program that:
o	Accepts patient record (such as name, age, ailment and treatment plan) as input.
o	Uses lists, functions and loops for data processing.
o	Adds, updates and makes it possible to view record of the patients.
Thus, helps with record management.
•	Consistent and reliable source for storing information for further treatment decisions.
•	Increased productivity.

3.	Applied Concepts Learned in the Class to Design the Solution.
•	Lists and dictionaries used to store the patient record.
•	Functions used to perform modular and reusable calculations.
•	Loops and iterative statement used to choose what the user wants (to add, view or update patient record).
•	User input handling used for dynamic data collection.
•	Problem-solving and structured programming techniques.

4.	Usage of Appropriate Tools and Programming Techniques:-
The project uses only the Python Standard Library.
Key techniques include:
•	Modular programming (functions).
•	Iterative input collection (loops).
•	Lists based data storage.
•	Conditional logic for choosing the option what the user wants (to add, view or update patient record).
•	Console-based user interactions.

5.	Follow a Structured Development Process:-

A.	Problem definition:
In many healthcare facilities, especially smaller clinics or resource-limited environments, patient data such as names, ages, ailments, and treatments are often recorded manually or in unstructured formats. This leads to difficulties in retrieving up-to-date information, higher chances of errors, loss of data, inefficient care coordination, and delays in treatment decisions. This system aims to solve this problem by providing a basic yet effective digital solution.
B.	Requirement Analysis:
•	The system must accept patient record, that is, patient’s name, age, ailment and treatment.
•	It must allow the user to view any patient record.
•	It must allow the user to update the treatment plan of any patient.
•	It must display results in a structured format.
•	Should be simple and user-friendly.
•	Must run on any system with Python installed.
•	Code must be readable, modular, and maintainable.
C.	Top-Down Design and Modularization:

Main modules-
1.	Input module= Collects a value, from 1 to 4 from the user, if the user wants to 1.add a new patient’s record, 2.view a patient’s record, 3.update the treatment plan or 4. Close.
2.	Processing module= 
•	add_patient(name, age, ailment, treatment) function takes input of the patient’s name, age, ailment and treatment and, stores and inserts it in a list.
•	view_patients() function to display all patient records.
•	update_treatment_for_patient(target_name, new_treatment) function to update the treatment plan of the patient.
3.	Output module= Displays the desired output.
Top-Down Approach:
•	Begin with the main problem: "Patient Record”.
•	 Break into smaller tasks:
Input→ Processing → Analysis→ Output
•	Implement each component step-by-step.

D.	Algorithm Development:

Algorithm: Patient Record Keeper
Step 1: Start.
Step 2: print “Program: Patient Health Record Keeper.”
Step 3: Create an empty list to store patient record, named as patients.
Step 4: Define function add_patient with parameters name, age, ailment and           treatment.
a.	Accept name, age, ailment, treatment of the function in a dictionary named as patient
b.	Insert this dictionary into the list named as patients, using append function.
c.	print f“Patient {name} added.”
Step 5: Define a function view_patients with no parameters, to display all patients records.
a.	Check if the length of the list patients is equal to zero then, print “No Patients Recorded”.
b.	Otherwise, take a for loop using enumerate built-in function, with patients as parameter, to print all the details of the patients as stored.
Step 6:  Define a function update_treatment_for_patient, with target_name and new_treatment as parameters.
a.	Take a for loop in patients.
b.	Check if the patients name is equal to the target name, proceed to change the earlier treatment of the patient with the new treatment then print the updated treatment plan and name of the patient.
c.	Otherwise, print f“Could not find patient named {target_name}.”
Step 7:  Now, while this loop is true,
a.	Print “\n==Patient Management System==”
b.	Print “1) Add a new patient.”
c.	Print “2) Show all patient records.”
d.	Print “3) Change a patient’s treatment.”
•	Take an input from the user to select an option from 1 to 4.
•	If option is equal to 1, then accept the input of the patients name, age, ailment and treatment. Call the function add_patient.
•	If option is equal to 2, then call the function view_patients.
•	If option is equal to 3, then accept the name and the new treatment of the patient. Call the function update_treatment_for_patient.
•	If the option is 4, then print “Program closed. Have a great day!”. Use break function.
•	Otherwise print “Invalid option. Please choose a number from 1 to 4.”
Step 8: End.

E.	Implementation:
•	Uses lists for data storage.
•	Uses loops for input and analysis.
•	Uses functions for adding, viewing or updating patient record.
•	Uses conditional statement.

F.	Testing and Refinement:

Test cases-
Test case	Input	Expected Outcome
1.	Add patient record:
Name= “Alice", Age = 40, Ailment = "Headache", Treatment = "Painkillers"	Patient record is added to the list.
2.	View all patient records:
Several patients added with valid information.	Patient details displayed in a clear, numbered list format.
3.	Update Existing Patient Treatment:
Existing patient name and new treatment details.	Patient's treatment updated and success message shown.
4.	Prevent Duplicate Patient Addition (if implemented):
Add patient with same name twice.	Second addition rejected or flagged with appropriate message.


Refinement Activities -

•	Improved category descriptions.
•	Added threshold-based analysis.
•	Enhanced textual output formatting.
•	Ensured code readability and modularity.
