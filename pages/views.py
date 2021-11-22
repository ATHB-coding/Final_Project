from django.views.generic import ListView
from products.models import Product


class HomePageView(ListView):
    template_name = "home.html"

    def get_queryset(self):
        queryset = Product.available.all()

        return queryset
