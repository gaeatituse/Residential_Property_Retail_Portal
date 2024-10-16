from django.shortcuts import render
from django.contrib.auth.models import User
from myapp.models import UserProfile
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def home1(request):
  return render(request,'home1.html')
def home2(request):
  return render(request,'home2.html')
def loginpage(request):
  return render(request, 'login.html')
def signuppage(request):
  return render(request, 'signuppage.html')
def logoutuser(request):
  logout(request)
  return redirect('/loginpage')
def info(request):
  if request.user.is_authenticated:
        user_profile = request.user.userprofile
        first_name = user_profile.first_name
        last_name = user_profile.last_name
        phone_number = user_profile.phone_number
        email = request.user.email
        context = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone_number": phone_number
    }
        return render(request, 'info.html',context)
  else:
        return redirect('/loginpage')



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # User authentication successful
            login(request, user)
            
    
            return redirect('/info')
        else:
            return redirect('/loginpage')
    else:
        return HttpResponse(request.method)

def updatenumber(request):
   new_phone_number=request.POST['new_phone_number']
   confirm_phone_number=request.POST['confirm_phone_number']
   if new_phone_number!=confirm_phone_number:
      return redirect('/info')
   else:
      user_profile = request.user.userprofile
      user_profile.phone_number=new_phone_number
      user_profile.save()
      return redirect('/info')
def updateemail(request):
   new_email_address=request.POST['new_email_address']
   confirm_email_address=request.POST['confirm_email_address']
   if new_email_address!=confirm_email_address:
      return redirect('/info')
   else:
        user = request.user
        user.email = new_email_address
        user.username = new_email_address
        user.save()
        return redirect('/logoutuser')
def updatepassword(request):
   new_password=request.POST['new_password']
   confirm_password=request.POST['confirm_password']
   if new_password!=confirm_password:
      return redirect('/info')
   else:
        user = request.user
        user.set_password(new_password)
        user.save()
        return redirect('/logoutuser')
def signup(request):
    
    if request.method == 'POST':
        username = request.POST['email']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm_password']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        phonenumber = request.POST['phone_number']
        # Create a new user
        if confirmpassword == password:
          user = User.objects.create_user(username=username, email=email, password=password)
          profile = UserProfile.objects.create(user=user, first_name=firstname, last_name=lastname, phone_number=phonenumber)
          login(request, user)
          return HttpResponse('success')
        else:
          return HttpResponse('passwords not same')
    
    # If the request method is GET, render the signup page template
    return HttpResponse('failed')