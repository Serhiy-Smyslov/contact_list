from django.shortcuts import render, redirect

from contact.models import Contact


def index(request):
    """Show all user contacts."""
    contacts = Contact.objects.all()
    context = {
        'contacts': contacts,
    }
    return render(request, 'index.html', context)


def add_contact(request):
    """Add new contact from special form."""
    if request.method == 'POST':
        new_contact = Contact(
            full_name=request.POST['fullname'],
            relationship=request.POST['relationship'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            address=request.POST['address']
        )
        new_contact.save()
        return redirect('index')
    return render(request, 'new.html')
