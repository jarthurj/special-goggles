from django import forms

class CourseForm(forms.Form):
	course_name = forms.CharField(label="Course Name", max_length=50)
	course_description = forms.CharField(label="Course Description", max_length=100)