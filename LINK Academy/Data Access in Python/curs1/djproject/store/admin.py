from django.contrib import admin
from .models import Category, Product
from django.http import HttpResponse
import csv
# Register your models here.

def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  f'attachment; filename="{modeladmin.model._meta.verbose_name}.csv"'
    writer = csv.writer(response)
    #writer.writerow(('Titlu', 'Slug', 'Pret', 'Description'))
    opts = modeladmin.model._meta
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    writer.writerow([field.verbose_name for field in fields])
    objects =  list(queryset)
    for obj in objects:
        data = []
        for field in fields:
            value = getattr(obj, field.name)
            data.append(value)
        writer.writerow(data)
    return response


def export_products_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] =  'attachment; filename="products.csv"'
    writer = csv.writer(response)
    writer.writerow(('Titlu', 'Slug', 'Pret', 'Description'))
    products =  list(queryset)
    for prod in products:
        writer.writerow((prod.name, prod.slug, prod.price, prod.description))
    return response

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = { 
        'slug': ('name',)
    }
    search_fields = ('name',)
    list_filter = ('name',)
    actions = [export_to_csv]



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = { 
        'slug': ('name',)
    }
    search_fields = ('name','price', 'description')
    list_filter = ('category', 'name','price', 'description')
    actions = [export_to_csv]





