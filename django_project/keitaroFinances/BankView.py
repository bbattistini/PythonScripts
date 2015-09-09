from django.http import HttpResponse
from django.shortcuts import render
from keitaroFinances.models import Bank
import datetime

from .forms import BankForm

def hello(request):
    if request.method == 'POST':
        form = BankForm(request.POST)
        
        if form.is_valid():
            
            bank = Bank()
            bank.bank_name = form.cleaned_data["bank_name"]
            bank.date_created = datetime.datetime.today()

            try:
                bank.save()
                return HttpResponse("ok")
            except e:
                return HttpResponse(e.message)
    else:
        form = BankForm()
        banks = Bank.objects.all()
        return render(request,'keitaroFinances/BankForm.html',{'form':form, "banks":banks})
