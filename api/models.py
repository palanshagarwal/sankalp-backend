from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.contrib.auth.models import User

class Event(models.Model):
    class Meta:
        db_table = 'Event'
    start_date = models.DateField(auto_now=False,auto_now_add=False)
    end_date = models.DateField(auto_now=False,auto_now_add=False)
    start_time = models.TimeField(auto_now=False,auto_now_add=False)
    end_time = models.TimeField(auto_now=False,auto_now_add=False)
    title = models.CharField(max_length=250,blank = False)
    venue = models.CharField(max_length=250,blank = False)
    description = models.TextField(default=' ')
    volunteers = models.ManyToManyField(User, blank = True)

    def __unicode__ (self):
        return self.title


class MyModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }
