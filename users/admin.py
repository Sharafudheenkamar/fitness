from django.contrib import admin
from.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .forms import *
# Register your models here.

class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "phoneno",
                    "first_name",
                    "photo",
                    "email",
                    "dob",
                    "gender",
                    "place",

                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "subscriptionplan",
                    "user_type",
                    "is_active",
                    "is_superuser",
                )
            },
        ),
    )
    # add_fieldsets = (
    #     (
    #         None,
    #         {"classes": ("wide",), "fields": ("username", "password1", "password2")},
    #     ),
    # )
    add_fieldsets = (
        (
            None,
            { "fields": ("username", "password1", "password2")},
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ("pk","username", "first_name", "user_type")
    search_fields = ("username", "first_name")
    ordering = ("username",)


admin.site.register(Userprofile, CustomUserAdmin)
admin.site.register(Token)
