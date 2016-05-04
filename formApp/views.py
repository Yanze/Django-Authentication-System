from django.shortcuts import render, redirect
# from formApp.forms import ContactForm
from django.views.generic import View
from django.contrib.auth import forms, login, authenticate

# Create your views here.
# def contact_form(request):
#     form = ContactForm()
#     return render(request, 'views/index.html', {'form': form})
#
# def add(request):
#     form = ContactForm(request.POST or None)
#     if form.is_valid():
#         print(form.cleaned_data['full_name'])
#         return redirect('show')
#     else:
#         return redirect('index')

def show(request):
    return render(request, 'views/success.html')

class Register(View):
    # UserCreationForm is a built-in form from the django.contrib.auth forms module
    form = forms.UserCreationForm
    def get(self, request):
        context = {'form': self.form()}
        return render(request, 'views/register.html', context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
        else:
            # context = {'form': form}
            return redirect('accounts-register')

class Login(View):
    form = forms.AuthenticationForm
    def get(self, request):
        context = {'form': form}
        return render(request, 'accounts/login.html', context)
