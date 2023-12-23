from django.contrib import admin
from .models import Expense, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'description')
    
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'expense_date')

admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Tag, TagAdmin)
