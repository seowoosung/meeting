from app.forms import SignUpForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
           user_name = form.cleaned_data['userName']

           return HttpResponseRedirect('/app/profile/')

    else:
        form = SignUpForm()


    return render(request, 'app/app.html', {'form' : form})

class ProfileView(TemplateView):
    template_name = "app/profile.html"