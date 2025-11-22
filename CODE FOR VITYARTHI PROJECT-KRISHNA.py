print("Program: Patient Health Record Keeper.")

patients = []

def add_patient(name, age, ailment, treatment):
    patient = {"name": name, "age": age, "ailment": ailment, "treatment": treatment}
    patients.append(patient)
    print(f"Patient {name} added.")

def view_patients():
    if len(patients) == 0:
        print("No Patients Recorded.")
    else:
        for i, patient in enumerate(patients):
            print(f"{i+1}. Name: {patient['name']}, Age: {patient['age']}, Ailment: {patient['ailment']}, Treatment: {patient['treatment']}")

def update_treatment_for_patient(target_name, new_treatment):
    for patient in patients:
        if patient["name"] == target_name:
            patient["treatment"] = new_treatment
            print(f"Updated treatment for {target_name}.")
            break
    else:
        print(f"Could not find patient named {target_name}.")


while True:
    print("\n=== Patient Management System ===")
    print("1) Add a new patient")
    print("2) Show all patient records")
    print("3) Change a patient's treatment")
    print("4) Close the program")

    option = input("Select an option (1–4): ")

    if option == "1":
        name = input("Patient name: ")
        age = input("Patient age: ")
        ailment = input("Ailment/Issue: ")
        treatment = input("Recommended treatment: ")
        add_patient(name, age, ailment, treatment)

    elif option == "2":
        view_patients()

    elif option == "3":
        target_name = input("Name of the patient to update: ")
        new_treatment = input("Enter the new treatment: ")
        update_treatment_for_patient(target_name, new_treatment)

    elif option == "4":
        print("Program closed. Have a great day!")
        break      
    else:
        print("Invalid option. Please choose a number from 1 to 4.")

