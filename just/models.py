from django.db import models

# STEP 1 : Create a new database model
class ContactData(models.Model) :
    fullname = models.CharField(max_length=100)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    message = models.TextField()
    profile = models.ImageField(upload_to="images/")
    createdAt = models.DateTimeField(auto_now_add=True)