
from django.shortcuts import render
from django.views.generic import ListView
from django.template import RequestContext, loader
from i_system_web.models import Departs
from django.core.urlresolvers import reverse
from django.views.generic import CreateView



# Create your views here.
class ListDepartsView(ListView):

      model = Departs
      template = 'departs_list.html'

class CreateDepartsView(CreateView):
      fields = ['name_dep']
      model = Departs
      template = 'departs_add.html'
      def get_success_url(self):
            return reverse('departs-list')