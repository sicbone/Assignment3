from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .forms import OrderForm
from .models import Order
from accounts.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
def home(request):
    return render(request, 'mcdelivery/home.html')
    
class OrderCreate(CreateView):
    model = Order
    form_class = OrderForm
    
    def form_valid(self, form):
        curruser = UserProfile.objects.get(user=self.request.user)
        form.instance.user = curruser
        form.save()
        return super(OrderCreate, self).form_valid(form)
        
class OrderList(ListView):
    #https://docs.djangoproject.com/en/1.7/topics/class-based-views/generic-display/
    model = Order
    queryset = Order.objects.all()
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderList, self).dispatch(*args, **kwargs)
    
    def get_queryset(self):
        curruser = UserProfile.objects.get(user=self.request.user)
        
        folder = self.kwargs.get('folder',"")
        if folder == '':
            self.queryset = Order.objects.filter(user=curruser)
            return self.queryset
        else:
            self.queryset = Order.objects.all().filter(user=curruser).filter(folder__title__iexact=folder)
            return self.queryset
            
    def get_context_data(self, **kwargs):
        context = super(OrderList, self).get_context_data(**kwargs)
        context['total'] = self.queryset.count()
        #provided so that the avatar can be displayed in base.html
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context

class OrderDetail(DetailView):
    model = Order
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderDetail, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(OrderDetail, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context
    
class OrderUpdate(UpdateView):
    model = Order
    form_class = OrderForm
    
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(OrderUpdate, self).dispatch(*args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super(OrderUpdate, self).get_context_data(**kwargs)
        context['curruser'] = UserProfile.objects.get(user=self.request.user)
        return context


class OrderDelete(DeleteView):
    model = Order
    success_url = reverse_lazy('order_list')
