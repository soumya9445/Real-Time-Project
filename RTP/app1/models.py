from django.db import models

class RegistrationModel(models.Model):
    rno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    contact=models.IntegerField()
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=70)
    otp=models.IntegerField()
    doj=models.DateField(auto_now_add=True)
    status=models.CharField(max_length=100,default='pending')

class IndustriesModel(models.Model):
    ino= models.AutoField(primary_key=True)
    type=models.CharField(max_length=70)

class ProfileModel(models.Model):
    pno=models.AutoField(primary_key=True)
    person=models.OneToOneField(RegistrationModel,on_delete=models.CASCADE)
    #on_delete means u delete profile model then automatically Registraion Model Is deleted.
    education=models.CharField(max_length=60)
    photo=models.ImageField(upload_to='user_images/')
    resume=models.FileField(upload_to='user_resumes')
    itype=models.ForeignKey(IndustriesModel,on_delete=models.CASCADE)
    #one Industries Model can have multiple Profile Model(One to Many Relation).
    #Many profile makes under one industreies.
    #One Registration Model Can Have One Profile Model.
    #Becz one registration can not have multiple profile,one profile can not have mul registration that's way use one to one relation.

