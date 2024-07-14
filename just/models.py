from django.db import models

# STEP 1 : Create a new database model
class ContactData(models.Model) :
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)