from django.contrib import admin
from Modelos.models import *

from import_export import resources
from import_export.admin import ImportExportActionModelAdmin

#####################################################################

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportActionModelAdmin):
    resource_class = CategoryResource
    list_display = (
        "usuario",
        "date_create",
        "name",
    )

    search_fields = (
        "usuario",
        "date_create",
        "name",
    )
    list_per_page = 10
    exclude = ("usuario", "user_update",)    


#####################################################################

admin.site.register(Category, CategoryAdmin)