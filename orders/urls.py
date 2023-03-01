from django.urls import path
from . import views

# Endpoints of movies app must be specifieds in urlpatterns:
# movies/
# moview/1/details
urlpatterns = [
    path("", views.index, name="orders_index"),
    #<> - to use parametr
    path('<int:order_id>', views.details, name='order_detail')
]
