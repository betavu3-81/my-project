from django.db import models

# Create your models here.
class Departs(models.Model):
    name_dep = models.CharField(max_length=100)

#def __str__(self):             
        #return self.name_dep

class Posts(models.Model):
    idposts = models.IntegerField(default=0)
    name_post = models.CharField(max_length=100)

class Users(models.Model):
    idusers = models.IntegerField(default=0)
    fio = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    phone = models.IntegerField(default=0)
    posts = models.ForeignKey(Posts)
    departs = models.ForeignKey(Departs)

class Equip(models.Model):
    id_equip = models.IntegerField(default=0)
    name_equip = models.CharField(max_length=100)
    invert_nambe = models.IntegerField(default=0)
    departs = models.ForeignKey(Departs)

class Cats(models.Model):
    id_cats = models.IntegerField(default=0)
    name_cats = models.CharField(max_length=60)
    description = models.CharField(max_length=200)

class Types1(models.Model):
    id_types = models.IntegerField(default=0)
    name_types = models.CharField(max_length=60)
    manufacturer = models.CharField(max_length=60)
    order_name = models.CharField(max_length=60)
    price = models.IntegerField(default=0)
    note = models.CharField(max_length=250)
    cats = models.ForeignKey(Cats)

class Arms(models.Model):
    id_arms = models.IntegerField(default=0)
    name_arms = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    users = models.ForeignKey(Users)

class Rel_types(models.Model):
    name_rel_types = models.CharField(max_length=100)
    id_rel_types = models.IntegerField(default=0)

class Relatives(models.Model):
    id_relatives = models.IntegerField(default=0)
    date_relatives = models.DateTimeField('date published')
    description_relatives = models.CharField(max_length=200)
    rel_types = models.ForeignKey(Rel_types)
    users = models.ForeignKey(Users)
    equip = models.ForeignKey(Equip)

class Repairs(models.Model):
    id_repairs = models.IntegerField(default=0)
    nambe_repairs = models.IntegerField(default=0)
    start_date_repairs = models.DateTimeField('date published')
    finish_date_repairs = models.DateTimeField('date published')
    text_problem = models.CharField(max_length=300)
    users = models.ForeignKey(Users)
    equip = models.ForeignKey(Equip)

class Calls(models.Model):
    id_calls = models.IntegerField(default=0)
    nambe_calls = models.IntegerField(default=0)
    date_calls = models.DateTimeField('date published')
    description_calls = models.CharField(max_length=300)
    users = models.ForeignKey(Users)
    equip = models.ForeignKey(Equip)