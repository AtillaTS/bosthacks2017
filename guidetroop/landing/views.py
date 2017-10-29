from django.shortcuts import render
from django.http import HttpResponseRedirect
from landing.forms import HomeForms
from django.views.generic import TemplateView
from landing.pydata import data

def index(request):
    return render(request, 'landing/header.html')

class HomeView(TemplateView):
    template_name = "landing/header.html"

    def get(self, request):
        form = HomeForms()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForms(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']

        text = data(text)

        args = {'form': form, 'text': text}
        return render(request, self.template_name, args)
