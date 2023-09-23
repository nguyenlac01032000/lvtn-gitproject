# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Contact
import smtplib
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
            email_message = form.cleaned_data['messages']
            send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL, fail_silently=False,)
            smtplib.SMTP('smtp.gmail.com', 587)
            return render(request, 'contact/success.html')
    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)

# def inquiry(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         email = request.POST['email']
#         phone = request.POST['phone']
#         messages = request.POST['message']
#         user_id = request.POST['user_id']
#
#         contact = Contact( first_name=first_name, last_name=last_name, email=email, phone=phone, messages=messages, user_id=user_id )
#
#         contact.save()
#         messages.success(request, 'Your request has been submitted')
#         return redirect(med/+med_id)

# def inquiry(request):
#     if request.method == 'POST':
#         form = contacts(request.POST)
#         if form.is_valid():
#             contact= form.save(commit=False)
#             contact.job_creator = request.user
#             contact.save()
#
#             return redirect('inquiry')
#     else:
#         form = contacts()
#     return render(request,
#                   'inquiry',
#                   {'form': form}
#
#                   )
