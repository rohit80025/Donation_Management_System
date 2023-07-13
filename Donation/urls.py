from Donation import views
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.index, name='Home'),
                  path('all_login/', views.all_login, name='all_login'),
                  path('donor_login/', views.donor_login, name='donor_login'),
                  path('Volunteer_login/', views.Volunteer_login, name='Volunteer_login'),
                  path('Admin_login/', views.Admin_login, name='Admin_login'),
                  path('Admin_home/', views.Admin_home, name='Admin_home'),
                  path('Pending_donation/', views.Pending_donation, name='Pending_donation'),
                  path('donor_reg/', views.donor_reg, name='donor_reg'),
                  path('donor_home/', views.donor_home, name='donor_home'),
                  path('logout/', views.Logout, name='logout'),
                  path('donate_now/', views.donate_now, name='donate_now'),
                  path('donation_history/', views.donation_history, name='donation_history'),
                  path('view_donationdetail/<int:pid>', views.view_donationdetail, name='view_donationdetail'),
                  path('accepted_donation/', views.accepted_donation, name='accepted_donation'),
                  path('add_area/', views.add_area, name='add_area'),
                  path('manage_area/', views.manage_area, name='manage_area'),
                  path('edit_area/<int:pid>', views.edit_area, name='edit_area'),
                  path('delete_area/<int:pid>', views.delete_area, name='delete_area'),
                  path('manage_donor/', views.manage_donor, name='manage_donor'),
                  path('view_donor_details/<int:pid>', views.view_donor_details, name='view_donor_details'),
                  path('delete_donor/<int:pid>', views.delete_donor, name='delete_donor'),
                  path('volunteer_reg/', views.volunteer_reg, name='volunteer_reg'),
                  path('volunteer_home/', views.volunteer_home, name='volunteer_home'),
                  path('new_volunteer/', views.new_volunteer, name='new_volunteer'),
                  path('view_volunteer_details/<int:pid>', views.view_volunteer_details, name='view_volunteer_details'),
                  path('accepted_volunteer/', views.accepted_volunteer, name='accepted_volunteer'),
                  path('rejected_volunteer/', views.rejected_volunteer, name='rejected_volunteer'),
                  path('all_volunteer/', views.all_volunteer, name='all_volunteer'),
                  path('delete_volunteer/<int:pid>', views.delete_volunteer, name='delete_volunteer'),
                  path('accepted_donation_details/<int:pid>', views.accepted_donation_details, name='accepted_donation_details'),
                  path('collection_request/', views.collection_request, name='collection_request'),
                  path('donation_collection_details/<int:pid>', views.donation_collection_details, name='donation_collection_details'),
                  path('donation_rec_volunteer/', views.donation_rec_volunteer, name='donation_rec_volunteer'),
                  path('donation_rec_details/<int:pid>', views.donation_rec_details, name='donation_rec_details'),
                  path('donation_not_rec_volunteer/', views.donation_not_rec_volunteer, name='donation_not_rec_volunteer'),
                  path('donation_delivered_volunteer/',views.donation_delivered_volunteer, name='donation_delivered_volunteer'),
                  path('profile_volunteer/',views.profile_volunteer, name='profile_volunteer'),


              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
