from django.urls import path
from . import views

# Endpoints of movies app must be specifieds in urlpatterns:
# movies/
# moview/1/details
urlpatterns = [
    path("", views.index, name="index")
]
