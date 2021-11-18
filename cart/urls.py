from django.urls import path
from .views import CartDetail, cart_add, cart_remove

app_name = "cart"

urlpatterns = [
    path("", CartDetail.as_view(), name="detail"),
    path("add/<slug>/", cart_add, name="add"),
    path("remove/<slug>/", cart_remove, name="remove"),
]
