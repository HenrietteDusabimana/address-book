from django.shortcuts import render, redirect
from .models import Contacts

# Create your views here.

def index(request):
    search_results =Contacts.objects.order_by('first_name')
    contacts = Contacts.objects.order_by('first_name')
    search_input = request.GET.get('search-area')
    if search_input:
        contacts = Contacts.objects.filter(first_name__icontains=search_input)
        search_results = contacts
        contacts = Contacts.objects.filter(last_name__icontains=search_input)
        search_results = search_results | contacts
    else:
        contacts = Contacts.objects.order_by('first_name')
        search_results = contacts
        search_input = ''
    return render(request, 'index.html', {'contacts': search_results, 'search_input': search_input})

def addContact(request):
    if request.method == 'POST':

        new_contact = Contacts(
            first_name=request.POST['first-name'],
            last_name=request.POST['last-name'],
            email=request.POST['email'],
            phone_number=request.POST['phone-number'],
            )
        new_contact.save()
        return redirect('/')

    return render(request, 'new.html')

def editContact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == 'POST':
        contact.first_name = request.POST['first-name']
        contact.last_name = request.POST['last-name']
        contact.phone_number = request.POST['phone-number']
        contact.email = request.POST['email']
        contact.save()

        return redirect('/profile/'+str(contact.id))
    return render(request, 'edit.html', {'contact': contact})

def deleteContact(request, pk):
    contact = Contacts.objects.get(id=pk)

    if request.method == 'POST':
        contact.delete()
        return redirect('/')

    return render(request, 'delete.html', {'contact': contact})

def contactProfile(request, pk):
    contact = Contacts.objects.get(id=pk)
    return render(request, 'contact-profile.html', {'contact':contact})