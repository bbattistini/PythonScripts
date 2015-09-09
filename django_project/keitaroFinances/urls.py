from django.conf.urls import url
from . import views
from . import BankView

urlpatterns = [
    url(r'Bank/$',BankView.hello, name='hello'),
    url(r'$',views.index, name ='index'),
]
