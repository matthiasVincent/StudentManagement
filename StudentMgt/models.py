from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField()
    def __str__(self):
        return "{}".format(self.name)
    class Meta:
        db_table = "departments"

class Level(models.Model):
    name = name = models.CharField(max_length=50, null=False)
    depts = models.ManyToManyField(Department)
    created_at = models.DateTimeField()
    def __str__(self):
        return "{}".format(self.name)
    class Meta:
        db_table = "classes"
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    id_user = models.IntegerField(default=0)
    dept_id = models.ForeignKey(Department, on_delete=models.CASCADE)
    sex = models.CharField(max_length=10, null=False)
    StuClass = models.ForeignKey(Level, on_delete=models.CASCADE)
    admin_no = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(default=datetime.utcnow())
    full_name = models.CharField(max_length=40)
    @property
    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)
    class Meta:
        db_table = "students"

    def __str__(self):
        return "{}".format(self.full_name)
    
class Subject(models.Model):
    name = models.CharField(max_length=50, null=False)
    depts = models.ManyToManyField(Department)
    created_at = models.DateTimeField()
    def __str__(self):
        return "{}".format(self.name)
    class Meta:
        db_table = "subjects"