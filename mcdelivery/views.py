from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from .models import Order

# Create your views here.
def order_list(request):
    allorders = Order.objects.all()
    responsetext = ""
    for order in allorders:
        url = reverse('detail', args=str(order.id))
        responsetext += "<a href='"+ url + "'>"
        responsetext += "<h1>" + order.customer + "</h1></a>"
        responsetext += "<h1>" + "Order number: " + str(order.id) + "</h1>"
        responsetext += "<h2>" + order.order + "</h2>"
        responsetext += "<h2>" + order.special_request + "</h2>"
        responsetext += "<h4>" + str(order.contact_number) + "</h4>"
        responsetext += "<h4>" + order.address + "</h4>"
    return render(request, 'mcdelivery/index.html', {'orders': allorders})
    
def order(request, order_id):
    order = Order.objects.get(id=order_id)
    responsetext = ""
    responsetext += "<h1>" + order.customer + " Order number: " + str(order.id) + "</h1>"
    responsetext += "<h2>" + order.order + "</h2>"
    responsetext += "<h2>" + order.special_request + "</h2>"
    responsetext += "<h4>" + str(order.contact_number) + "</h4>"
    responsetext += "<h4>" + order.address + "</h4>"
    return HttpResponse(responsetext)
