from django.shortcuts import render
from django.views.generic import TemplateView
from test_project.models import TestJSON
from django.shortcuts import redirect

def index(request):
    context = {
        'title': 'Home',
    }
    return render(request, 'index.html', context = context)

def results(request):
    json_data = TestJSON.objects.all()

    context = {
        'title': 'Results',
        'json_data': json_data,
    }
    return render(request, 'results.html', context = context)

class HomeView(TemplateView):
    template_name = 'test_form2.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        d = dict(request.POST.items())
        if 'csrfmiddlewaretoken' in d: del d['csrfmiddlewaretoken']
        TestJSON.objects.create(data=d)
        return redirect('/results')

