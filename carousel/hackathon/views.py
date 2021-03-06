# Django
from django.shortcuts import render
from django.contrib.auth import logout
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

# Django REST Framework
from django.views.generic import ListView
from django.views.generic import View
from rest_framework import viewsets, mixins

# Scripts
from scripts.linkedin import LinkedinOauthClient
from scripts.facebook import *

# Python
import oauth2 as oauth
import simplejson as json
import requests

# Models
from hackathon.models import *
from hackathon.forms import UserForm


profile_track = None
getLinkedIn = LinkedinOauthClient(settings.LINKEDIN_CLIENT_ID, settings.LINKEDIN_CLIENT_SECRET)
getFacebook = FacebookOauthClient(settings.FACEBOOK_APP_ID, settings.FACEBOOK_APP_SECRET)


class OfferView(ListView):
    model = Offer
    template_name = 'hackathon/offer.html'

    def get_queryset(self):
        qs = super(OfferView, self).get_queryset()
        qs = qs.filter(technologies=self.request.user.userprofile.recruit.technologies.all)
        qs = qs.exclude(pk__in=self.request.user.userprofile.recruit.accepted_offers.all)
        qs = qs.exclude(pk__in=self.request.user.userprofile.recruit.declined_offers.all)
        return qs


class AcceptOfferView(View):
    def get(self, request, *args, **kwargs):
        offer_id = int(request.GET['id'])
        recruit = request.user.userprofile.recruit
        recruit.accepted_offers.add(Offer.objects.get(pk=offer_id))
        recruit.save()
        return HttpResponse('ok')


class RejectOfferView(View):
    def get(self, request, *args, **kwargs):
        offer_id = int(request.GET['id'])
        recruit = request.user.userprofile.recruit
        recruit.declined_offers.add(Offer.objects.get(pk=offer_id))
        recruit.save()
        return HttpResponse('ok')


class RecruitView(ListView):
    model = Recruit
    template_name = 'hackathon/recruit.html'

    def get_queryset(self):
        qs = super(RecruitView, self).get_queryset()
        offers = Offer.objects.filter(recruiter=self.request.user.userprofile.recruiter)
        qs = qs.filter(accepted_offers__in=offers)
        return qs


def index(request):
    print "index: " + str(request.user)

    if not request.user.is_active:
        if request.GET.items():
            if profile_track == 'linkedin':
                code = request.GET['code']
                getLinkedIn.get_access_token(code)
                getLinkedIn.getUserInfo()

                try:
                    user = User.objects.get(username=getLinkedIn.user_id+'_linkedin')
                except User.DoesNotExist:
                    username = getLinkedIn.user_id+'_linkedin'
                    new_user = User.objects.create_user(username, username+'@madwithlinkedin.com', 'password')
                    new_user.save()
                    try:
                        profile =LinkedinProfile.objects.get(user = new_user.id)
                        profile.access_token = LinkedinProfile.access_token
                    except LinkedinProfile.DoesNotExist:
                        profile = LinkedinProfile(user=new_user, access_token=getLinkedIn.access_token, linkedin_user=getLinkedIn.user_id)
                    profile.save()
                user = authenticate(username=getLinkedIn.user_id+'_linkedin', password='password')
                login(request, user)

            elif profile_track == 'facebook':
                code = request.GET['code']
                getFacebook.get_access_token(code)
                userInfo = getFacebook.get_user_info()
                username = userInfo['first_name'] + userInfo['last_name']

                try:
                    user = User.objects.get(username=username+'_facebook')
                except User.DoesNotExist:
                    new_user = User.objects.create_user(username+'_facebook', username+'@madewithfacbook', 'password')
                    new_user.save()

                    try:
                        profile = FacebookProfile.objects.get(user=new_user.id)
                        profile.access_token = getFacebook.access_token
                    except:
                        profile = FacebookProfile()
                        profile.user = new_user
                        profile.fb_user_id = userInfo['id']
                        profile.profile_url = userInfo['link']
                        profile.access_token = getFacebook.access_token
                    profile.save()
                user = authenticate(username=username+'_facebook', password='password')
                login(request, user)

    else:
        if request.GET.items():
            user = User.objects.get(username = request.user.username)
            if profile_track == 'linkedin':
                code = request.GET['code']
                getLinkedIn.get_access_token(code)
                getLinkedIn.getUserInfo()

                try:
                    linkedinUser = LinkedinProfile.objects.get(user=user.id)
                except LinkedinProfile.DoesNotExist:
                    profile = LinkedinProfile(user = user, access_token = getLinkedIn.access_token, linkedin_user=getLinkedIn.user_id)
                    profile.save()



    context = {'hello': 'world'}
    return render(request, 'hackathon/index.html', context)


##################
#  API Examples  #
##################

def api_examples(request):
    context = {'title': 'API Examples Page'}
    return render(request, 'hackathon/api_examples.html', context)

#################
#  FACEBOOK API #
#################

def facebook(request):
    '''
    This is an example of getting basic user info and display it
    '''
    userInfo = getFacebook.get_user_info()
    return render(request, 'hackathon/facebookAPIExample.html', { 'userInfo' : userInfo})


##################
#  LINKEDIN  API #
##################

def linkedin(request):
    if getLinkedIn.is_authorized:
        content = getLinkedIn.getUserInfo()
    else:
        global profile_track
        profile_track = 'linkedin'
        linkedin_url = getLinkedIn.get_authorize_url()
        return HttpResponseRedirect(linkedin_url)

    context = {'title': 'linkedin example', 'content': content}
    return render(request, 'hackathon/linkedin.html', context)



######################
# Registration Views #
######################

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect('/hackathon/login/')
        else:
            print user_form.errors
    else:
        user_form = UserForm()


    return render(request,
            'hackathon/register.html',
            {'user_form': user_form, 'registered': registered} )

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                if hasattr(user.userprofile, 'recruiter'):
                    # TODO: To redirect to recruiter page.
                    return HttpResponseRedirect('/hackathon/recruits/')
                else:
                    return HttpResponseRedirect('/hackathon/offers/')
            else:
                return HttpResponse("Your Django Hackathon account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'hackathon/login.html', {})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/hackathon/login/')

def linkedin_login(request):
    global profile_track
    profile_track = 'linkedin'
    linkedin_url = getLinkedIn.get_authorize_url()
    return HttpResponseRedirect(linkedin_url)

def facebook_login(request):
    global profile_track
    profile_track = 'facebook'
    facebook_url = getFacebook.get_authorize_url()
    return HttpResponseRedirect(facebook_url)

