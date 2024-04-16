from django.shortcuts import render

# Create your views here.

def home(request):

    context = {
            'home_active': 'active',
            'home_disabled': 'disabled',
    }
    return render(request, 'core/home.html', context)

def about(request):
    pass


def feedback(request):
    pass

def loan(request):
    pass

def loan_predict(request):
    pass
