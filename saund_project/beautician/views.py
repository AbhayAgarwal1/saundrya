from django.shortcuts import render

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .form import UserForm
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index(request):
    return render(request, 'beautician/home.html', )


def UserFormView(request):
    form_class = UserForm
    template_name = 'beautician/register.html'

    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()

        user = authenticate(username=username, password=password)

        if user is not None:

            if user.is_active:
                login(request, user)
                return redirect('index')

    return render(request,template_name, {'form': form})

