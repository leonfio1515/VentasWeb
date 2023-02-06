from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

##########################################################################


class Users(UserAdmin):
    list_display = (
        "username",
        "is_active",
        "is_staff",
        "id",
    )

    list_per_page = 25
    exclude = ("user_update", "date_update", "usuario",)

##########################################################################


admin.site.register(Usuario, Users)
