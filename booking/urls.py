from django.urls import path 
from booking import views 

app_name = "booking"

urlpatterns = [
    path("check_room_availability/", views.check_room_availability, name="check_room_availability"),

    # Ajax
    path("add_to_selection/", views.add_to_selection, name="add_to_selection"),
    
]