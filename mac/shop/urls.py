from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
     path("",views.index,name="Shophome"),
     path("about/",views.about,name="AboutUS"),
     path("contact/",views.contact,name="ContactUS"),
     path("tracker/",views.tracker,name="TrackingStatus"),
     path("search/",views.search,name="AboutUS"),
     path("productview/",views.prodview,name="Productview"),
     path("checkout/",views.checkout,name="Checkout"),
]

   
