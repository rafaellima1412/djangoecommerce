# coding=utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
#posso fazer por classe exemplo index
from django.views.generic import View, TemplateView

from .form import ContactForm
#classe chamamvel do index
class IndexView(TemplateView):
    #usando o template viem posso chamar assim
    template_name = 'index.html'


index = IndexView.as_view()

#teste
def contact(request):
    success = False
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.send_mail()
        success = True
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
