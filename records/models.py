from django.db import models

# Create your models here.

class Patient(models.Model):
	patient_id = models.IntegerField('patient ID', default=0)
	patient_name = models.CharField('Name of patient', max_length=200)
	patient_age = models.IntegerField('Age of patient')
	date_registered = models.DateTimeField('Date of Registration')

	def __str__(self):
		return str(str(self.patient_id) +' ' + self.patient_name)

class Appointment(models.Model):
	date_of_appointment = models.DateTimeField('Date of appointment')
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	complaints = models.TextField('Complaints')
	diagnosis = models.TextField('Diagnosis')
	care_plan = models.TextField('Care plan')

	def __str__(self):
		return str(self.date_of_appointment) + ' '  + str( self.patient)