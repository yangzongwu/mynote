from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from . import models
from django.core.urlresolvers import reverse_lazy
# Create your views here.
'''
def index(request):
    return render(request,'index.html')
'''
'''
from django.http import HttpResponse
class CBview(View):
    def get(self,request):
        return HttpResponse("class are cool")
'''

class IndexView(TemplateView):
    template_name='index.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme']='BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name='schools'
    model= models.School
    # ListView return lower()_list :school_list
class SchoolDetailView(DetailView):
    context_object_name='school_detail'
    model= models.School
    template_name='basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields=('name','principal','location')
    model= models.School

class SchoolupdateView(UpdateView):
    fields=('name','principal')
    model= models.School

class SchoolDeleteView(DeleteView):
    model= models.School
    success_url=reverse_lazy('basic_app:list')
