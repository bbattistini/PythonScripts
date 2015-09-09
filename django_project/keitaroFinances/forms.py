from django import forms

class BankForm(forms.Form):
    bank_name = forms.CharField(label="Bank Name", max_length=50)

