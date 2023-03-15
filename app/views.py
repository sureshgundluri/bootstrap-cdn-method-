from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'homepage.html')

def Registration(request):
    return render(request,'Registration.html')

def loginpage(request):
    return render(request,'loginpage.html')
