#render is used to render templates
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Order

# Create your views here.

# Represents main page of movies app. Index always must accept request


def index(request):
    #Allow to get all object with this type from DB
    orders = Order.objects.all()
    MY_RENDER = render(request, "orders/index.html", {"orders" : orders})
    return MY_RENDER
    #return HttpResponse(output)

def details(request, order_id):
    # try: 
    #     order = Order.objects.get(id=order_id)
    #     print(order)
    #     return render(request, "orders/details.html", {"order" : order})
    # except Order.DoesNotExist:
    #     raise Http404()
    order = get_object_or_404(Order, id=order_id)
    return render(request, "orders/details.html", {"order" : order})
