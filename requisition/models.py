from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Requisition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_file = models.FileField(upload_to='uploads/')
    amount = models.DecimalField(default=0,max_digits=10, decimal_places=2)
    approved = models.BooleanField(default=False)
    amount_60_percent = models.DecimalField(max_digits=10, decimal_places=2, editable=False, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calculate 60% of the amount and save it to the amount_60_percent field
        self.amount_60_percent = 0.6 * float(self.amount)
        
        # Call the save method of the parent class to perform the actual saving
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title,self.user.username
    
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=20, choices=[('normal', 'Normal User'), ('supervisor', 'Supervisor'), ('administrator', 'Administrator')])

    def __str__(self):
        return self.user_type, self.user.username