from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import messages
import uuid
from .helper import send_forget_password_mail, send_message
from .models import *

# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "homepage.html")

class RegisterView(View):
    template_name = 'signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            print('Already logged in..')
            return HttpResponseRedirect('/')
        form = RegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to RegisterForm()
        form = RegisterForm(request.POST)
        sex = request.POST['gender'].lower()
        if form.is_valid():
            # create a User account
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            cfpassword = form.cleaned_data['cnfpassword']
            emailid = form.cleaned_data['email'].lower()
            f_name = form.cleaned_data['firstname'].lower()
            l_name = form.cleaned_data['lastname'].lower()
            p_num = form.cleaned_data['ph_number']
            add = form.cleaned_data['address']
            
            print(f_name, l_name, user_name, sex)

            try:
                user_exist = User.objects.get(username=user_name)
            except:
                user_exist = None
            if user_exist:
                messages.error(request, "Username already exist..!!")
                return HttpResponseRedirect('register')

            try:
                pnum_exist = User.objects.get(ph_number=p_num)
            except:
                pnum_exist = None
            if pnum_exist:
                messages.error(request, "Contact Number already exist..!!")
                return HttpResponseRedirect('register')
            
            try:
                email_exist = User.objects.get(email=emailid)
            except:
                email_exist = None
            if email_exist:
                messages.error(request, "EmailID already exist..!!")
                return HttpResponseRedirect('register')
            
            try:
                if password == cfpassword:
                    print("pass matched")
                    new_user = User(username=user_name, email=emailid,
                                    first_name=f_name, last_name=l_name, 
                                    )
                    new_user.set_password(password)
                    new_user.save()
                    print("new user created")
                    profile = User_profile(username=user_name, first_name=f_name,
                                        last_name=l_name, ph_number = p_num,
                                    address = add, gender = sex, email_id = emailid)
                    profile.save()
                    print(profile)
                    print("new user profile created")
                    return HttpResponseRedirect('/login')
                else:
                    messages.error(request, "Password doesn't match..!!")
                    return HttpResponseRedirect('register')
            except:
                messages.error(request, "Something went's wrong.!!")
                return HttpResponseRedirect('register')
        return HttpResponse('This is Register view. POST Request.')

class LoginView(View):
    template_name = 'signin.html'

    def get(self, request):
        if request.user.is_authenticated:
            # logout(request)
            return HttpResponseRedirect('/')
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        # pass filled out HTML-Form from View to LoginForm()
        print("===> in first login view")
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                obj = User_profile.objects.get(user=user)
                login(request, user)
                print('success login')
                return HttpResponseRedirect('/')
            else:
                messages.error(
                    request, "Your username or password is incorrect")
                return HttpResponseRedirect('login')
        return HttpResponse('This is Login view. POST Request.')

def forget_password(request):
    try:
        if request.method == 'POST':
            email_obj = request.POST.get('email')
            if not User.objects.filter(email=email_obj).first():
                print("User Not Found!!")
                messages.error(request, "No User Found!!")
                return HttpResponseRedirect('/forget_password/')
            user_obj = User.objects.get(email=email_obj)
            print(user_obj.email)
            token = str(uuid.uuid4())
            profile_obj = User_profile.objects.get(user=user_obj)
            profile_obj.token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email, token)
            messages.success(request, "Email Sent")
            return HttpResponseRedirect('/forget_password/')

    except Exception as e:
        print(e)
        messages.error(request, "Something went's wrong try again...!!")
        return HttpResponseRedirect('/forget_password/')
    return render(request, 'forget_password.html')


def change_password(request, token):
    context = {}
    try:
        profile_obj = User_profile.objects.filter(token=token).first()
        print("profile", profile_obj)
        print("profile id", profile_obj.user.id)
        context = {'user_id': profile_obj.user.id}
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_newpassword')
            user_id = request.POST.get('user_id')
            if new_password != confirm_password:
                messages.success(request, "Password not match!!")
                return HttpResponseRedirect(f'/change_password/{token}/')
            user_obj = User.objects.get(id=user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return HttpResponseRedirect('/login')
    except Exception as e:
        print(e)
        messages.error(request, "Something went's wrong try again...!!")
        return HttpResponseRedirect(f'/change_password/{token}/')
    return render(request, 'change_password.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

@login_required
def base(request):
    print(request.user)
    return render(request, 'base.html')



#api 

# class UserViewset(viewsets.ModelViewSet):
#     queryset = User_profile.objects.all().order_by("first_name")
#     serializer_class = UserSerializers


    