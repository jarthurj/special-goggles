from patient import Patient

class Hospital(object):

	def __init__(self, name, capacity):
		self.name = name
		self.open_beds = [n for n in range(capacity)]
		self.patients = []
		self.capacity = capacity

	def admit(self, patient_name, patient_allergies):
		if len(self.open_beds) <= 0:
			print("NO OPEN BEDS")
		else:
			new_patient = Patient(patient_name, patient_allergies, self.open_beds[0])
			self.patients.append(new_patient)
			del self.open_beds[0]
			print("PATIENT ADMITTED")

	def discharge(self, patient_id):
		for x, patient in enumerate(self.patients):
			if patient.id == patient_id:
				self.open_beds.insert(patient.bed_number)
				self.open_beds.sort()
				patient.bud_number = None
				del self.patients[x]
				print("patient discharged")

		print("error")


