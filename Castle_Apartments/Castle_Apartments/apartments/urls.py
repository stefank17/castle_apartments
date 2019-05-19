from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('sell_apartment', views.sell_apartment, name="sell_apartment"),
    path('<int:apartment_id>', views.get_apartment_by_id, name="apartment_details"),
    path('<int:id>/purchase', views.purchase_apartment, name="purchase_aparment"),
    path('<int:id>/purchase/finish', views.delete_apartment, name='delete_apartment'),
    path('<int:id>/delete', views.delete_apartment, name="delete_apartment")
]
