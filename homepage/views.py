from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages 
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView

import datetime
import json

from .models import *
from .forms import BookingForm,SearchForm,ItemForm



def index(request):
    dt = datetime.datetime.now()
    day = dt.strftime("%A")
    categories = Category.objects.all()
    degustacion = SetMenu.objects.first()
    with open('datas/schedule.txt','r') as f:
        data = f.read()
    schedule = json.loads(data)
    opentoday= {'open': schedule[day]}
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            pax = form.cleaned_data['pax']
            hour = form.cleaned_data['hour']
            comment = form.cleaned_data['comment']
            customer = form.cleaned_data['customer']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            #password creation to fit User Model creation required fields
            pw = 'usr' + phone
            user = Customer.objects.create_user(username=customer, password = pw, email = email, phoneNumber = phone)
            new_res = Reservation(date=date, pax=pax, hour=hour, comment=comment, customer= user)
            new_res.save()
            subject = 'Reserva de ' + customer[:10] + '...'
            message = f'Fecha: {date}\nHora: {hour}\nPax: {pax}\nPhone: {phone}\nNota: {comment}'

            email = EmailMessage(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],
                reply_to=[email]
            )
            email.send(fail_silently=False)
            messages.success(request,f'Pedido de reserva por {customer} para {pax} personas a fecha {date.strftime("%d-%m-%y")} y hora {hour} RECIBIDA.')         
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BookingForm()
        
    return render(request,"homepage/index.html", {'categories': categories,
                                                  'degustacion': degustacion,
                                                  'opentoday':schedule[day],
                                                  'form':form,
                                                  'schedule': schedule})
@login_required
def manage(request):
    categories = Category.objects.all()
    return render(request,"homepage/manage-home.html", {'categories': categories})

class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "homepage/update_item.html"
    success_url = '/'
