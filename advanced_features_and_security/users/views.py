from django.views import View
from django.http import HttpResponse

class RegisterView(View):
    def get(self, request):
        return HttpResponse("Register page")

class ProfileView(View):
    def get(self, request):
        return HttpResponse("Profile page")