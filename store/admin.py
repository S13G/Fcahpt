from django.contrib import admin

from store.models import Newsletter, Car, Contact, Setting


# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'passengers', 'luggage', 'doors']
    list_filter = ['name', 'price', 'passengers']
    list_per_page = 10
    search_fields = ['name']


@admin.register(Newsletter)
class NewsLetter(admin.ModelAdmin):
    list_display = ['email']
    list_per_page = 10
    search_fields = ['email']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_filter = ['name', 'email']
    list_per_page = 10
    search_fields = ['name', 'email']


@admin.register(Setting)
class SettingsAdmin(admin.ModelAdmin):
    list_display = ['website_name', 'company_email', 'phone_number']

    def has_add_permission(self, request) -> bool:
        return False if self.get_queryset(request).count() == 1 else True

    def get_actions(self, request):
        actions = super().get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions