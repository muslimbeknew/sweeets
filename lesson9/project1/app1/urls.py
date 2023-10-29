from .views import homePage
from django.urls import path,include

urlpatterns = [
    path('',homePage),
    path('<son>/',homePage)

]
