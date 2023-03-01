from django.urls import path
from . import views


#app_name - will be used as erf in HTML to use methods
app_name = 'orders'

# Endpoints of movies app must be specifieds in urlpatterns:
# movies/
# moview/1/details
urlpatterns = [
    path("", views.index, name=f"index"),
    #<> - to use parametr
    path('<int:order_id>', views.details, name='detail')
]
