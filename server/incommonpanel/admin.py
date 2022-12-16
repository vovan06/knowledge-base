from django.contrib import admin

from .models import Catalog, Document


class CatalogAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title',
    )
    list_display = (
        'id', 'title',
    )
    search_fields = (
        'id', 'title',
    )
    readonly_fields = (
        'id', 
    )


class DocumentAdmin(admin.ModelAdmin):
    fields = (
        'id', 'title', 'file', 
        'private_access', 'created_at', 
        'catalog',
    )
    list_display = (
        'id', 'title', 'file', 
        'private_access', 'catalog',
    )
    list_editable = (
        'private_access',
    )
    search_fields = (
        'id', 'title', 'private_access', 
        'created_at', 'catalog',
    )
    readonly_fields = (
        'id', 'created_at', 
    )

admin.site.register(Catalog, CatalogAdmin)
admin.site.register(Document, DocumentAdmin)
