from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate, login, logout
import logging
from datetime import date


# Create your views here.


def index(request):
    return render(request, 'index.html')


def all_login(request):
    return render(request, 'all_login.html')


# ///////  code of Volunteer is start ///////

def Volunteer_login(request):
    error = ""  # Initialize error variable
    if request.method == 'POST':
        u = request.POST.get('emailid')
        p = request.POST.get('pwd')
        user = authenticate(username=u, password=p)
        if user:
            try:
                user1 = Volunteer.objects.get(user=user)
                if user1.status != "pending":
                    login(request, user)
                    error = "no"
                else:
                    error = "not"  # Set error if status is pending
            except Volunteer.DoesNotExist:
                error = "not"  # Set error if Volunteer.DoesNotExist exception occurs
        else:
            error = "yes"  # Set error if authentication fails
    return render(request, 'volunteer/Volunteer_login.html', locals())


def volunteer_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        idpic = request.FILES['idpic']
        address = request.POST['address']
        aboutme = request.POST['aboutme']
        try:
            user = User.objects.create_user(
                first_name=fn, last_name=ln, username=em, password=pwd)
            Volunteer.objects.create(user=user, contact=contact,
                                     userpic=userpic, idpic=idpic, address=address, aboutme=aboutme, status="pending")
            error = "no"
        except:
            error = "yes"
    return render(request, 'volunteer/volunteer_reg.html', locals())


def volunteer_home(request):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    return render(request, 'volunteer/volunteer_home.html')


def collection_request(request):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Volunteer Allocated")
    return render(request, 'volunteer/collection_request.html', locals())


def donation_collection_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        volunteerRemarks = request.POST['volunteerRemarks']

        try:

            donation.status = status
            donation.volunteerRemarks = volunteerRemarks
            donation.updationDate = date.today()
            donation.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'volunteer/donation_collection_details.html', locals())

def donation_rec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation Received")
    return render(request, 'volunteer/donation_rec_volunteer.html', locals())

# def donation_rec_details(request, pid):
#     if not request.user.is_authenticated:
#         return redirect('Volunteer_login')
#     donation = Donation.objects.get(id=pid)
#     error = ""
#     if request.method == "POST":
#         status = request.POST['status']
#         deliverypic = request.FILES['deliverypic']
#
#         try:
#             donation.status = status
#             donation.updationDate = date.today()
#             donation.save()
#             Gallery.objects.create(donation=donation, deliverypic=deliverypic)
#             error = "no"
#         except:
#             error = "yes"
#
#     return render(request, 'volunteer/donation_rec_details.html', locals())

def donation_rec_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    donation = Donation.objects.get(id=pid)
    error = ""
    if request.method == "POST":
        status = request.POST['status']
        deliverypic = request.FILES['deliverypic']

        try:
            donation.status = status
            donation.updationDate = date.today()
            donation.save()
            Gallery.objects.create(donation=donation, deliverypic=deliverypic)  # Corrected variable name
            error = "no"
        except:
            error = "yes"

    return render(request, 'volunteer/donation_rec_details.html', locals())

def donation_not_rec_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation notReceived")
    return render(request, 'volunteer/donation_not_rec_volunteer.html', locals())

def donation_delivered_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    user = request.user
    volunteer = Volunteer.objects.get(user=user)
    donation = Donation.objects.filter(volunteer=volunteer, status="Donation Deliverd Successfully")
    return render(request, 'volunteer/donation_delivered_volunteer.html', locals())




# /////// code of Volunteer is End ///////

# Admin All Code Start
def Admin_login(request):
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"

    return render(request, 'admin/Admin_login.html', locals())


def Admin_home(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')
    return render(request, 'admin/admin_home.html')


def Pending_donation(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    donation = Donation.objects.filter(status="pending")
    return render(request, 'admin/Pending_donation.html', locals())


def add_area(request):
    if not request.user.is_authenticated:
        return redirect('admin_login')

    if request.method == "POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        try:
            DonationArea.objects.create(areaname=areaname, description=description)
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/add_area.html', locals())


def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    area = DonationArea.objects.all()
    return render(request, 'admin/manage_area.html', locals())


def edit_area(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    area = DonationArea.objects.get(id=pid)
    if request.method == "POST":
        areaname = request.POST['areaname']
        description = request.POST['description']
        area.areaname = areaname
        area.description = description
        try:
            area.save()
            error = "no"
        except:
            error = "yes"
    return render(request, 'admin/edit_area.html', locals())


def delete_area(request, pid):
    area = DonationArea.objects.get(id=pid)
    area.delete()
    return redirect('manage_area')


def manage_area(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    area = DonationArea.objects.all()
    return render(request, 'admin/manage_area.html', locals())


def manage_donor(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    donor = Donor.objects.all()
    return render(request, 'admin/manage_donor.html', locals())


def view_donor_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('admin_login')
    donor = Donor.objects.get(id=pid)

    return render(request, 'admin/view_donor_details.html', locals())


def delete_donor(request, pid):
    user = User.objects.get(id=pid)
    user.delete()
    return redirect('manage_area')


def new_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    volunteer = Volunteer.objects.filter(status="pending")
    return render(request, 'admin/new_volunteer.html', locals())


def view_volunteer_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('Volunteer_login')
    volunteer = Volunteer.objects.get(id=pid)

    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

        try:
            volunteer.adminremark = adminremark
            volunteer.status = status
            volunteer.updationdate = date.today()
            volunteer.save()
            error = "no"
        except:
            error = "yes"

    return render(request, 'admin/view_volunteer_details.html', locals())


def accepted_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    volunteer = Volunteer.objects.filter(status="accept")
    return render(request, 'admin/accepted_volunteer.html', locals())


def rejected_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    volunteer = Volunteer.objects.filter(status="reject")
    return render(request, 'admin/rejected_volunteer.html', locals())


def all_volunteer(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    volunteer = Volunteer.objects.all()
    return render(request, 'admin/all_volunteer.html', locals())


def delete_volunteer(request, pid):
    User.objects.get(id=pid).delete()
    return redirect('all_volunteer')


def accepted_donation_details(request, pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    donation = Donation.objects.get(id=pid)
    donationarea = DonationArea.objects.all()
    volunteer = Volunteer.objects.all()

    if request.method == "POST":
        donationareaid = request.POST['donationareaid']
        volunteerid = request.POST['volunteerid']
        da = DonationArea.objects.get(id=donationareaid)
        vo = Volunteer.objects.get(id=volunteerid)

        try:
            donation.donationArea = da
            donation.volunteer = vo
            donation.status = "Volunteer Allocated"
            donation.updationDate = date.today()
            donation.save()
            error = "No"
        except:
            error = "yes"

    return render(request, 'admin/accepted_donation_details.html', locals())


# Admin all code end


# Donor All code

def donor_login(request):
    if request.method == 'POST':
        u = request.POST['emailid']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        if user:
            login(request, user)
            error = "no"
        else:
            error = "yes"
    return render(request, 'donor/donor_login.html', locals())


def donor_reg(request):
    error = ""
    if request.method == 'POST':
        fn = request.POST['firstname']
        ln = request.POST['lastname']
        em = request.POST['email']
        contact = request.POST['contact']
        pwd = request.POST['pwd']
        userpic = request.FILES['userpic']
        address = request.POST['address']
        try:
            user = User.objects.create_user(
                first_name=fn, last_name=ln, username=em, password=pwd)
            Donor.objects.create(user=user, contact=contact,
                                 userpic=userpic, address=address)
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor/donor_reg.html', locals())


def donor_home(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')

    return render(request, 'donor/donor_home.html')


def Logout(request):
    logout(request)
    return redirect('Home')


def donate_now(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    if request.method == "POST":
        donationName = request.POST['donationName']
        donationpic = request.FILES['donationpic']
        collactionloc = request.POST['collactionloc']
        description = request.POST['description']
        try:
            Donation.objects.create(donor=donor, donationName=donationName, donationpic=donationpic,
                                    colloctionloc=collactionloc, description=description, status="pending", )
            error = "no"
        except:
            error = "yes"
    return render(request, 'donor/donate_now.html', locals())


def donation_history(request):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    user = request.user
    donor = Donor.objects.get(user=user)
    donation = Donation.objects.filter(donor=donor)
    return render(request, 'donor/donation_history.html', locals())


def view_donationdetail(request, pid):
    if not request.user.is_authenticated:
        return redirect('donor_login')
    donation = Donation.objects.get(id=pid)

    if request.method == "POST":
        status = request.POST['status']
        adminremark = request.POST['adminremark']

        try:
            donation.adminRemarks = adminremark
            donation.status = status
            donation.updationDate = date.today()
            donation.save()
            error = "No"
        except:
            error = "yes"

    return render(request, 'donor/view_donationdetail.html', locals())


def accepted_donation(request):
    if not request.user.is_authenticated:
        return redirect('Admin_login')

    donation = Donation.objects.filter(status="accept")
    return render(request, 'admin/accepted_donation.html', locals())
