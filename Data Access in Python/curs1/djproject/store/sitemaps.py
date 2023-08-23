from django.contrib.sitemaps import Sitemap
from .models import Product


class ProductSitemap(Sitemap):
    def items(request):
        all_prods = Product.objects.all()
        return all_prods