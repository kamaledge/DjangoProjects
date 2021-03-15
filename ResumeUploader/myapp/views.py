from django import views
from django.urls import reverse
from django.contrib.auth import decorators
from django.contrib.auth.forms import UserCreationForm
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Resume
from .forms import ResumeForm
from django.views import View
from django.contrib import messages
from django.views.generic.edit import UpdateView
# from django.contrib.auth.models import User
from .forms import SignUpForm
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django import forms
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
# Create your views here.




class UserSignupView(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/User_form.html'
    success_url = '/success/'

class SignUpSuccess(TemplateView):
    template_name = 'myapp/success.html'


class UserLoginView(LoginView):
    template_name = 'myapp/login.html'
    # success_url = '/home/'

class UserLogoutView(LogoutView):
    template_name = 'myapp/logout_success.html'


def home(request):
    return render(request, 'myapp/home.html')


# access control
# decorators = [login_required(login_url='/login/')]
decorators = [login_required()]


@method_decorator(decorators, name='dispatch')
class Dashboard(View):
    def get(self, request):
        if not request.user.is_staff:
            form = ResumeForm()
            candidates = Resume.objects.filter(email=request.user.email )
            # candidates = Resume.objects.all()
            if candidates:
                return render(request, 'myapp/dashboard.html', {'candidates':candidates})
            return render(request, 'myapp/dashboard.html', {'form': form, 'candidates':candidates})
            
        form = ResumeForm()
        candidates = Resume.objects.all()
        # candidates = Resume.objects.all()
        return render(request, 'myapp/dashboard.html', {'form': form, 'candidates':candidates})


    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            # form = ResumeForm()
            messages.add_message(request,messages.SUCCESS, 'Your form has been submitted')
            messages.info(request, 'You can now login')
            # return render(request, 'myapp/home.html', {'form': form, 'msg':msg})
            return HttpResponseRedirect('/dashboard/')
        print('invalid')
        print(form.errors)
        msg = messages.add_message(request, messages.ERROR,'Something wrong with form data')
        messages.info(request, 'Please correct the data')
        print(msg)
        form = ResumeForm()
        return render(request, 'myapp/dashboard.html', {'form': form, 'msg':msg})


class CandidateView(View):
    def get(self, request, pk):
        id = pk
        candidate = Resume.objects.get(id=id)
        return render(request, 'myapp/candidate.html', {'candidate': candidate})

class CandidateUpdate(View):
    def get(self, request, pk):
        id = pk
        candidate = Resume.objects.get(id=id)
        form = ResumeForm(instance=candidate)
        return render(request,'myapp/candidate_update.html',{'form':form})

    def post(self, request, pk):
        id = pk
        candidate = Resume.objects.get(id=id)
        # print(candidate)
        form = ResumeForm(request.POST or None, request.FILES or None, instance=candidate)
        print(request.POST)
        print(request.FILES)
        # print('is form valid', form.is_valid)
        # print(form)
        if form.is_valid():
            form.save()
            print('form saved')
            candidate.save()
            print('record saved')
            # return render(request,'enroll/update_student.html',{'candidate':candidate})
            return HttpResponseRedirect('/dashboard/')
        print('form invalid')
        print('errors in form: ', form.errors)
        return HttpResponseRedirect(reverse('editcandidate',args=[id]))
