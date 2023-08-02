class Patient(object):
	patient_counter = 0
	def __init__(self, name, allergies, bed_number):
		Patient.patient_counter += 1
		self.id = Patient.patient_counter
		self.allergies = allergies
		self.bed_number = bed_number