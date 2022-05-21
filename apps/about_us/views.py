from django.shortcuts import render
from django.views.generic import View


class AboutUs(View):
    def get(self, request):
        return render(request, 'about-us/about.html', {})
