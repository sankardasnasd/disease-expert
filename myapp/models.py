from django.db import models

#
#  Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    type=models.CharField(max_length=100)


class Doctor(models.Model):
    LOGIN=models.ForeignKey(Login,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    pin=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    housename=models.CharField(max_length=100)
    houseno=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="pending")

class User(models.Model):
    LOGIN = models.ForeignKey(Login, on_delete=models.CASCADE, default=1)
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    # gender=models.CharField(max_length=100)
    photo=models.CharField(max_length=300)
    pin=models.CharField(max_length=100)
    housename=models.CharField(max_length=100)
    houseno=models.CharField(max_length=100)
    mobileno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class Schedule(models.Model):
    DOCTOR=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=1)
    date= models.DateField()
    fromtime=models.CharField(max_length=30)
    totime=models.CharField(max_length=30)

class Appointment(models.Model):
    SCHEDULE=models.ForeignKey(Schedule, on_delete=models.CASCADE, default=1)
    USER=models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    date =  models.DateField()
    time = models.CharField(max_length=10)

class Feedback(models.Model):
    USERNAME= models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    feeedback= models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()

class Compliant(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    complain= models.CharField(max_length=300)
    date = models.DateField()
    time = models.TimeField()
    reply= models.CharField(max_length=300)
    status= models.CharField(max_length=100)

class Diease(models.Model):
    dieasename= models.CharField(max_length=100)
    details = models.CharField(max_length=2000)
    image = models.CharField(max_length=2000)

class Symptoms(models.Model):
    symtoms = models.CharField(max_length=500)
    DISEASE=models.ForeignKey(Diease, on_delete=models.CASCADE)

class Chat(models.Model):
    FROMID = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='fromid')
    TOID = models.ForeignKey(Login, on_delete=models.CASCADE,related_name='toid')
    date =  models.DateField()
    message = models.CharField(max_length=2000)


class Review(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Review = models.CharField(max_length=1000)
    Rating = models.FloatField()
    date = models.DateField()
    time = models.TimeField()



class AppoinmentReview(models.Model):
    USER = models.ForeignKey(User, on_delete=models.CASCADE)
    APPOINTMENT = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Review = models.CharField(max_length=1000)
    date = models.DateField()


class Dataset(models.Model):
    disease = models.CharField(max_length=100)
    homogeneity = models.CharField(max_length=100)
    energy = models.CharField(max_length=100)
    dissimilarity = models.CharField(max_length=100)
    correlation = models.CharField(max_length=100)
    contrast = models.CharField(max_length=100)

class Symptoms(models.Model):
    symptoms = models.CharField(max_length=100)
    # description = models.CharField(max_length=500,default="")
    DISEASE=models.ForeignKey(Diease, on_delete=models.CASCADE)