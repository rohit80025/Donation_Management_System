from django.contrib import admin
from Donation.models import Donor,Volunteer,DonationArea,Donation,Gallery

# Register your models here.
#admin.site.register(Donor)

@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = ['id','user','contact' ,'address' ,'userpic','regdate']

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id','user','contact' ,'address' ,'userpic','idpic','status','aboutme' ,'regdate' ,'adminremark','updationdate']


@admin.register(DonationArea)
class DonationAreaAdmin(admin.ModelAdmin):
    list_display = ['id','areaname','description' ,'creationdate']


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ['id','donor','donationName' ,'donationpic' ,'colloctionloc','description',
                    'status','donationdate' ,'adminRemarks' ,'volunteer','donationArea',
                    'volunteerRemarks','updationDate']
    
@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id','donation','deliverypic' ,'crationdate']