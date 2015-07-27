from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .forms import OrderForm
from .models import Order

# Create your views here.
def home(request):
    return render(request, 'mcdelivery/home.html')
    
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    
class OrderList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Order
    
    def get_queryset(self):
        folder = self.kwargs['folder']
        if folder == '':
            return Order.objects.all()
        else:
            return Order.objects.filter(folder__title__iexact=folder)

class OrderDetail(DetailView):
    model = Order
    
class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm

class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')