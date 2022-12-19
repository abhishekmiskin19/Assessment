from django.db import models
import datetime

# Create your models here.


gender_choices = (
    ('m', 'Male'),
    ('f', 'Female'),
)

class User(models.Model):
    Email = models.EmailField(unique=True)
    Password = models.CharField(max_length=12)    

    class Meta:
        db_table = "User"

    def __str__(self) -> str:
        return self.Email

class Member(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    FullName = models.CharField(max_length=15, default=str(), blank=True)
    Mobile = models.CharField(max_length=10, default=str(), blank=True)
    Gender = models.CharField(max_length=6, choices=gender_choices, default=str(), blank=True)
    
    class Meta:
        db_table = "Member"

    def __str__(self) -> str:
        return self.User.Email

class Chairman(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    FullName = models.CharField(max_length=15, default=str(), blank=True)
    Mobile = models.CharField(max_length=10, default=str(), blank=True)
    Gender = models.CharField(max_length=6, choices=gender_choices, default=str(), blank=True)
    

    class Meta:
        db_table = "Chairman"


class Event(models.Model):
    
    AddEvent = models.CharField(max_length=50, default=str(), blank=True)    
    Date = models.DateField()

    class Meta:
        db_table = "Event"

class Notice(models.Model):
    AddNotices = models.TextField(max_length=150, default=str(), blank=True)
    Date = models.DateField()
    
    class Meta:
        db_table = "Notice"


class Notice_view(models.Model):
    Notices = models.ForeignKey(Notice, on_delete=models.CASCADE)
    

    class Meta:
        db_table = "Notice_view"


class Visitor(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=(20), default=str(), blank=True)
    Mobile = models.CharField(max_length=10, default=str(), blank=True)
    
    class Meta:
        db_table = "Visitor"


class Watchman(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    FullName = models.CharField(max_length=(20), default=str(), blank=True)
    Mobile = models.CharField(max_length=10, default=str(), blank=True)
    

    class Meta:
        db_table = "Watchman"


class Transaction(models.Model):

    
    class Meta:
        db_table = "Transaction"

