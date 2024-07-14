from django.contrib import admin
from .models import ContactData

# STEP 2 : register model classes
# STEP 3 : after registration do migration through terminal - python manage.py makemigrations just
# STEP 5 : to convert object data to in table format use this method

class ContactDataAdmin(admin.ModelAdmin) :
    list_display = (
        'id',
        'fullname',
        'email',
        'message',
        'createdAt'
    )

admin.site.register(ContactData, ContactDataAdmin)