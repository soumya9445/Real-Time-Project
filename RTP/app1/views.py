from django.shortcuts import render,redirect
from app1.forms import RegistrationForm
from app1.models import RegistrationModel
from django.contrib.messages import success

# Create your views here.
def showindex(request):
    return render(request,'app1_temp/main.html')
#create a app and write the html it is the advantages is this total app operation wil be store in this app.
#after some issue u create a new aap then no problem u create a another aap and work ur operation.


def registration(request):
    rf=RegistrationForm(request.POST)
    if request.method == 'POST':
        if rf.is_valid():
            #rf.otp = 5475
            #rf.status = 'pending'#Not Write status in this place means this status write in default in models thats way
            rf.save()
            return redirect('user_otp')

        else:
            return render(request,'app1_temp/Registration.html',{'form':rf})
    else:
        return render(request,'app1_temp/Registration.html',{'form':rf})


def userotp(request):
    return render(request,'app1_temp/otp.html')


def validate_otp(request):#get--it will return only one object
    try:
        result = RegistrationModel.objects.get(contact=request.POST.get('t1'),otp=request.POST.get('t2'))
        #print(result.status)
        if result.status == 'pending':
            result.status == 'approved'#updating the record
            result.save()
            success(request,'Thank You For Registration ')
            return redirect('conformation')
        elif result.status == 'approved':
            success(request,'Your Registration Is Already Approved')
            return redirect('conformation')
        #elif result.status

    except RegistrationModel.DoesNotExist:
        message='Sorry This User Is Invalid'
        return render(request,'app1_temp/otp.html',{'message':message})



def conformation(request):
    return render(request,'app1_temp/conformation.html')


def login(request):
    return render(request,'app1_temp/login.html')

#use session
def logincheck(request):
    try:
        result=RegistrationModel.objects.get(email=request.POST.get('u1'),password=request.POST.get('u2'))
        #your status is pending then write and showing some error message
        if result.status == 'pending':
            return render(request,'app1_temp/login.html',{"error":"Sorry Your Registration Is Not Approved"})
        #your status is closed then write and showing some error message
        if result.status == 'closed':
            return render(request,'app1_temp/login.html',{'error1':'Sorry Your Account Is Closed'})
        #your status is approved then showing this message--welcome to profile page
        request.session['contact']=result.contact
        request.session['name']=result.name
        return  redirect('view_profile')
    except RegistrationModel.DoesNotExist:
        return render(request,'app1_temp/login.html',{"error":"Invalid User"})
def view_profile(request):
    return render(request,'app1_temp/view_profile.html')


def logout(request):
    #delete the session
    del request.session['contact']
    del request.session['name']
    return redirect('main')