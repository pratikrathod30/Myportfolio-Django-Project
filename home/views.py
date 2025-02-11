from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib import messages
# Create your views here.
def index(request):

     if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_content = request.POST.get('message')

        # Create and save the Contact object
        contact_entry = Contact(name=name, email=email, message=message_content)
        contact_entry.save()  # Correct way to save
        messages.success(request, "Your message has been sent successfully!")
        return redirect('/')
     
     return render(request,"index.html")

