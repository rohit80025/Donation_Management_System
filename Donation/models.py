from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Donor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    regdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    

class Volunteer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    contact = models.CharField(max_length=15,null=True)
    address = models.CharField(max_length=300,null=True)
    userpic = models.FileField(null=True)
    idpic = models.FileField(null=True)
    status = models.CharField(max_length=20)
    aboutme = models.CharField(max_length=300,null=True)
    regdate = models.DateTimeField(auto_now=True)
    adminremark = models.CharField(max_length=300,null=True)
    updationdate = models.DateField(null=True)
    def __str__(self):
        return self.user.username
    
class DonationArea(models.Model):
   areaname = models.CharField(max_length=200,null=True)
   description = models.CharField(max_length=300,null = True)
   creationdate = models.DateTimeField(auto_now_add=True)
   def __str__(self):
        return self.areaname
   
# class Donation(models.Model):
#     donor = models.ForeignKey(Donor,on_delete=models.CASCADE)
#     donationName = models.CharField(max_length=100,null=True)
#     donationpic = models.FileField(null=True)
#     colloctionloc = models.CharField(max_length=50,null=True)
#     description = models.CharField(max_length=300,null=True)
#     status = models.CharField(max_length=50)
#     donationdate = models.DateTimeField(auto_now_add=True)
#     adminRemarks = models.CharField(max_length=300,null=True)
#     volunteer = models.ForeignKey(Volunteer,on_delete=models.CASCADE)
#     donationArea = models.ForeignKey(DonationArea,on_delete=models.CASCADE,null=True)
#     volunteerRemarks = models.CharField(max_length=300,null=True)
#     updationDate = models.DateTimeField(null=True)
#     def __str__(self):
#         return self.id

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.SET_NULL, null=True)
    donationName = models.CharField(max_length=100, null=True)
    donationpic = models.FileField(null=True)
    colloctionloc = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=50)
    donationdate = models.DateTimeField(auto_now_add=True)
    adminRemarks = models.CharField(max_length=300, null=True)
    volunteer = models.ForeignKey(Volunteer, on_delete=models.SET_NULL, null=True)
    donationArea = models.ForeignKey(DonationArea, on_delete=models.CASCADE, null=True)
    volunteerRemarks = models.CharField(max_length=300, null=True)
    updationDate = models.DateTimeField(null=True)

    def __str__(self):
        return str(self.id)

    
class Gallery(models.Model):
    donation =models.ForeignKey(Donation,on_delete=models.CASCADE)
    deliverypic = models.FileField(null=True)
    crationdate = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.id



