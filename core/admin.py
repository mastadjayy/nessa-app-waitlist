from django.contrib import admin
from .models import Waitlist

@admin.register(Waitlist)
class DegreeEnquiryAdmin(admin.ModelAdmin):
  list_display = ('email', 'date_joined')
  list_filter = ('email', 'date_joined')
