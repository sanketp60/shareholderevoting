from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import uuid

class Company(models.Model):
    CompanyID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Name = models.CharField(max_length=50)
    Volume = models.CharField(max_length=20)
    MarketCap = models.CharField(max_length=20)
    FaceValue = models.CharField(max_length=20)

    def __str__(self):
        return self.Name
    
class Poll(models.Model):
    PollID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Content = models.TextField()
    Company = models.ForeignKey(Company, on_delete=models.CASCADE)
    CreateDateTime = models.DateTimeField(default=timezone.now, editable=False)
    EndDateTime = models.DateTimeField()
    ResultDateTime = models.DateTimeField()

class UserData(models.Model):
    UserID = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    Pan = models.CharField(max_length=10)
    DateOfBirth = models.DateField()

    def __str__(self):
        return self.UserID.username
    

