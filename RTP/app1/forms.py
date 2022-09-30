import random
from django import forms
from app1.models import *
# *--star means import all the models
from app1.utils import sendtextmessage

class RegistrationForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)



    #otp validation
    def clean_otp(self):
        cno = self.cleaned_data['contact']
        #otp = self.cleaned_data['otp']
        #otp = self.cleaned_data['otp']
        otp = random.randint(100000,999999)
        message = '''Hello mr.soumya Gd Mng,Your Resume Will be Shortlisted,
                   Can You join our company,package @500000.00 per annum,
                   if you intrested Then Just send me your otp '''+ str(otp)
        sendtextmessage(message,cno)
        return otp
    class Meta:
        model = RegistrationModel
        exclude = ('status',)
        #exclude means not include

