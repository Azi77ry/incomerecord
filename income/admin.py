
# Register your models here.
from django.contrib import admin
from .models import Income

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('date', 'amount', 'description')  # Fields to display in the admin list view
    list_filter = ('date',)  # Add filters for the date field
    search_fields = ('description',)  # Add search functionality for the description field