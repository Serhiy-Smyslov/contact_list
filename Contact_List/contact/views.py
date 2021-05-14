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


def contact_profile(request, pk):
    """Show information about choice user."""
    profile = Contact.objects.get(pk=pk)

    context = {'profile': profile}
    return render(request, 'contact-profile.html', context)


def edit_contact(request, pk):
    """Update data about contact."""
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        contact.full_name = request.POST['fullname']
        contact.relationship = request.POST['relationship']
        contact.email = request.POST['email']
        contact.phone_number = request.POST['phone']
        contact.address = request.POST['address']

        contact.save()
        return redirect('/profile/'+str(contact.pk))

    context = {'contact': contact}
    return render(request, 'edit.html', context)
