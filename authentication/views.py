from django.shortcuts import render


# Create your views here.
def login_user(request):
    return render(request, 'base.html', {})


def logout_user(request):
    return render(request, 'base.html', {})


def register_user(request):
    return render(request, 'base.html', {})
