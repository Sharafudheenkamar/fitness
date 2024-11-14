from django.db import models

# Create your models here.

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

class User(models.Model):
    name=models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    photo= models.CharField(max_length=500,default='')
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)

class Trainer(models.Model):
    name = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    certificate = models.CharField(max_length=500)
    photo= models.CharField(max_length=500)
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)

class Category(models.Model):
    categoryname = models.CharField(max_length=100)


class Posture(models.Model):
    CATEGORY = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    TRAINER = models.ForeignKey(Trainer,on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=1000)
    video = models.FileField()

class Chat(models.Model):
    message = models.CharField(max_length=100)
    date= models.CharField(max_length=100)
    FROM_ID = models.ForeignKey(Login,on_delete=models.CASCADE,default=1,related_name="fuser")
    TO_ID = models.ForeignKey(Login,on_delete=models.CASCADE,default=1,related_name="tuser")

class Diet(models.Model):
    title= models.CharField(max_length=100)
    file= models.CharField(max_length=500)
    TRAINER = models.ForeignKey(Trainer,on_delete=models.CASCADE,default=1)

class Payment(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    validity_date = models.DateField(default='2023-11-18')
    amount = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="")
    date = models.DateField(max_length=100,default="")

class Bank(models.Model):
    acholdername = models.CharField(max_length=100)
    card_number = models.CharField(max_length=100)
    cvv = models.CharField(max_length=100)
    expiry_date = models.CharField(max_length=100)
    balance=models.FloatField()


class Rating(models.Model):
    review=models.CharField(max_length=700)
    rating=models.FloatField()
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date=models.DateField()
    POSTURE=models.ForeignKey(Posture, on_delete=models.CASCADE, default=1)

























