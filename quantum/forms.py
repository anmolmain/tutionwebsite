from django import forms
from .models import LowerSchoolStudent
from .models import MiddleSchoolStudent
from .models import HighSchoolStudent
from .models import Contact
from .models import HomePageContact

class HomePageContactForm(forms.ModelForm):
    class Meta:
        model = HomePageContact
        fields =  '__all__'

class HighSchoolStudentForm(forms.ModelForm):
    class Meta:
        model = HighSchoolStudent
        fields = '__all__'

class LowerSchoolStudentForm(forms.ModelForm):
    class Meta:
        model = LowerSchoolStudent
        fields = '__all__'

class MiddleSchoolStudentForm(forms.ModelForm):
    class Meta:
        model = MiddleSchoolStudent
        fields = '__all__'
        

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
